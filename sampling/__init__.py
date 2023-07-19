import random

from otree.api import *
import numpy as np


author = 'Zahra Rahmani'
doc = """
Sampling Paradigma
"""

class C(BaseConstants):
    NAME_IN_URL = 'SAMPLING'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 10


class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    boxChoice = models.StringField( choices = ['i', 'm'])
    range_agree = models.IntegerField( min=-100, max=100)
    range_likelyTrue = models.IntegerField( min=-100, max=100)
    range_ccconcern = models.IntegerField( min=-100, max=100)
    statementText =models.StringField()
    statementID =models.StringField()
    


def creating_session(subsession:Subsession):
    for player in subsession.get_players():
        if subsession.round_number == 1: 
            player.participant.randomInfoArray = random.sample(range(1,147),C.NUM_ROUNDS)
            player.participant.randomMisinfoArray = random.sample(range(1,79),C.NUM_ROUNDS)


# ---------------------------------------------------------------
# ------------------- PAGES--------------------------------------
#----------------------------------------------------------------


class sampling(Page):
    form_model = 'player'
    form_fields = ['boxChoice']
    @staticmethod
    def vars_for_template(player: Player):
        round_number = player.round_number
        return {
            'round_number': round_number
            }
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        print('maybe I should draw the text here')


class statement(Page):
    form_model = 'player'
    #form_fields = ['statementText', 'statementID', ]
    form_fields = ['range_ccconcern', 'range_agree', 'range_likelyTrue','statementText', 'statementID']
    def vars_for_template(player: Player):
        round_number = player.round_number
        return {
            'round_number': round_number,
            'randomInfo': player.participant.randomInfoArray[round_number-1],
            'randomMisinfo': player.participant.randomMisinfoArray[round_number-1],
            'boxChoice' : player.boxChoice
            }
    
page_sequence = [
    #betweenGames,
    sampling,
    statement
]