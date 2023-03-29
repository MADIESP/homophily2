from otree.api import *
import random



doc = """
Counting Task: Communication (can't submit again an answer). They only get
a feedback on whether the group's answer is correct. 
"""

class C(BaseConstants):
    NAME_IN_URL = 'Communication2'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 6
    TIME_PER_PROBLEM = 45
    #PAYMENT_CURRENT_PER_ITEM = cu(1)



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):

 same1= models.BooleanField( doc="Whether players submit the same first sum as a group")
 #same2= models.BooleanField( doc="Whether players submit the same second sum as a group")






class Player(BasePlayer):
     answerA= models.IntegerField(label="How many 0s are in Sub-Table A?")
     answerB = models.IntegerField(label="How many 0s are in Sub-Table B?")
     sumE = models.IntegerField(label="How many 0s are in the Table?")
     sum1I=models.IntegerField(doc="First Sum submitted (individually) ")
     sum1 = models.IntegerField(label="How many 0s are in the Table?", doc="Sum submitted individually ")
     sum2 = models.IntegerField(label="How many 0s are in the Table?", doc=" First Sum submitted in group ")
     same1_ind=models.BooleanField( doc="Whether both participants submit the same sum (first time)")
     same2_ind = models.BooleanField(doc="Whether both participants submit the same sum (second time)")
     #sum3=models.IntegerField(label="How many 0s are in the Table?", doc="Second Sum submitted in group")
     correct = models.BooleanField( doc="Whether the first sum provided is correct.")
     correctG1=models.BooleanField( doc="Whether the first sum provided in group is correct.")
     timed_out = models.BooleanField(doc="Whether the participant submitted an answer within the allotted time.")
     correctE=models.BooleanField(default=True)
     confidence=models.IntegerField(widget=widgets.RadioSelect,
                       choices=[1,2,3,4,5,6,7,8,9,10], label= "How confident are you that the number of 0s you just counted in the table is correct?")

def set_sum1(player):
        sum1= player.answerA + player.answerB
        player.sum1=sum1
        player.participant.sum1=player.sum1
        player.participant.answerA=player.answerA
        player.participant.answerB = player.answerB


def set_correctG1(player:Player):
    player.participant.sum2 = player.sum2
    correct_answers = [49, 52, 49, 50, 46, 53]
    for player, correct in zip(player.in_all_rounds(), correct_answers):
        if player.sum2 == correct:
            correctG1 = True
        else:
            correctG1 = False

    player.correctG1 = correctG1

def set_correctError(player):
    player.participant.sumE = player.sumE
    correct_answers = [49, 52, 49, 50, 46, 53]
    for player, correct in zip(player.in_all_rounds(), correct_answers):
        if player.sumE == correct:
            correctE = True
        else:
            correctE = False

    player.correctE = correctE


def set_same1(group):
    for player in group.get_players():
        p1 = group.get_player_by_id(1)
        p2 = group.get_player_by_id(2)

        if p1.sum2 == p2.sum2:
            same1 = True
        else:
            same1 = False

        group.same1 = same1
        player.same1_ind = same1




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
        participant.expiry = time.time() + 6*60

    def is_displayed(player):
        return player.round_number == 1



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



class Confidence(Page):
    form_model = 'player'
    form_fields = ['confidence']


class WaitforChat(WaitPage):
    @staticmethod
    def get_timeout_seconds(player):
        participant = player.participant
        import time
        return participant.expiry - time.time()


class Chat(Page):
    @staticmethod
    def get_timeout_seconds(player):
        participant = player.participant
        import time
        return  participant.expiry - time.time()

    form_model = 'player'
    form_fields = ['sum2']

    def before_next_page(player, timeout_happened):
        set_correctG1(player)

class WaitforNext(WaitPage):
    @staticmethod
    def get_timeout_seconds(player):
        participant = player.participant
        import time
        return participant.expiry - time.time()

    def after_all_players_arrive(group:Group):
     set_same1(group)

class Error1(Page):
    @staticmethod
    def get_timeout_seconds(player):
        participant = player.participant
        import time
        return  participant.expiry - time.time()

    def is_displayed(player):
        return player.same1_ind == False

    form_model = 'player'
    form_fields = ['sumE']



    def before_next_page(player, timeout_happened):
        set_correctError(player)

class WaitforError1(WaitPage):
    @staticmethod
    def get_timeout_seconds(player):
        participant = player.participant
        import time
        return participant.expiry - time.time()
    def is_displayed(player):
        return player.same1_ind == False

class feedback(Page):
    @staticmethod
    def get_timeout_seconds(player):
        participant = player.participant
        import time
        return  participant.expiry - time.time()

    form_model = 'player'

    def is_displayed(player):
        return player.correctG1 == True and player.same1_ind == True


class feedback_neg(Page):
    @staticmethod
    def get_timeout_seconds(player):
        participant = player.participant
        import time
        return  participant.expiry - time.time()

    form_model = 'player'

    def is_displayed(player):
        return player.correctG1 == False and player.same1_ind == True

class feedback_error(Page):
        @staticmethod
        def get_timeout_seconds(player):
            participant = player.participant
            import time
            return participant.expiry - time.time()

        form_model = 'player'

        def is_displayed(player):
            return player.correctE == True and player.same1_ind == False


class feedback_error_neg(Page):
        @staticmethod
        def get_timeout_seconds(player):
            participant = player.participant
            import time
            return participant.expiry - time.time()

        form_model = 'player'


        def is_displayed(player):
            return player.correctE == False and player.same1_ind == False


    #def before_next_page(player, timeout_happened):
        #set_correctG2(player)

class WaitforNext2(WaitPage):
    @staticmethod
    def get_timeout_seconds(player):
        participant = player.participant
        import time
        return participant.expiry - time.time()

    def is_displayed(player):
        return player.correctG1 == False and player.same1_ind == True

    #def after_all_players_arrive(group:Group):
     #set_same2(group)

class WaitforNext2_error(WaitPage):
    @staticmethod
    def get_timeout_seconds(player):
        participant = player.participant
        import time
        return participant.expiry - time.time()

    def is_displayed(player):
        return player.correctE == False and player.same1_ind == False

    #def after_all_players_arrive(group:Group):
    # set_same2(group)





#class Count2(Page):
   # @staticmethod
   # def get_timeout_seconds(player):
       # participant = player.participant
       # import time
       # return  participant.expiry - time.time()

    #def is_displayed(player):
        #return player.correct == False

   # form_model = 'player'
   # form_fields = ['answerA2', 'answerB2']

    #def before_next_page(player, timeout_happened):
        #set_sum2(player)

page_sequence = [Start,Count, Confidence, WaitforChat, Chat, WaitforNext, Error1, WaitforError1, feedback, feedback_neg, feedback_error, feedback_error_neg, WaitforNext2, WaitforNext2_error]