from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'Post_Survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    clear=models.LongStringField(label= "Were the instructions clear?")
    easy = models.LongStringField(label="Was it easy to count the 0s in 30s?")
    object = models.LongStringField(label="What do you think is the object of our study? Why?")
    comment = models.LongStringField(label="Do you have any comments/suggestions?")


    rank_mary= models.IntegerField(
        choices=[[1, ' Rank 1st'],
                 [2, 'Rank 2nd'],
                 [3, ' Rank 3rd'],
                 [4, ' Rank 4th'], ],
        label="<b> Mary: </b>",
        widget=widgets.RadioSelectHorizontal,

    )
    rank_emma = models.IntegerField(
        choices=[[1, ' Rank 1st'],
                 [2, 'Rank 2nd'],
                 [3, ' Rank 3rd'],
                 [4, ' Rank 4th'], ],
        label="<b> Emma: </b>",
        widget=widgets.RadioSelectHorizontal,

    )
    rank_james = models.IntegerField(
        choices=[[1, ' Rank 1st'],
                 [2, 'Rank 2nd'],
                 [3, ' Rank 3rd'],
                 [4, ' Rank 4th'], ],
        label="<b> James: </b>",
        widget=widgets.RadioSelectHorizontal,

    )
    rank_john = models.IntegerField(
        choices=[[1, ' Rank 1st'],
                 [2, 'Rank 2nd'],
                 [3, ' Rank 3rd'],
                 [4, ' Rank 4th'], ],
        label="<b> John: </b>",
        widget=widgets.RadioSelectHorizontal,

    )
    rank_name = models.IntegerField(
        choices=[[1, ' Very Useful'],
                 [2, 'Useful'],
                 [3, ' Somehow Useful'],
                 [4, ' Irrelevant'], ],
        label="<b> Player's Name: </b>",
        widget=widgets.RadioSelectHorizontal,

    )
    rank_study = models.IntegerField(
        choices=[[1, ' Very Useful'],
                 [2, 'Useful'],
                 [3, ' Somehow Useful'],
                 [4, ' Irrelevant'], ],
        label=" <b> Player's Year of Study: </b>",
        widget=widgets.RadioSelectHorizontal,
    )
    rank_born = models.IntegerField(
        choices=[[1, ' Very Useful'],
                 [2, 'Useful'],
                 [3, ' Somehow Useful'],
                 [4, ' Irrelevant'], ],
        label="<b> Whether the Player was born in Ile de France: </b>",
        widget=widgets.RadioSelectHorizontal,
    )
    rank_job = models.IntegerField(
        choices=[[1, ' Very Useful'],
                 [2, 'Useful'],
                 [3, ' Somehow Useful'],
                 [4, ' Irrelevant'], ],
        label="<b> Whether the Player has a Student Job: </b>",
        widget=widgets.RadioSelectHorizontal,
    )

    BFNE_q1 = models.IntegerField(
        choices=[1, 2, 3, 4, 5],

        # widget=widgets.Select,
        verbose_name=' 1. I worry about what other people will think of me even when I know it doesn´t make any difference.',
        widget=widgets.RadioSelectHorizontal,

    )
    BFNE_q2 = models.IntegerField(
        choices=[1, 2, 3, 4, 5],

        # widget=widgets.Select,
        verbose_name='  2. I am unconcerned even if I know people are forming an unfavorable impression of me.',
        widget=widgets.RadioSelectHorizontal,

    )
    BFNE_q3 = models.IntegerField(
        choices=[1, 2, 3, 4, 5],

        # widget=widgets.Select,
        verbose_name=' 3. I am frequently afraid of other people noticing my shortcomings.',
        widget=widgets.RadioSelectHorizontal,

    )
    BFNE_q4 = models.IntegerField(
        choices=[1, 2, 3, 4, 5],

        # widget=widgets.Select,
        verbose_name=' 4. I rarely worry about what kind of impression I am making on someone.',
        widget=widgets.RadioSelectHorizontal,

    )
    BFNE_q5 = models.IntegerField(
        choices=[1, 2, 3, 4, 5],

        # widget=widgets.Select,
        verbose_name=' 5. I am afraid others will not approve of me.',
        widget=widgets.RadioSelectHorizontal,

    )
    BFNE_q6 = models.IntegerField(
        choices=[1, 2, 3, 4, 5],

        # widget=widgets.Select,
        verbose_name=' 6. I am afraid that people will find fault with me.',
        widget=widgets.RadioSelectHorizontal,

    )
    BFNE_q7 = models.IntegerField(
        choices=[1, 2, 3, 4, 5],

        # widget=widgets.Select,
        verbose_name='7.  Other people´s opinions of me do not bother me.',
        widget=widgets.RadioSelectHorizontal,

    )
    BFNE_q8 = models.IntegerField(
        choices=[1, 2, 3, 4, 5],

        # widget=widgets.Select,
        verbose_name=' 8. When I am talking to someone, I worry about what they may be thinking about me.',
        widget=widgets.RadioSelectHorizontal,

    )
    BFNE_q9 = models.IntegerField(
        choices=[1, 2, 3, 4, 5],

        # widget=widgets.Select,
        verbose_name=' 9. I am usually worried about what kind of impression I make.',
        widget=widgets.RadioSelectHorizontal,

    )
    BFNE_q10 = models.IntegerField(
        choices=[1, 2, 3, 4, 5],

        # widget=widgets.Select,
        verbose_name=' 10. If I know someone is judging me, it has little effect on me.',
        widget=widgets.RadioSelectHorizontal,

    )
    BFNE_q11 = models.IntegerField(
        choices=[1, 2, 3, 4, 5],

        # widget=widgets.Select,
        verbose_name=' 11. Sometimes I think I am too concerned with what other people think of me.',
        widget=widgets.RadioSelectHorizontal,

    )
    BFNE_q12 = models.IntegerField(
        choices=[1, 2, 3, 4, 5],

        # widget=widgets.Select,
        verbose_name=' 12. I often worry that I will say or do the wrong things.',
        widget=widgets.RadioSelectHorizontal,

    )



# PAGES
class Instructions(Page):
    form_model= 'player'

class WaitforSurvey(WaitPage):
    pass

class Ranking_gender(Page):
    form_model= 'player'
    form_fields = ['rank_mary', 'rank_emma', 'rank_james', 'rank_john']

class WaitPageforPart2(WaitPage):
    pass


class RankingTrait(Page):
    form_model= 'player'
    form_fields = ['rank_name', 'rank_study', 'rank_born', 'rank_job']

class WaitPageforPart3(WaitPage):
    pass

class BFNE(Page):
    form_model = 'player'
    form_fields = ['BFNE_q1', 'BFNE_q2', 'BFNE_q3', 'BFNE_q4', 'BFNE_q5','BFNE_q6','BFNE_q7','BFNE_q8','BFNE_q9','BFNE_q10','BFNE_q11','BFNE_q12']

class feedback(Page):
    form_model = 'player'
    form_fields = ['clear','easy','object','comment']







#page_sequence = [ Ranking_gender, WaitPageforPart2, RankingTrait, WaitPageforPart3, BFNE]
page_sequence = [ Instructions, WaitPageforPart3, feedback]
