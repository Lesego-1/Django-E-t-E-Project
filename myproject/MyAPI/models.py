from django.db import models

# Create your models here.
class Customers(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age_group = models.CharField(max_length=20, choices=(("Elderly", "Elderly"), ("Middle Aged", "Middle Age"), ("Young Adult", "Young Adult")))
    campaign_contacts = models.IntegerField()
    contact_duration = models.IntegerField()
    contact_type = models.CharField(max_length=20, choices=(("cellular", "cellular"), ("unknown", "unknown"), ("telephone", "telephone")))
    days_last_contacted = models.IntegerField()
    personal_loan = models.CharField(max_length=20, choices=(("yes", "yes"), ("no", "no")))
    poutcome = models.CharField(max_length=20, choices=(("success", "succes"), ("unknown", "unknown"), ("failure", "failure"), ("other", "other")))
    classification = models.CharField(max_length=20, default=None)
    published_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.first_name