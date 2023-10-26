from otree.api import *
import os


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'tables'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass

import numpy as np
from PIL import Image
import otree.settings
import matplotlib.pyplot as plt


def creating_m(player):
    session = player.session
    subsession = player.subsession
    np.random.seed(0)

    # Define the dimensions of the table
    rows, columns = 10, 10

    # Initialize a dictionary to store the counts of 0s for each table
    zeros_counts = {}

    # Generate and save 10 tables as images
    for i in range(22):
        # Generate a table of random 0s and 1s
        table = np.random.randint(2, size=(rows, columns))

        # Count the number of 0s in the table
        num_zeros = np.sum(table == 0)

        # Store the count in the dictionary with a unique key
        zeros_counts[f'TABLE{i + 1}'] = num_zeros

        # Create a figure and axis for the table
        fig, ax = plt.subplots()

        # Hide axis labels and ticks
        ax.axis('off')

        # Create a table with 0s and 1s displayed as text, without cell borders
        table_obj = ax.table(cellText=table, loc='center', cellLoc='center', edges='open', bbox=[0, 0, 1, 1])
        for key, cell in table_obj._cells.items():
            cell.set_text_props(fontsize=14)  # Adjust font size as needed
            if key[0] == 0 or key[1] == -1 or key[1] == columns:
                cell.set_facecolor('none')
                cell.set_edgecolor('none')
            else:
                cell.set_facecolor('white')

        # Save the table as an image
        image_filename = f'table_{i + 1}.png'
        static_path = otree.settings.STATIC_ROOT
        image_path = os.path.join(static_path, image_filename)
        plt.savefig(image_path, bbox_inches='tight')
        plt.close(fig)

    # Store the dictionary of zero counts in the session vars

    session.vars['zeros_counts'] = zeros_counts
    session.zeros_counts2 = zeros_counts




# PAGES
class MyPage(Page):
    def before_next_page(player, timeout_happened):
        creating_m(player)


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [MyPage, Results]
