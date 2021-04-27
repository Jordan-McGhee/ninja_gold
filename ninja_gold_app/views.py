from django.shortcuts import render, redirect, HttpResponse
import random
from datetime import datetime
# Create your views here.

places = {
    "farm": (10,20),
    "cave": (5,10),
    "house": (2,5),
    "casino": (-50,50)
}

def index(request):
    if not "gold" in request.session or not "activities" in request.session:
        request.session['gold'] = 0
        request.session['activities'] = []

    return render(request, "index.html")

def reset(request):
    request.session.flush()
    return redirect("/")


def process_gold(request):
    if request.method == "GET":
        return redirect("/")

    building = request.POST['location']

    building_values = places[building]

    gold_earned = random.randint(building_values[0], building_values[1])

    time_now = datetime.now().strftime("%m/%d/%Y %I:%M%p")

    message = f"Earned {gold_earned} from the {building}! {time_now}"

    if building == "casino" and gold_earned < 0:
        message = f"Lost {gold_earned} from the {building}... {time_now}"

    request.session['gold'] += gold_earned
    request.session['activities'].append(message)

    return redirect("/")
