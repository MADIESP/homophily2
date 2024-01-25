from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'Post_Survey_FR'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    CHOICES=[[1, 'Non'], [2, 'Plutôt Non'],[2, 'Plutôt Oui'],[2, 'Oui'] ]


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
        verbose_name=' 1. Je m’inquiète de l’opinion des autres même quand je sais que cela n’a aucune importance.',
        widget=widgets.RadioSelectHorizontal,

    )
    BFNE_q2 = models.IntegerField(
        choices=[1, 2, 3, 4, 5],

        # widget=widgets.Select,
        verbose_name='  2. Je reste imperturbable même si je sais que quelqu’un se fait une opinion défavorable de moi.',
        widget=widgets.RadioSelectHorizontal,

    )
    BFNE_q3 = models.IntegerField(
        choices=[1, 2, 3, 4, 5],

        # widget=widgets.Select,
        verbose_name=' 3. J’ai souvent peur que les gens s’aperçoivent de mes défauts.',
        widget=widgets.RadioSelectHorizontal,

    )
    BFNE_q4 = models.IntegerField(
        choices=[1, 2, 3, 4, 5],

        # widget=widgets.Select,
        verbose_name=' 4. Je suis souvent indifférent(e) à ce que les autres pensent de moi.',
        widget=widgets.RadioSelectHorizontal,
    )
    BFNE_q5 = models.IntegerField(
        choices=[1, 2, 3, 4, 5],

        # widget=widgets.Select,
        verbose_name=' 5. J’ai peur d’être désapprouvé(e).',
        widget=widgets.RadioSelectHorizontal,

    )
    BFNE_q6 = models.IntegerField(
        choices=[1, 2, 3, 4, 5],

        # widget=widgets.Select,
        verbose_name=' 6.J’ai peur que les autres me trouvent des défauts.',
        widget=widgets.RadioSelectHorizontal,

    )
    BFNE_q7 = models.IntegerField(
        choices=[1, 2, 3, 4, 5],

        # widget=widgets.Select,
        verbose_name='7. L’opinion des autres à mon égard m’est égal.',
        widget=widgets.RadioSelectHorizontal,

    )
    BFNE_q8 = models.IntegerField(
        choices=[1, 2, 3, 4, 5],

        # widget=widgets.Select,
        verbose_name=' 8. Lorsque je parle à quelqu’un, je m’inquiète de ce qu’il pense de moi.',

        widget=widgets.RadioSelectHorizontal,
    )
    BFNE_q9 = models.IntegerField(
        choices=[1, 2, 3, 4, 5],

        # widget=widgets.Select,
        verbose_name=' 9. Je m’inquiète de l’impression que je donne aux autres.',
        widget=widgets.RadioSelectHorizontal,

    )
    BFNE_q10 = models.IntegerField(
        choices=[1, 2, 3, 4, 5],

        # widget=widgets.Select,
        verbose_name=' 10. Savoir que quelqu’un me juge ne perturbe pas.',
        widget=widgets.RadioSelectHorizontal,

    )
    BFNE_q11 = models.IntegerField(
        choices=[1, 2, 3, 4, 5],

        # widget=widgets.Select,
        verbose_name=' 11. Parfois, je pense que je m’inquiète trop de ce que les autres pensent de moi.',
        widget=widgets.RadioSelectHorizontal,
    )
    BFNE_q12 = models.IntegerField(
        choices=[1, 2, 3, 4, 5],

        # widget=widgets.Select,
        verbose_name=' 11. Parfois, je pense que je m’inquiète trop de ce que les autres pensent de moi. ',
        widget=widgets.RadioSelectHorizontal,

    )
    BFNE_q12 = models.IntegerField(
        choices=[1, 2, 3, 4, 5],

        # widget=widgets.Select,
        verbose_name=' 12. Je m’inquiète souvent à l’idée de commettre une erreur ou de dire quelque chose d’inapproprié.',
        widget=widgets.RadioSelectHorizontal,

    )

    SPSRQ_q1 = models.IntegerField(
        choices=C.CHOICES,

        # widget=widgets.Select,
        verbose_name=' 1.Préférez-vous ne pas demander quelque chose quand vous n’êtes pas sûr de l’obtenir ?  ',
        widget=widgets.RadioSelectHorizontal,

    )

    SPSRQ_q2 = models.IntegerField(
        choices=C.CHOICES,

        # widget=widgets.Select,
        verbose_name=' 2.Avez-vous souvent peur des situations nouvelles ou inattendues ?  ',
        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q3 = models.IntegerField(
        choices=C.CHOICES,

        # widget=widgets.Select,
        verbose_name=' 3.Faites-vous souvent des choses pour recevoir des compliments ?  ',
        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q4 = models.IntegerField(
        choices=C.CHOICES,

        # widget=widgets.Select,
        verbose_name=' 4. Aimez-vous être le centre d’attention lors d’une fête ou d’un autre événement ?  ',
        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q5 = models.IntegerField(
        choices=C.CHOICES,

        # widget=widgets.Select,
        verbose_name=' 5.Pour les tâches pour lesquelles vous n’êtes pas préparé(e), Attachez-vous une grande importance à la possibilité d’échouer ?  ',
        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q6 = models.IntegerField(
        choices=C.CHOICES,

        # widget=widgets.Select,
        verbose_name=' 6.Consacrez-vous beaucoup de votre temps pour acquérir une bonne image ? ',
        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q7 = models.IntegerField(
        choices=C.CHOICES,

        # widget=widgets.Select,
        verbose_name='7. Etes-vous facilement découragé(e) face aux situations difficiles ?   ',
        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q8 = models.IntegerField(
        choices=C.CHOICES,

        # widget=widgets.Select,
        verbose_name=' 8.Quand vous étiez enfant, est-ce que vous faisiez beaucoup de choses dans le but d’obtenir l’approbation des gens ?',

        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q9 = models.IntegerField(
        choices=C.CHOICES,

        # widget=widgets.Select,
        verbose_name=' 9.	Est-ce que la possibilité de progresser socialement vous incite à l’action, même si cela vous conduit à ne pas agir de manière correcte ? ',
        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q10 = models.IntegerField(
        choices=C.CHOICES,

        # widget=widgets.Select,
        verbose_name='10.Donnez-vous généralement la préférence aux activités débouchant sur un gain immédiat ?',
        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q11 = models.IntegerField(
        choices=C.CHOICES,

        # widget=widgets.Select,
        verbose_name=' 11.	Est-ce que vous aimez la compétition et faire tout ce que vous pouvez pour gagner ?  ',
        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q12 = models.IntegerField(
        choices=C.CHOICES,

        # widget=widgets.Select,
        verbose_name='12.Pensez que vous pourriez faire plus de choses si vous n’étiez pas retenu(e) par un sentiment de peur ou d’insécurité ? ',
        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q13 = models.IntegerField(
        choices=C.CHOICES,

        # widget=widgets.Select,
        verbose_name='13. Etes-vous souvent inquiet(ète) des choses que vous avez dites ou faites ?    ',
        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q14 = models.IntegerField(
        choices=C.CHOICES,

        # widget=widgets.Select,
        verbose_name='14.Serait-il difficile pour vous de demander une augmentation de salaire à votre patron ?   ',
        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q15 = models.IntegerField(
        choices=C.CHOICES,

        # widget=widgets.Select,
        verbose_name=' 15. Essayez-vous généralement d’éviter de vous exprimer en public ?  ',
        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q16 = models.IntegerField(
        choices=C.CHOICES,

        # widget=widgets.Select,
        verbose_name='16. . Par rapport  aux autres, diriez-vous que vous êtes  quelqu’ un qui a peur de beaucoup de choses ? ',
        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q17 = models.IntegerField(
        choices=C.CHOICES,

        # widget=widgets.Select,
        verbose_name=' 17. Vous inquiétez-vous souvent au point que vos performances intellectuelles s’en trouvent diminuées ? ',
        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q18 = models.IntegerField(
        choices=C.CHOICES,

        # widget=widgets.Select,
        verbose_name=' Vous abstenez-vous souvent de faire quelque chose que vous aimez pour ne pas être réprimandé(e) ou désapprouvé(e) par les autres ? ',
        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q19 = models.IntegerField(
        choices=C.CHOICES,

        # widget=widgets.Select,
        verbose_name='19. Aimez-vous ajouter des éléments compétitifs dans toutes vos activités ?  ',
        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q20 = models.IntegerField(
        choices=C.CHOICES,

        # widget=widgets.Select,
        verbose_name=' 20. Voudriez-vous être une personne socialement influente ?  ',
        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q21 = models.IntegerField(
        choices=C.CHOICES,

        # widget=widgets.Select,
        verbose_name=' 21. Vous abstenez-vous souvent de faire des choses par peur d’être embarrassé(e) ? ',
        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q22 = models.IntegerField(
        choices=C.CHOICES,

        # widget=widgets.Select,
        verbose_name='22. Aimez-vous prouver vos capacités physiques même si cela pourrait impliquer un danger ? ',
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
