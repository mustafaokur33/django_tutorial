from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

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
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported!")
