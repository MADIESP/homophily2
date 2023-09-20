from otree.api import *


class Constants(BaseConstants):
    name_in_url = 'Survey'
    players_per_group = 2
    num_rounds = 2




class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    strategy = models.LongStringField(
        label="  Which strategy did you set up with your partner to most efficiently complete the game?")

    gender = models.IntegerField(label="What gender do you identify with?", widget=widgets.RadioSelectHorizontal,
                                 choices=[[0, "Female"], [1, "Male"], [2, "Other"]])
    rank1st = models.IntegerField(
        choices=[[1, ' A'],
            [2, 'B'],
            [3, '  C'],
            [4, ' D'],],
       # widget=widgets.Select,
        verbose_name='<b>Rank 1st:</b>',
        widget=widgets.RadioSelectHorizontal,

    )

    rank2nd = models.IntegerField(
        choices=[[1, 'A'],
                 [2, 'B'],
                 [3, ' C'],
                 [4, ' D'], ],
        # widget=widgets.Select,
        verbose_name='<b>Rank 2nd: </b>',
        widget=widgets.RadioSelectHorizontal,

    )

    rank3rd = models.IntegerField(
        choices=[[1, ' A'],
                 [2, 'B'],
                 [3, ' C'],
                 [4, ' D'], ],
        # widget=widgets.Select,
        verbose_name='<b>Rank 3rd: </b>',
        widget=widgets.RadioSelectHorizontal,

    )

    rank4th = models.IntegerField(
        choices=[[1, ' A'],
                 [2, 'B'],
                 [3, ' C'],
                 [4, ' D'], ],
        # widget=widgets.Select,
        verbose_name='<b>Rank 4th: </b>',
        widget=widgets.RadioSelectHorizontal,

    )






class WaitCounting(WaitPage):
   # wait_for_all_groups = True
    body_text = "Please wait for your partner to finish."

class Survey(Page):
    form_model = 'player'
    form_fields = [ 'rank1st', 'rank2nd','rank3rd','rank4th']

    def vars_for_template(player: Player):
        if  player.round_number == 1:
            return {
                image_path = '_static/global/9.jpg',
            }
        elif  player.round_number == 2:
            return {
                image_path = '_static/global/test.jpg',
            }








page_sequence = [WaitCounting, Survey]








