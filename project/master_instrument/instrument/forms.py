from django import forms
from .models import master


class masterform(forms.ModelForm):

    class Meta:
        model = master
        fields = ('mastername','make','model','rng','leastcount','uncertainity','idno','srno','calibrationdate','calibrationduedate','lab','certificateno')
        labels = {
            'mastername':'Master Name',
            'make': 'Make',
            'model': 'Model',
            'rng': 'Range',
            'leastcount': 'Least Count',
            'uncertainity': 'Uncertainity',
            'idno': 'Id no',
            'srno': 'Sr no',
            'calibrationdate': 'Calibration Date',
            'calibrationduedate': 'Calibration Due Date',
            'lab': 'Lab',
            'certificateno': 'Certificate No'
            
        }

    def __init__(self, *args, **kwargs):
        super(masterform,self).__init__(*args, **kwargs)
        self.fields['lab'].empty_label = "Select"
      