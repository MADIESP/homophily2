from otree.api import *
from settings import SESSION_CONFIG_DEFAULTS, SESSION_CONFIGS, PARTICIPANT_FIELDS, LANGUAGE_CODE

import threading
import random
import itertools
from call_api import call_api

doc = """
The consent form
"""


class api_thread(threading.Thread):
    def __init__(self, label, vars, config, room_name, my_room_name=""):
        threading.Thread.__init__(self)
        self.vars = vars
        self.label = label
        self.config = config
        self.room_name = room_name
        self.my_room_name = my_room_name
        self.done = False
        self.error = False
        self.msg = ""
        # helper function to execute the threads
    def run(self):
        rooms = call_api("GET1", self.config, 'rooms')
        print("rooms:", rooms)
        from datetime import datetime
        for r in rooms:
            if r['name'] == self.room_name and not r['name'] == self.my_room_name:
                if not r['session_code'] is None:
                    newvars = {}
                    for k in self.vars:
                        newvars[k] = self.vars[k]
                    res = call_api("POST", self.config, 'participant_vars',
                                   room_name=r['name'], participant_label=self.label, vars=newvars)
                    if 'error' in res and res['error']:
                        self.done = False
                        self.error = True
                        self.msg += "\n room %s : " % r['name']+res['msg']
                        print(datetime.now(), "!Error in call_api for participant %s, room '%s' : " % (
                            self.label, r['name']), res['msg'])
                    else:
                        print(datetime.now(), "participant %s, call_api done for room '%s' with the following vars : " % (
                            self.label, r['name']), newvars)
                        # print(datetime.now()," (vars for %s, room %s) "%(self.label,r['name'], newvars)
                else:
                    self.done = False
                    self.error = True
                    self.msg += "\n room %s not initialized! " % r['name']
                    print(datetime.now(), "room %s not initialized!" % (r['name']))
        if not self.error:
            self.done = True
            print("sending vars_done=1 to room %s" % self.my_room_name)
            call_api("POST1", self.config, 'participant_vars', room_name=self.my_room_name,
                     participant_label=self.label, vars=(dict(vars_done=1)))
        else:
            print("sending error message to  %s" % self.my_room_name)
            call_api("POST1", self.config, 'participant_vars', room_name=self.my_room_name,
                     participant_label=self.label, vars=(dict(error=int(self.error), err_msg='error: '+self.msg)))


class api_create_roomsession(threading.Thread):
    def __init__(self, config, name, npart):
        threading.Thread.__init__(self)
        self.name = name
        self.npart = npart
        self.config = config

        # helper function to execute the threads
    def run(self):
        import datetime,os,time
        os.environ['TZ'] = 'Europe/Paris'
        if hasattr(time,'tzset'): time.tzset()
        x = datetime.datetime.now()
        sdate=x.strftime("%Y-%m-%d %H:%M")
        data = call_api("POST1", self.config, 
            'sessions',
            session_config_name=self.name,
            room_name=self.name,
            num_participants=self.npart,
            label = self.name+", "+sdate
            #modified_session_config_fields=dict(num_apples=10, abc=[1, 2, 3]),
        )
        from pprint import pprint
        pprint(data)

class C(BaseConstants):
    NAME_IN_URL = 'redirectapp'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # id_choosen=models.IntegerField()
    api_thread_started = models.BooleanField(initial=False)


def creating_session(subsession: Subsession):
    session = subsession.session
    players = subsession.get_players()
    if not session.config["Tr"] in ['T2','T1','T0','Control']:
        raise ValueError('The Treatment should be set to a Control (or T0), T1 or T2 "Configure session"!')
    if subsession.round_number == 1:
        #creating rooms for redirection
        surbook_if_less_then_8=False
        nparts_main=0
        nparts_surb=0
        if surbook_if_less_then_8:
            for i in range(len(players),0,-1):
                if i % 8 == 0 and i < 24:
                    nparts_main = i
                    break
                else:
                    nparts_surb += 1
        else:
            nparts_main=min(len(players),16)
            if nparts_main<len(players): nparts_surb=len(players)-nparts_main
        configs = dict(SERVER_URL=session.config['SERVER_URL'], REST_KEY=session.config['REST_KEY'])
        if nparts_main > 0: 
            thread1 = api_create_roomsession(configs, get_next_room(session,True), nparts_main)
            thread1.start()
        if nparts_surb > 0:
            thread2 = api_create_roomsession(configs, get_next_room(session,False), nparts_surb)
            thread2.start()
    # initcycle=range(2,8)
    # random.shuffle(initcycle)
    # seqs = itertools.cycle(initcycle)
    for player in players:
        # player.id_choosen=next(seqs)
        player.participant.error = 0

def get_next_room(session,main):
    tr=0
    next_room = 'Control_Main' if main else "Control_Surbooking"
    if session.config["Tr"] != 'Control': tr=int(session.config["Tr"][-1])
    if tr == 1:
        next_room = 'T1_Main' if main else "T1_Surbooking"
    if tr == 2:
        next_room = 'T2_Main' if main else "T1_Surbooking"
    return next_room


# PAGES


class RedirectPage(Page):
    @staticmethod
    def live_method(player, data):
        status = data[:data.find('|')]
        if status == 'load':
            # player.intro_nloads+=1
            newlabel = player.participant.label if not (
                not player.participant.label) else player.participant.code
            return {player.id_in_group: "wait"}
        if status == 'check':
            if not player.participant.vars_done:
                return {player.id_in_group: player.participant.err_msg if player.participant.error else "wait"}
            else:
                return {player.id_in_group: "ok"}

    @staticmethod
    def vars_for_template(player: Player):
        httphost = player.session.config['SERVER_URL']
        newlabel = player.participant.label if not ( not player.participant.label) else player.participant.code
        next_room=get_next_room(player.session,player.participant.Main)
        rp = httphost+'/room/'+next_room+'/?participant_label='+newlabel
        varnames=["gender","BornIDF","CommutingTime","Main","Surbooking"]
        if not player.field_maybe_none('api_thread_started') or player.participant.error:
            newvars = {}
            for v in varnames:
                newvars[v]=getattr(player.participant,v)
            if newvars != {}:
                room=player.session.get_room()
                room_name = '' if room is None else room.name
                thread1 = api_thread(newlabel, newvars, dict(
                    SERVER_URL=player.session.config['SERVER_URL'], 
                    REST_KEY=player.session.config['REST_KEY']
                    ), next_room, room_name)
                thread1.start()
                player.api_thread_started = 1
                player.participant.vars_done = 0
                player.participant.err_msg = "no error message"
                player.participant.error = 0
        return dict(redirect_page=rp, redirect_directly=1-player.api_thread_started)

page_sequence = [RedirectPage]
