from django import forms

class CustomersForm(forms.Form):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    age_group = forms.ChoiceField(choices=(("Elderly", "Elderly"), ("Middle Aged", "Middle Age"), ("Young Adult", "Young Adult")))
    campaign_contacts = forms.IntegerField()
    contact_duration = forms.IntegerField()
    contact_type = forms.ChoiceField(choices=(("cellular", "cellular"), ("unknown", "unknown"), ("telephone", "telephone")))
    days_last_contacted = forms.IntegerField()
    personal_loan = forms.ChoiceField(choices=(("yes", "yes"), ("no", "no")))
    poutcome = forms.ChoiceField(choices=(("success", "succes"), ("unknown", "unknown"), ("failure", "failure"), ("other", "other")))