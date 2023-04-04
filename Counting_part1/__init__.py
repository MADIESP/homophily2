from otree.api import *
import random



doc = """
Counting Task: Part 1: task performed individually  
"""

class C(BaseConstants):
    NAME_IN_URL = 'Counting_part1'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 4
    TIME_PER_PROBLEM = 45
    #PAYMENT_CURRENT_PER_ITEM = cu(1)



class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    pass


class Player(BasePlayer):
     answerA_ind= models.IntegerField(label="How many 0s are in Sub-Table A?")
     answerB_ind = models.IntegerField(label="How many 0s are in Sub-Table B?")
     sum=models.IntegerField(doc="Sum submitted ")
     correct_ind = models.BooleanField( doc="Whether the sum is correct.")
     timed_out = models.BooleanField(doc="Whether the participant submitted an answer within the allotted time.")
     points = models.IntegerField(doc="Number of correct answers {0,...5}.")

def set_sum(player):
        sum= player.answerA_ind + player.answerB_ind
        player.sum=sum
        player.participant.sum=player.sum
        player.participant.answerA_ind=player.answerA_ind
        player.participant.answerB_ind = player.answerB_ind



def set_correct_ind(player):
    correct_answers = [78, 78, 69, 62]
    for player, correct in zip(player.in_all_rounds(), correct_answers):
        if player.sum == correct:
            correct_ind = True
        else:
            correct_ind = False

    player.correct_ind = correct_ind

#def set_payoffs(group):

def get_points(player:BasePlayer):
        points = 0
        correct_answers = [78, 78, 69, 62]
        for player, correct in zip(player.in_all_rounds(), correct_answers):
            # print(p.answer, correct, p.answer == correct)
            points = points + 1 if player.sum == correct else points
            player.points = points

            player.payoff = player.points
            player.participant.ind_payoff = player.payoff




#def get_timeout_seconds(player):
   # participant=player.participant
    #import time
    #return participant.expiry - time.time()

class Start(Page):

    #@staticmethod
    #def before_next_page(player, timeout_happened):
        #participant = player.participant
        #import time

        # remember to add 'expiry' to PARTICIPANT_FIELDS. 3 minutes to count as many correct tables.
        ##participant.expiry = time.time() + 1 * 60

    def is_displayed(player):
        return player.round_number == 1




class Count(Page):
    timeout_seconds = C.TIME_PER_PROBLEM
    form_model = 'player'
    form_fields = ['answerA_ind', 'answerB_ind']

    timer_text = 'Time left to count this table:'

    #def is_displayed(player):
        #return get_timeout_seconds(player) > 3

    #@staticmethod
    #def get_timeout_seconds(player):
        #participant = player.participant
        #import time
        #return min(C.TIME_PER_PROBLEM, participant.expiry - time.time())


    #def is_displayed(player):
        #return get_timeout_seconds(player) > 3

    def before_next_page(player, timeout_happened):
        # player.timed_out = True if player.timed_out else False
        # if player.round_number == C.NUM_ROUNDS:
        set_sum(player)
        set_correct_ind(player)
        get_points(player)


# def is_displayed(player):
       # return get_timeout_seconds(player) > 3






page_sequence = [Start, Count]