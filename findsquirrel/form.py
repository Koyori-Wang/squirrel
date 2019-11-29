from django.forms import ModelForm
from .models import Squirrel
 
class SquirrelForm(ModelForm):
  class Meta:
    model = Squirrel
    fields = ['latitude', 'longitude', 'squirrel_id', 'shift', 'date', 'age', 'color', 'location', 'specific_location', 'running', 'chasing', 'climbing', 'eating', 'foraging', 'other_activities', 'kuks', 'quaas', 'moans', 'tail_flag', 'tail_twitches', 'approaches', 'indifferent', 'runs_from'] 
