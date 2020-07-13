from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    form_model = 'player'
    form_fields = [
        'are_you_ok',
        'treatment_rate']

    def js_vars(self):
        return dict(chosen_rate = self.player.treatment_rate,)


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [MyPage, ResultsWaitPage, Results]
