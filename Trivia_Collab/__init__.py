from otree.api import *
import random




doc = """
Trivia Task: Communication + can resubmit once 
"""

class C(BaseConstants):
    NAME_IN_URL = 'Trivia_Collab'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 6
    TIME_PER_PROBLEM = 60
    #PAYMENT_CURRENT_PER_ITEM = cu(1)



class Subsession(BaseSubsession):
   pass

class Group(BaseGroup):
   pass

class Player(BasePlayer):
     answerA= models.IntegerField(label=" What is the likelihood (in %) that Option 1 is correct?")
     answerB = models.IntegerField(label="What is the likelihood (in %) that Option 2 is correct?")
     answerC = models.IntegerField(label="What is the likelihood (in %) that Option 3 is correct?")
     answerD= models.IntegerField(label="What is the likelihood (in %) that Option 4 is correct?")
     answer1=models.IntegerField(widget=widgets.RadioSelectHorizontal,
                       choices=[1,2,3,4], label= "Coordinate with your partner using the chat to select the correct answer:")
     answer2 = models.IntegerField(widget=widgets.RadioSelectHorizontal,
                                   choices=[1, 2, 3, 4],
                                   label="Coordinate with your partner using the chat to select the correct answer:")
     correctG1=models.BooleanField( doc="Whether the first answer provided in group is correct.", default=False)
     timed_out = models.BooleanField(doc="Whether the participant submitted an answer within the allotted time.")




def set_correctG1(player):
    player.participant.answer1 = player.answer1
    correct_answers = [3, 3, 3, 1, 4, 1]
    for player, correct in zip(player.in_all_rounds(), correct_answers):
        if player.answer1 == correct:
            correctG1 = True
        else:
            correctG1 = False

    player.correctG1 = correctG1




def get_timeout_seconds(player):
        participant = player.participant
        import time
        return participant.expiry - time.time()

class Start(Page):

    @staticmethod
    def before_next_page(player, timeout_happened):
        participant = player.participant
        import time

        # remember to add 'expiry' to PARTICIPANT_FIELDS. 3 minutes to count as many correct tables.
        participant.expiry = time.time() + 6*60

    def is_displayed(player):
        return player.round_number == 1



class Solo(Page):
    form_model = 'player'
    form_fields = ['answerA', 'answerB', 'answerC', 'answerD']

    @staticmethod
    def get_timeout_seconds(player):
        participant = player.participant
        import time
        return min(C.TIME_PER_PROBLEM,participant.expiry - time.time())

    def is_displayed(player):
        return get_timeout_seconds(player) > 3

class WaitForChat(WaitPage):
    @staticmethod
    def get_timeout_seconds(player):
        participant = player.participant
        import time
        return participant.expiry - time.time()

    def is_displayed(player):
        return get_timeout_seconds(player) > 3

class Chat(Page):
    @staticmethod
    def get_timeout_seconds(player):
        participant = player.participant
        import time
        return  participant.expiry - time.time()

    form_model = 'player'
    form_fields = ['answer1']

    def is_displayed(player):
        return get_timeout_seconds(player) > 3
    def before_next_page(player, timeout_happened):
        set_correctG1(player)

class WaitforNext(WaitPage):
    @staticmethod
    def get_timeout_seconds(player):
        participant = player.participant
        import time
        return participant.expiry - time.time()

    def is_displayed(player):
        return get_timeout_seconds(player) > 3

class Chat2(Page):
    @staticmethod
    def get_timeout_seconds(player):
        participant = player.participant
        import time
        return  participant.expiry - time.time()

    form_model = 'player'
    form_fields = ['answer2']

    def is_displayed(player):
        return player.correctG1 == False and get_timeout_seconds(player) > 3



class WaitforNext2(WaitPage):
    @staticmethod
    def get_timeout_seconds(player):
        participant = player.participant
        import time
        return participant.expiry - time.time()

    def is_displayed(player):
        return player.correctG1 == False and get_timeout_seconds(player) > 3


page_sequence = [Start,Solo,WaitForChat, Chat, WaitforNext,  Chat2, WaitforNext2]