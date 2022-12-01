from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.template.loader import render_to_string

monthly_challenges = {
    "january": "Trinke mehr Wasser ",
    "february": "Keine unnötigen Einkäufe.",
    "march": "Nimm die Stufen, verzichte auf den Lift.",
    "april": "Mache jeden Tag X Liegestützen",
    "may": "Verzichte auf dein Auto",
    "june": "Lerne eine neue Fremdsprache",
    "july": "Verzichte auf Kaffee und / oder Koffein",
    "august": "Verwende keine elektronischen Geräte im Bett.",
    "september": "Lese keine Nachrichten",
    "october": "Lerne Programmieren",
    "november": "Verzichte auf Zucker",
    "december": None,
}


# Create your views here.
def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_challenge_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
    redirect_path = reverse("monthly-challenge", args=[redirect_month])  # e.g. /challenge/january
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month": month.capitalize()
        })
    except Exception as e:
        raise Http404(e)
        # response_data = render_to_string("404.html")
        # return HttpResponseNotFound(response_data)
