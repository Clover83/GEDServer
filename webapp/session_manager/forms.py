from django import forms
from django.core.exceptions import ValidationError

from django.contrib.postgres.forms import SimpleArrayField

class LocationDataForm(forms.Form):
    session_key = forms.CharField(max_length=200)
    player_key = forms.CharField(max_length=100)
    time_list = SimpleArrayField(forms.CharField(max_length=20))
    loc_list = SimpleArrayField(forms.CharField(max_length=50))


    def clean_time_list(self):
        data = self.cleaned_data['time_list']
        for t in data:
            try:
                a = int(t)
            except:
                raise ValidationError("Time list contains non int value")
        if len(data) != len(self.cleaned_data['loc_list']):
            raise ValidationError("Length of time list and location list differ")
        return data

    def clean_loc_list(self):
        data = self.cleaned_data['loc_list']
        if len(data) != len(self.cleaned_data['time_list']):
            raise ValidationError("Length of time list and location list differ")
        return data


    



