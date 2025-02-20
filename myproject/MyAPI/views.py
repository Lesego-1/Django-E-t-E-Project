from django.shortcuts import render
from rest_framework import generics, status
from .models import Customers
from .serializers import CustomersSerializer
from rest_framework.response import Response
import joblib
import pandas as pd
import os
from django.conf import settings
from .forms import CustomersForm

# Create your views here.
class CustomersListCreate(generics.ListCreateAPIView):
    queryset = Customers.objects.all()
    serializer_class = CustomersSerializer
    
    def delete(self, request, *args, **kwargs):
        Customers.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class CustomersRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customers.objects.all()
    serializer_class = CustomersSerializer
    lookup_field = 'pk'
    
def oneHotEncode(df: pd.DataFrame):
    features_path = os.path.join(settings.BASE_DIR, 'MyAPI', 'pickled_objects', 'features.pkl')
    
    features = joblib.load(features_path)  # Load features
    categorical_cols = ['age_group', 'contact_type', 'personal_loan', 'poutcome']
    df_processed = pd.get_dummies(df, columns=categorical_cols, drop_first=False)  # One Hot Encode Input Data
    
    # Assign 0 to columns with no returned values
    new_dict = {}
    for col in features:
        if col in df_processed.columns:
            new_dict[col] = df_processed[col].values
        else:
            new_dict[col] = 0
            
    result = pd.DataFrame(new_dict)
    result.replace({True:1, False:0})

    return result

def predictions(df: pd.DataFrame):
    # Load ML Model
    model_path = os.path.join(settings.BASE_DIR, 'MyAPI', 'pickled_objects', 'rf_model.pkl')  
    model = joblib.load(model_path)
    
    # Predict the input data
    y_pred = model.predict(df)
    
    return "Yes" if y_pred == 1 else "No"

def formProcessing(request):
    if request.method == "POST":
        form = CustomersForm(request.POST)
        if form.is_valid():
            # Get form values
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            age_group = form.cleaned_data['age_group']
            campaign_contacts = form.cleaned_data['campaign_contacts']
            contact_duration = form.cleaned_data['contact_duration']
            contact_type = form.cleaned_data['contact_type']
            days_last_contacted = form.cleaned_data['days_last_contacted']
            personal_loan = form.cleaned_data['personal_loan']
            poutcome = form.cleaned_data['poutcome']
            
            # Transform input data into DataFrame
            myDict = (request.POST).dict()
            columns = ["first_name", "last_name", "age_group", "campaign_contacts", "contact_duration", "contact_type", "days_last_contacted", "personal_loan", "poutcome"]
            df = pd.DataFrame(myDict, index=[0])
            df.drop(columns=['first_name', 'last_name'], axis=1, inplace=True)  # Drop columns that are not features in the model
            
            # Get the predictions
            result = predictions(oneHotEncode(df))
            
            # Store the data in the database
            Customers.objects.create(
                first_name = first_name,
                last_name = last_name,
                age_group = age_group,
                campaign_contacts = campaign_contacts,
                contact_duration = contact_duration,
                contact_type = contact_type,
                days_last_contacted = days_last_contacted,
                personal_loan = personal_loan,
                poutcome = poutcome,
                classification = result
            )
            
            return render(request, "result.html", {"result" : result})
        
    form = CustomersForm()
    
    return render(request, "index.html", {'form':form})