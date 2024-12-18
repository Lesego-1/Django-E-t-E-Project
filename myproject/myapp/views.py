from django.shortcuts import render
from .forms import ClassificationForm
import joblib
import pandas as pd
from django.conf import settings
import os

# Create your views here.
def index(request):
    if request.method == "POST":
        form = ClassificationForm(request.POST)
        if form.is_valid():
            # Define paths to the model and scaler
            model_path = os.path.join(settings.BASE_DIR, 'myapp', 'ml_models', 'rf_model.pkl')
            scaler_path = os.path.join(settings.BASE_DIR, 'myapp', 'ml_models', 'scaler.pkl')
            
            # Extract data and format it for the model
            input_data = pd.DataFrame([form.cleaned_data.values()])
            print(input_data)
            # Load the model
            model = joblib.load(model_path)
            
            # Load the scaler
            scaler = joblib.load(scaler_path)
            
            # Scale the input values
            input_scaled = scaler.transform(input_data)
            
            # Predict if user will subscribe to a term deposit
            prediction = model.predict(input_scaled)
            result = "Yes" if prediction == 1 else "No"
            
            return render(request, "result.html", {"result": result})
    else:
        form = ClassificationForm()
    return render(request, 'index.html', {"form":form})