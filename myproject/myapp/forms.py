from django import forms

class ClassificationForm(forms.Form):
    contact_duration = forms.IntegerField(
        label="Last contact duration in seconds",
        required=True,
        min_value=0,
        widget=forms.TextInput(attrs={"placeholder": "Enter the last contact duration in seconds:"})
    )
    annual_balance = forms.IntegerField(
        label="Annual Balance",
        required=True,
        min_value=0,
        widget=forms.TextInput(attrs={"placeholder": "Enter your annual balance:"})
    )
    age = forms.IntegerField(
        label="Your Age",
        required=True,
        min_value=0,
        max_value=120,
        widget=forms.TextInput(attrs={"placeholder": "Enter your age:"})
    )
    contact_day = forms.IntegerField(
        label="Last contact day",
        required=True,
        widget=forms.TextInput(attrs={"placeholder":"Enter the last contact day of the month:"})
    )
    outcome_choices = [
        (1, 'Yes'),
        (0, 'No')
    ]
    poutcome = forms.ChoiceField(
        label="Previous outcome",
        required=True,
        choices=outcome_choices,
        widget=forms.RadioSelect
    )