from django.shortcuts import render
from .forms import ClassificationForm
import joblib
import pandas as pd

# Create your views here.
def index(request):
    if request.method == "POST":
        form = ClassificationForm(request.POST)
        if form.is_valid():
            # Extract data and format it for the model
            input_data = pd.DataFrame([form.cleaned_data])
            
            # Load the model
            model = joblib.load(r"myproject\myapp\ml_models\rf_model.pkl")
            
            prediction = model.predict(input_data)[0]
            result = "Yes" if prediction == 1 else "No"
            
            return render(request, "result.html", {"result": result})
    else:
        form = ClassificationForm()
    return render(request, 'index.html', {"form":form})