from django import forms

class ClassificationForm(forms.Form):
    contact_duration = forms.IntegerField(
        label="Last contact duration in seconds",
        required=True,
        min_value=0,
        widget=forms.TextInput(attrs={"placeholder": "Enter the last contact duration in seconds:"})
    )
    age = forms.IntegerField(
        label="Your Age",
        required=True,
        min_value=0,
        max_value=120,
        widget=forms.TextInput(attrs={"placeholder": "Enter your age:"})
    )
    outcome_choices = [
        (1, 'Yes'),
        (0, 'No')
    ]
    housing_loan = forms.ChoiceField(
        label="Do you have a housing loan?",
        required=True,
        choices=outcome_choices,
        widget=forms.RadioSelect
    )
    annual_balance = forms.IntegerField(
        label="Annual Balance",
        required=True,
        min_value=0,
        widget=forms.TextInput(attrs={"placeholder": "Enter your annual balance:"})
    )
    contact_day = forms.IntegerField(
        label="Last contact day",
        required=True,
        widget=forms.TextInput(attrs={"placeholder":"Enter the last contact day of the month:"})
    )