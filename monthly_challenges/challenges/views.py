from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


monthly_challenges = {

    "january": "Eat no meat for the entire month.",
    "february": "Walk at least 20 minute every day.",
    "march": "Learn django for t least 20 minutes every day.",
    "april": "Eat no meat for the entire month.",
    "may": "Walk at least 20 minute every day.",
    "june": "Learn django for t least 20 minutes every day.",
    "july": "Eat no meat for the entire month.",
    "august": "Walk at least 20 minute every day.",
    "september": "Learn django for t least 20 minutes every day.",
    "october": "Eat no meat for the entire month.",
    "november": "Walk at least 20 minute every day.",
    "december": "Learn django for t least 20 minutes every day."

}
# Create your views here.

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
    
    response_data = f"<h1><ul>{list_items}</ul></h1>"

    return HttpResponse(response_data)


def monthly_chalenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid Month")

    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")
