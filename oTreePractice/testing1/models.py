from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
import random

author = 'Your name here'

doc = """
Your app description
"""

class Treatment(object):

   #def get_treatment(player):
        #participant = player.participant
        #if Constants.key_rate not in participant.vars:
            #participant.vars[Constants.key_rate] = random.choice([0.7, 0.8, 0.9])

        #rate = participant.vars[Constants.key_rate]
        #return rate（選擇二）
    pass
    
  

class Constants(BaseConstants):
    name_in_url = 'testing1'
    players_per_group = None
    num_rounds = 1
    key_rate = 'treatment_rate' 

class Subsession(BaseSubsession):
   def creating_session(self):
        for p in self.get_players():
            p.treatment_rate = random.choice([0.7, 0.8, 0.9])


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    treatment_rate = models.FloatField()
    are_you_ok = models.BooleanField(
            label = '你今天好嗎？',
            choices = [
                [True, '很好'],
                [False, '還好']
            ],
            widget=widgets.RadioSelect,
        )
    
