import requests
from django.shortcuts import render


def houses_list(request):
    response = requests.get(f"https://wizard-world-api.herokuapp.com/houses")
    houses = response.json() if response.status_code == 200 else []

    return render(request, "houses/list.html", {"houses": houses})


def house_detail(request, house_id):
    response = requests.get(f"https://wizard-world-api.herokuapp.com/houses/{house_id}")
    house = response.json() if response.status_code == 200 else None

    return render(request, "houses/detail.html", {"house": house})




