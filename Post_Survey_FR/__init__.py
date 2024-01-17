from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'Post_Survey_FR'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    clear=models.LongStringField(label= "Were the instructions clear?")
    easy = models.LongStringField(label="Ressentez-vous un effet d’apprentissage ? Pensez- vous avoir mieux réussi que la semaine dernière?")
    object = models.LongStringField(label="Quel est selon-vous l'objet de l'étude? Pourquoi?")
    comment = models.LongStringField(label="Avez vous des commentaires/suggestions?")


    rank_mary= models.IntegerField(
        choices=[[1, ' Rang 1'],
                 [2, 'Rang 2'],
                 [3, ' Rang 3'],
                 [4, ' Rang 4'], ],
        label="<b> Mary: </b>",
        widget=widgets.RadioSelectHorizontal,

    )
    rank_emma = models.IntegerField(
        choices=[[1, ' Rang 1'],
                 [2, 'Rang 2'],
                 [3, ' Rang 3'],
                 [4, ' Rang 4'], ],
        label="<b> Emma: </b>",
        widget=widgets.RadioSelectHorizontal,

    )
    rank_james = models.IntegerField(
        choices=[[1, ' Rang 1'],
                 [2, 'Rang 2'],
                 [3, ' Rang 3'],
                 [4, ' Rang 4'], ],
        label="<b> James: </b>",
        widget=widgets.RadioSelectHorizontal,

    )
    rank_john = models.IntegerField(
        choices=[[1, ' Rang 1'],
                 [2, 'Rang 2'],
                 [3, ' Rang 3'],
                 [4, ' Rang 4'], ],
        label="<b> John: </b>",
        widget=widgets.RadioSelectHorizontal,

    )
    rank_name = models.IntegerField(
        choices=[[1, ' Très utile'],
                 [2, 'Utile'],
                 [3, ' Un peu utile'],
                 [4, ' Inutile'], ],
        label="<b> Prénom fictif:  </b>",
        widget=widgets.RadioSelectHorizontal,

    )
    rank_gender = models.IntegerField(
        choices=[[1, ' Très utile'],
                 [2, 'Utile'],
                 [3, ' Un peu utile'],
                 [4, ' Inutile'], ],
        label="<b> Genre:  </b>",
        widget=widgets.RadioSelectHorizontal,
    )
    rank_born = models.IntegerField(
        choices=[[1, ' Très utile'],
                 [2, 'Utile'],
                 [3, ' Un peu utile'],
                 [4, ' Inutile'], ],
        label="<b> Naissance en Ile De France: </b>",
        widget=widgets.RadioSelectHorizontal,
    )
    rank_commute = models.IntegerField(
        choices=[[1, ' Très utile'],
                 [2, 'Utile'],
                 [3, ' Un peu utile'],
                 [4, ' Inutile'], ],
        label="<b> Temps de Trajet: </b>",
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
    BFNE_q12 = models.IntegerField(
        choices=[1, 2, 3, 4, 5],

        # widget=widgets.Select,
        verbose_name=' 12. I often worry that I will say or do the wrong things.',
        widget=widgets.RadioSelectHorizontal,

    )

    SPSRQ_q1 = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],

        # widget=widgets.Select,
        verbose_name=' 1.Do you often refrain from doing something because you are afraid of it being illegal? ',
        widget=widgets.RadioSelectHorizontal,

    )

    SPSRQ_q2 = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],

        # widget=widgets.Select,
        verbose_name=' 2.Does the good prospect of obtaining money motivate you strongly to do some things? ',
        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q3 = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],

        # widget=widgets.Select,
        verbose_name=' 3.	Do you prefer not to ask for something you are not sure you will obtain it? ',
        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q4 = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],

        # widget=widgets.Select,
        verbose_name=' 4.	Are you frequently encouraged to act by the possibility of being valued in your work, in your studies, with your friends or with your family? ',
        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q5 = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],

        # widget=widgets.Select,
        verbose_name=' 5.	Are you often afraid of new or unexpected situations? ',
        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q6 = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],

        # widget=widgets.Select,
        verbose_name=' 6.	Do you often meet people that you find physically attractive? ',
        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q7 = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],

        # widget=widgets.Select,
        verbose_name='7.	Is it difficult for you to telephone someone you do not know?  ',
        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q8 = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],

        # widget=widgets.Select,
        verbose_name=' 8.	Do you like taking some drugs because of the pleasure you get from them?  ',
        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q9 = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],

        # widget=widgets.Select,
        verbose_name=' 9.	Do you often renounce your rights when you know you can avoid a quarrel with a person or an organization?  ',
        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q10 = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],

        # widget=widgets.Select,
        verbose_name='10.	Do you often do things to be praised?   ',
        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q11 = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],

        # widget=widgets.Select,
        verbose_name=' 11.	As a child, were you troubled by punishments at home or in school? ',
        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q12 = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],

        # widget=widgets.Select,
        verbose_name='12.	Do you like being the center of attention at a party or a social meeting?  ',
        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q13 = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],

        # widget=widgets.Select,
        verbose_name='13.	In tasks that you are not prepared for, do you attach great importance to the possibility of failure?   ',
        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q14 = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],

        # widget=widgets.Select,
        verbose_name='14.	Do you spend a lot of your time on obtaining a good image?  ',
        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q15 = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],

        # widget=widgets.Select,
        verbose_name=' 15.	Are you easily discouraged in difficult situations? ',
        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q16 = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],

        # widget=widgets.Select,
        verbose_name='16.	Do you need people to show their affection for you all the time?  ',
        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q17 = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],

        # widget=widgets.Select,
        verbose_name=' 17.	Are you a shy person? ',
        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q18 = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],

        # widget=widgets.Select,
        verbose_name=' 18.	When you are with a group, do you try to make your opinions the most intelligent or the funniest? ',
        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q19 = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],

        # widget=widgets.Select,
        verbose_name='19.	Whenever possible, do you avoid demonstrating your skills for fear of being embarrassed?  ',
        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q20 = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],

        # widget=widgets.Select,
        verbose_name=' 20.	Do you often take the opportunity to pick up people you find attractive? ',
        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q21 = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],

        # widget=widgets.Select,
        verbose_name=' 21.	When you are with a group, do you have difficulties selecting a good topic to talk about? ',
        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q22 = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],

        # widget=widgets.Select,
        verbose_name='22.	As a child, did you do a lot of things to get people’s approval?  ',
        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q23 = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],

        # widget=widgets.Select,
        verbose_name=' 23.	Is it often difficult for you to fall asleep when you think about things you have done or must do? ',
        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q24 = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],

        # widget=widgets.Select,
        verbose_name='24.	Does the possibility of social advancement, move you to action, even if this involves not playing fair?  ',
        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q25 = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],

        # widget=widgets.Select,
        verbose_name=' 25.	Do you think a lot before complaining in a restaurant if your meal is not well prepared? ',
        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q26 = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],

        # widget=widgets.Select,
        verbose_name='26.	Do you generally give preference to those activities that imply an immediate gain? ',
        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q27 = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],

        # widget=widgets.Select,
        verbose_name=' 27.	Would you be bothered if you had to return to a store when you noticed you were given the wrong change? ',
        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q28 = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],

        # widget=widgets.Select,
        verbose_name='28.	Do you often have trouble resisting the temptation of doing forbidden things?   ',
        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q29 = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],

        # widget=widgets.Select,
        verbose_name=' 29.	Whenever you can, do you avoid going to unknown places? ',
        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q30 = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],

        # widget=widgets.Select,
        verbose_name=' 30.	Do you like to compete and do everything you can do to win? ',
        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q31 = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],

        # widget=widgets.Select,
        verbose_name='31.	Are you often worried by things you said or did?  ',
        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q32 = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],

        # widget=widgets.Select,
        verbose_name=' 32.	Is it easy for you to associate tastes and smells to very pleasant events? ',
        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q33 = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],

        # widget=widgets.Select,
        verbose_name='33.	Would it be difficult for you to ask your boss for a raise (salary increase)?  ',
        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q34 = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],

        # widget=widgets.Select,
        verbose_name='34.	Are there a large number of objects or sensations that remind you of pleasant events?  ',
        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q35 = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],

        # widget=widgets.Select,
        verbose_name=' 35.	Do you generally avoid speaking in public? ',
        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q36 = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],

        # widget=widgets.Select,
        verbose_name=' 36.	When you start to play with a slot machine, is it often difficult for you to stop?  ',
        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q37 = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],

        # widget=widgets.Select,
        verbose_name='37.	Do you, on a regular basis, think that you could do more things if it was not for your insecurity or fear?   ',
        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q38 = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],

        # widget=widgets.Select,
        verbose_name=' 38.	Do you sometimes do things for quick gains? ',
        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q39 = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],

        # widget=widgets.Select,
        verbose_name='39.	Comparing yourself to people you know, are you afraid of many things?  ',
        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q40 = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],

        # widget=widgets.Select,
        verbose_name=' 40.	Does your attention easily stray from your work in the presence of an attractive stranger? ',
        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q41 = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],

        # widget=widgets.Select,
        verbose_name=' 41.	Do you often find yourself worrying about things to the extent that performance in intellectual abilities is impaired? ',
        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q42 = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],

        # widget=widgets.Select,
        verbose_name='42.	Are you interested in money to the point of being able to do risky jobs?  ',
        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q43 = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],

        # widget=widgets.Select,
        verbose_name='43.	Do you often refrain from doing something you like in order not to be rejected or disapproved by others? ',
        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q44 = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],

        # widget=widgets.Select,
        verbose_name='44.	Do you like to put competitive ingredients in all of your activities? ',
        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q45 = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],

        # widget=widgets.Select,
        verbose_name=' 45.	Generally, do you pay more attention to threats than to pleasant events? ',
        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q46 = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],

        # widget=widgets.Select,
        verbose_name=' 46.	Would you like to be a socially powerful person?  ',
        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q47 = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],

        # widget=widgets.Select,
        verbose_name=' 47.	Do you often refrain from doing something because of your fear of being embarrassed? ',
        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q48 = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],

        # widget=widgets.Select,
        verbose_name=' 48.	Do you like displaying your physical abilities even though this may involve danger? ',
        widget=widgets.RadioSelectHorizontal,

    )







    # PAGES
