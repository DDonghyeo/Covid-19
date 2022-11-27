import requests as requests
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home.html')


def covidapi(n):
    url = f"openapi.seoul.go.kr:8088/547171685163686f35324270474f6e/json/TbCorona19CountStatus/1/{n}/"
    API = requests.get(url).json()
    data = API[0][0]
    return data

def home(request):
    value = covidapi(1)[0]
    week = covidapi(7)
    week_data = []
    for data in week:
        week_data.append(data['S_DT'], data['N_MJ'])
    return(request, 'home.html',{'value':int(value),'week_data':int(week_data)})
