from otree.api import *
import random



doc = """
Counting Task 
"""

class C(BaseConstants):
    NAME_IN_URL = 'Counting2'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 6
    TIME_PER_PROBLEM = 45
    #PAYMENT_CURRENT_PER_ITEM = cu(1)



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):

            pass



class Player(BasePlayer):
     answerA= models.IntegerField(label="How many 0s are in Sub-Table A?")
     answerB = models.IntegerField(label="How many 0s are in Sub-Table B?")
     answerA2 = models.IntegerField(label="How many 0s are in Sub-Table A?")
     answerB2 = models.IntegerField(label="How many 0s are in Sub-Table B?")
     sum1=models.IntegerField(doc="First Sum submitted")
     sum2=models.IntegerField(doc="Second Sum submitted")
     correct = models.BooleanField( doc="Whether the first sum provided is correct.")
     timed_out = models.BooleanField(doc="Whether the participant submitted an answer within the allotted time.")

def set_sum1(player):
        sum1= player.answerA + player.answerB
        player.sum1=sum1
        player.participant.sum1=player.sum1
        player.participant.answerA=player.answerA
        player.participant.answerB = player.answerB


def set_sum2(player):
    sum2 = player.answerA2 + player.answerB2
    player.sum2 = sum2

def set_correct(player):
    correct_answers = [49, 52, 49, 50, 46, 53]
    for player, correct in zip(player.in_all_rounds(), correct_answers):
        if player.sum1 == correct:
            correct = True
        else:
            correct = False

    player.correct = correct


class Start(Page):

    @staticmethod
    def before_next_page(player, timeout_happened):
        participant = player.participant
        import time

        # remember to add 'expiry' to PARTICIPANT_FIELDS. 3 minutes to count as many correct tables.
        participant.expiry = time.time() + 3*60

    def is_displayed(player):
        return player.round_number == 1
 #def get_timeout_seconds(player):
   # participant = player.participant
   # import time
  #  return participant.expiry - time.time()

class Count(Page):
    form_model = 'player'
    form_fields = ['answerA', 'answerB']

    @staticmethod
    def get_timeout_seconds(player):
        participant = player.participant
        import time
        return min(C.TIME_PER_PROBLEM,participant.expiry - time.time())

    def before_next_page(player, timeout_happened):
        # player.timed_out = True if player.timed_out else False
        # if player.round_number == C.NUM_ROUNDS:
        set_sum1(player)
        set_correct(player)



class Count2(Page):
    @staticmethod
    def get_timeout_seconds(player):
        participant = player.participant
        import time
        return  participant.expiry - time.time()

    def is_displayed(player):
        return player.correct == False

    form_model = 'player'
    form_fields = ['answerA2', 'answerB2']

    def before_next_page(player, timeout_happened):
        set_sum2(player)

page_sequence = [Start,Count, Count2]