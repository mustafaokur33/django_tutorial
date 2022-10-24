from importlib.resources import path


from django.urls import path
from . import views

urlpatterns = [
    path("<int:month>", views.monthly_chalenge_by_number),

    path("<str:month>", views.monthly_challenge,name="month-challenge")
]
