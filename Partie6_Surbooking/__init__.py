from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'Partie6_Surbooking'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    CHOICES=[[1, 'Non'], [2, 'Plutôt Non'],[3, 'Plutôt Oui'],[4, 'Oui']]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass



class Player(BasePlayer):
    ind_payoff = models.IntegerField()
    Message1 = models.IntegerField(
        choices=[[1, 'Positif' ],[2 ,'Négatif'], [ 3,'Neutre' ]],
        # widget=widgets.Select,
        verbose_name=' Pas de pression, ce tableau n’est pas simple ! ',
        widget=widgets.RadioSelectHorizontal,

    )
    Message2 = models.IntegerField(
        choices=[[1, 'Positif'], [2, 'Négatif'], [3, 'Neutre']],
        # widget=widgets.Select,
        verbose_name=' Ne t’inquiète pas, cela arrive de faire des erreurs ! ',
        widget=widgets.RadioSelectHorizontal,

    )
    Message3 = models.IntegerField(
        choices=[[1, 'Positif'], [2, 'Négatif'], [3, 'Neutre']],
        # widget=widgets.Select,
        verbose_name=' Je sais que c’est difficile, mais essaye de te concentrer davantage. ',
        widget=widgets.RadioSelectHorizontal,

    )
    Message4 = models.IntegerField(
        choices=[[1, 'Positif'], [2, 'Négatif'], [3, 'Neutre']],
        # widget=widgets.Select,
        verbose_name='Il est très important de donner la bonne réponse, tu devrais essayer une autre technique de comptage. ',
        widget=widgets.RadioSelectHorizontal,

    )

    question_genre = models.IntegerField(
        choices=[[1,'Les femmes comptent correctement plus de tableaux.'], [2,'Les hommes comptent correctement plus de tableaux.'], [3,'Il n’y a pas de différence entre les femmes et les hommes.']],

        # widget=widgets.Select,
        verbose_name='En moyenne, pensez-vous que ce sont les femmes ou les hommes qui comptent le plus de tableaux correctement ? ',
        widget=widgets.RadioSelect,

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
        verbose_name=' 10. Savoir que quelqu’un me juge ne me perturbe pas.',
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
        verbose_name=' 12. Je m’inquiète souvent à l’idée de commettre une erreur ou de dire quelque chose d’inapproprié.',
        widget=widgets.RadioSelectHorizontal,

    )

    SPSRQ_q1 = models.IntegerField(
        choices=C.CHOICES,

        # widget=widgets.Select,
        verbose_name=' 1. Préférez-vous ne pas demander quelque chose lorsque vous n’êtes pas sûr de l’obtenir ?  ',
        widget=widgets.RadioSelectHorizontal,

    )

    SPSRQ_q2 = models.IntegerField(
        choices=C.CHOICES,

        # widget=widgets.Select,
        verbose_name=' 2. Avez-vous souvent peur des situations nouvelles ou inattendues ?  ',
        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q3 = models.IntegerField(
        choices=C.CHOICES,

        # widget=widgets.Select,
        verbose_name=' 3. Faites-vous souvent des choses pour recevoir des compliments ?  ',
        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q4 = models.IntegerField(
        choices=C.CHOICES,

        # widget=widgets.Select,
        verbose_name=' 4. Aimez-vous être le centre de l’attention lors d’une fête ou d’un événement ?  ',
        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q5 = models.IntegerField(
        choices=C.CHOICES,

        # widget=widgets.Select,
        verbose_name=' 5. Pour les tâches pour lesquelles vous n’êtes pas préparé(e), attachez-vous une grande importance à la possibilité d’échouer ?  ',
        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q6 = models.IntegerField(
        choices=C.CHOICES,

        # widget=widgets.Select,
        verbose_name=' 6. Consacrez-vous beaucoup de temps pour acquérir une bonne image ? ',
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
        verbose_name=' 8. Quand vous étiez enfant, est-ce que vous faisiez beaucoup de choses dans le but d’obtenir l’approbation des gens ?',

        widget=widgets.RadioSelectHorizontal,

    )

    SPSRQ_q9 = models.IntegerField(
        choices=C.CHOICES,

        # widget=widgets.Select,
        verbose_name='9. Donnez-vous généralement la préférence aux activités débouchant sur un gain immédiat ?',
        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q10 = models.IntegerField(
        choices=C.CHOICES,

        # widget=widgets.Select,
        verbose_name=' 10. Aimez-vous la compétition et faites-vous tout ce que vous pouvez pour gagner ?  ',
        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q11 = models.IntegerField(
        choices=C.CHOICES,

        # widget=widgets.Select,
        verbose_name='11. Pensez que vous pourriez faire plus de choses si vous n’étiez pas retenu(e) par un sentiment de peur ou d’insécurité ? ',
        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q12 = models.IntegerField(
        choices=C.CHOICES,

        # widget=widgets.Select,
        verbose_name='12. Etes-vous souvent inquiet(ète) des choses que vous avez dites ou faites ?    ',
        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q13 = models.IntegerField(
        choices=C.CHOICES,

        # widget=widgets.Select,
        verbose_name='13. Serait-il difficile pour vous de demander une augmentation de salaire à votre patron ?   ',
        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q14 = models.IntegerField(
        choices=C.CHOICES,

        # widget=widgets.Select,
        verbose_name=' 14. Essayez-vous généralement d’éviter de vous exprimer en public ?  ',
        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q15 = models.IntegerField(
        choices=C.CHOICES,

        # widget=widgets.Select,
        verbose_name='15. Par rapport  aux autres, diriez-vous que vous êtes  quelqu’un qui a peur de beaucoup de choses ? ',
        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q16 = models.IntegerField(
        choices=C.CHOICES,

        # widget=widgets.Select,
        verbose_name=' 16. Vous inquiétez-vous souvent au point que vos performances intellectuelles s’en trouvent diminuées ? ',
        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q17 = models.IntegerField(
        choices=C.CHOICES,

        # widget=widgets.Select,
        verbose_name='17. Vous abstenez-vous souvent de faire quelque chose que vous aimez pour ne pas être réprimandé(e) ou désapprouvé(e) par les autres ? ',
        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q18 = models.IntegerField(
        choices=C.CHOICES,

        # widget=widgets.Select,
        verbose_name='18. Aimez-vous ajouter des éléments compétitifs dans toutes vos activités ?  ',
        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q19 = models.IntegerField(
        choices=C.CHOICES,

        # widget=widgets.Select,
        verbose_name=' 19. Voudriez-vous être une personne socialement influente ?  ',
        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q20 = models.IntegerField(
        choices=C.CHOICES,

        # widget=widgets.Select,
        verbose_name=' 20. Vous abstenez-vous souvent de faire des choses par peur d’être embarrassé(e) ? ',
        widget=widgets.RadioSelectHorizontal,

    )
    SPSRQ_q21 = models.IntegerField(
        choices=C.CHOICES,

        # widget=widgets.Select,
        verbose_name='21. Aimez-vous prouver vos capacités physiques même si cela pourrait impliquer un danger ? ',
        widget=widgets.RadioSelectHorizontal,
    )
    questionnaire_q1 = models.FloatField(label="1- Quel âge avez-vous ?", min=18, max=99)
    questionnaire_q2 = models.IntegerField(
        verbose_name=' 2- Quel est le dernier diplôme que vous avez obtenu ?  ',
        widget=widgets.RadioSelect,
        choices=[[0, 'CAP/BEP'], [1,'Brevet des collèges'],[2,'Baccalauréat'], [3, 'DUT/BTS/DEUG'],[4,'Licence'],[5,'Master'],[6,'Doctorat'], [7,'Aucun']])
    questionnaire_q3 = models.IntegerField(
        verbose_name=' 3- Quelle catégorie décrit-elle le mieux votre situation actuelle ?  ',
        widget=widgets.RadioSelect,
        choices=[[0, 'Etudiant/Etudiante en L1'], [1, 'Etudiant/Etudiante en L2'], [2, 'Etudiant/Etudiante en L3'], [3, 'Etudiant/Etudiante en M1'], [4, 'Etudiant/Etudiante en M2'],
                 [5, 'Doctorant/Doctorante'], [6, 'En recherche d’emploi '], [7, 'Agriculteur exploitant /Agricultrice exploitante'], [8,"	Artisan/Artisane, commerçant/commerçante et chef/cheffe d’entreprise "], [9,'Cadre et profession intellectuelle supérieur'],[10,'Employé/Employée à temps plein'], [11,'Employé/Employée à temps partiel'], [12,'Auto-entrepreneur/auto-entrepreneuse'], [12, 'Ouvrier/Ouvrière '], [13,'Retraité/Retraitée'],[14,'Autre']])
    questionnaire_q4 = models.IntegerField(
        verbose_name=' 4- Quel est ou quel a été votre champ d’étude ?  ',
        widget=widgets.RadioSelect,
        choices=[[0, 'Sciences Humaines et Sociales (Sociologie, Economie, Gestion)'], [1, 'Langues'], [2, 'Art'],
                 [3, 'Droit'], [4, 'Sciences Naturelles (Biologie, Physique)'],
                 [5, 'Mathématiques et/ou Informatique'], [6, 'Santé (médecine, infirmier/infirmière, psychologie, etc.) '],
                 [7, 'Technologie/ Ingénerie'],
                 [8, "Autre "]])


def get_points(player):

    player.ind_payoff=player.participant.points_partie2 + player.participant.points_partie3+player.participant.points_partie4 + player.participant.points_partie5 + player.participant.points_beliefs1 + player.participant.points_beliefs2 + player.participant.points_beliefs3
    player.participant.ind_payoff=player.ind_payoff

def set_payoffs_fee(player):
    player.participant.payoff= player.participant.ind_payoff + 3
    player.participant.payoff_euros= player.participant.ind_payoff + 3

def set_payoffs(player):

    if player.participant.ind_payoff < 7:
        player.participant.payoff=7
        player.participant.payoff_euros=7
    else:
        player.participant.payoff = player.participant.ind_payoff
        player.participant.payoff_euros= player.participant.ind_payoff

class WaitforInstructions(WaitPage):
    pass

# PAGES
class Instructions(Page):
    form_model= 'player'

class Messages(Page):
    form_model = 'player'
    form_fields = ['Message1', 'Message2', 'Message3', 'Message4']

    @staticmethod
    def is_displayed(player: Player):
        return player.participant.nb_participants > 1


class BFNE(Page):
    form_model = 'player'
    form_fields = ['BFNE_q1', 'BFNE_q2', 'BFNE_q3', 'BFNE_q4', 'BFNE_q5','BFNE_q6','BFNE_q7','BFNE_q8','BFNE_q9','BFNE_q10','BFNE_q11','BFNE_q12']


class WaitforPart4(WaitPage):
    pass

class SPSRQ(Page):
    form_model = 'player'
    form_fields = ['SPSRQ_q1', 'SPSRQ_q2', 'SPSRQ_q3', 'SPSRQ_q4', 'SPSRQ_q5','SPSRQ_q6','SPSRQ_q7','SPSRQ_q8','SPSRQ_q9','SPSRQ_q10','SPSRQ_q11','SPSRQ_q12', 'SPSRQ_q13', 'SPSRQ_q14','SPSRQ_q15','SPSRQ_q16','SPSRQ_q17','SPSRQ_q18','SPSRQ_q19','SPSRQ_q20','SPSRQ_q21']

class WaitforQuestionnaireGenre(WaitPage):
    pass

class QuestionGenre(Page):
    form_model = 'player'
    form_fields = ['question_genre']





class Questionnaire_Instructions(Page):
    form_model = 'player'

class Questionnaire(Page):
    form_model = 'player'
    form_fields = ['questionnaire_q1', 'questionnaire_q2', 'questionnaire_q3', 'questionnaire_q4']

    def before_next_page(player, timeout_happened):
        get_points(player)
        set_payoffs_fee(player)




class WaitforEnd(WaitPage):
    after_all_players_arrive = set_payoffs


class Point(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.participant.nb_participants == 2 or player.participant.nb_participants == 4 or player.participant.nb_participants == 6 or player.participant.nb_participants == 8


class PointImpair(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.participant.nb_participants == 1 or player.participant.nb_participants == 3 or player.participant.nb_participants == 5 or player.participant.nb_participants == 7


page_sequence = [WaitforInstructions, Instructions, Messages, BFNE, SPSRQ,QuestionGenre, Questionnaire,Point, PointImpair]
#page_sequence = [ Questionnaire, WaitforEnd, Point]
