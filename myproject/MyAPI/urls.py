from django.urls import path
from . import views

urlpatterns = [
    path("api/", views.CustomersListCreate.as_view(), name="api"),
    path("api/<int:pk>/", views.CustomersRetrieveUpdateDestroy.as_view(), name="update"),
    path("", views.formProcessing, name='form'),
]