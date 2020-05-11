from django import forms
from .models import inservice
from .models import test


class inserviceform(forms.ModelForm):

    class Meta:
        model = inservice
        fields = ('eqname','make1','srno1','referancename','make2','srno2')
        labels = {
            'eqname':'Inservice Verification For Equipment',
            'make1':'Make',
            'srno1': 'Sr No',
            'referancename': 'Referance Standard/Artifact',
            'make2': 'Make',
            'srno2': 'Sr No'
        }

    def __init__(self, *args, **kwargs):
        super(inserviceform,self).__init__(*args, **kwargs)
        self.fields['eqname'].empty_label = "Select"
        self.fields['referancename'].empty_label = "Select"
        


class testform(forms.ModelForm):

    class Meta:
        model = test
        fields = ('testpoint','deviation1','deviation2','difference','uncertainity','remark')
        labels = {
            'testpoint':'Test Point',
            'deviation1':'Deviation(E1)',
            'deviation2': 'Deviation(E2)',
            'difference': '(E2-E1)',
            'uncertainity': 'Uncertainity',
            'remark': 'Remark'
        }
