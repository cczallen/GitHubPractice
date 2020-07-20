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

class Treatment( object ):
    def get_treatment( player ):
        participant = player.participant
        if Constants.key_method not in participant.vars:
            participant.vars[ Constants.key_method ] = random.choice(['fast', 'normal', 'slow'])
            
        method = participant.vars[ Constants.key_method ]
        return method

class OptionOfSpeed( object ):
    def option( string ):
        if string == 'slow':
            return 0.7
        if string == 'fast':
            return 0.9
        else:
            return 0.8

class Constants(BaseConstants):
    name_in_url = 'testing1'
    players_per_group = None
    num_rounds = 1
    key_method = 'treatment_method'


class Subsession(BaseSubsession):
    def creating_session( self ):
        for p in self.get_players():
            p.treatment_method = Treatment.get_treatment(p)
            p.treatment = OptionOfSpeed.option( p.treatment_method )


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    are_you_ok = models.BooleanField(
            label = '你今天好嗎？',
            choices = [
                [True, '很好'],
                [False, '還好']
            ],
            widget=widgets.RadioSelect,
        )
    
    treatment_method = models.StringField()
    treatment = models.FloatField()
    # these are duplicated columns, need to find solutions

        