class Instructions(Page):
    form_model= 'player'

class WaitforSurvey(WaitPage):
    pass




class RankingTrait(Page):
    form_model= 'player'
    form_fields = ['rank_name', 'rank_gender', 'rank_born', 'rank_commute']

class WaitPageforPart2(WaitPage):
    pass
class Ranking_gender_instructions(Page):
    pass

class WaitPageforRanking(WaitPage):
    pass

class Ranking_gender(Page):
    form_model= 'player'
    form_fields = [ 'rank_emma', 'rank_james', 'rank_john','rank_mary',]


class WaitPageforPart3(WaitPage):
    pass

class BFNE(Page):
    form_model = 'player'
    form_fields = ['BFNE_q1', 'BFNE_q2', 'BFNE_q3', 'BFNE_q4', 'BFNE_q5','BFNE_q6','BFNE_q7','BFNE_q8','BFNE_q9','BFNE_q10','BFNE_q11','BFNE_q12']


class WaitforPart4(WaitPage):
    pass

class SPSRQ(Page):
    form_model = 'player'
    form_fields = ['SPSRQ_q1', 'SPSRQ_q2', 'SPSRQ_q3', 'SPSRQ_q4', 'SPSRQ_q5','SPSRQ_q6','SPSRQ_q7','SPSRQ_q8','SPSRQ_q9','SPSRQ_q10','SPSRQ_q11','SPSRQ_q12', 'SPSRQ_q13', 'SPSRQ_q14','SPSRQ_q15','SPSRQ_q16','SPSRQ_q17','SPSRQ_q18','SPSRQ_q19','SPSRQ_q20','SPSRQ_q21','SPSRQ_q22','SPSRQ_q23','SPSRQ_q24','SPSRQ_q25','SPSRQ_q26','SPSRQ_q27','SPSRQ_q28','SPSRQ_q29','SPSRQ_q30','SPSRQ_q31','SPSRQ_q32','SPSRQ_q33','SPSRQ_q34','SPSRQ_q35','SPSRQ_q36','SPSRQ_q37','SPSRQ_q38','SPSRQ_q39','SPSRQ_q40','SPSRQ_q41','SPSRQ_q42','SPSRQ_q43','SPSRQ_q44','SPSRQ_q45','SPSRQ_q46','SPSRQ_q47', 'SPSRQ_q48']


class feedback(Page):
    form_model = 'player'
    form_fields = ['easy','object','comment']

class WaitforEnd(WaitPage):
    pass


class End(Page):
    form_model = 'player'



page_sequence = [ Instructions,WaitforSurvey,  RankingTrait,  WaitPageforPart2, Ranking_gender_instructions, WaitPageforRanking, Ranking_gender, WaitPageforPart3, BFNE, WaitforPart4, SPSRQ, WaitforEnd, End]
#page_sequence = [ Instructions, WaitPageforPart3, feedback]
