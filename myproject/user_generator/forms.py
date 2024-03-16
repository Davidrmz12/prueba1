from django import forms

class MassUserCreationForm(forms.Form):
    num_users = forms.IntegerField(min_value=1, max_value=100)
