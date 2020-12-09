from django.shortcuts import render, redirect
from datetime import datetime

# Create your views here.
def index(request):
    if "favorite_color" in request.session:
        favorite_color = request.session["favorite_color"]
    else:
        favorite_color = "white"
        request.session["activities"] = []

    context = {
        "fav_color": favorite_color,
        "activities": request.session["activities"]
    }

    return render(request, "index.html", context)

def process_form(request):
    if request.method != "POST":
        return redirect("/")

    request.session["favorite_color"] = request.POST["color"]

    request.session["activities"].append({
        "color": request.POST["color"],
        "time": str(datetime.now())
    })

    return redirect("/")