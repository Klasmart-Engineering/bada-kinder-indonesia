from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

import requests
from django.shortcuts import render


def main(request):
    CMS_BASE_URL = 'http://localhost:1337'
    r = requests.get(
        f'{CMS_BASE_URL}/api/levels?populate=thumbnail&populate=vertical_cover&populate=age_badge'
    )
    data = r.json()['data']
    print(data)
    context = {'data': data}
    return render(request, 'main.html', context)


def book_list(request, level_id):
    # http://localhost:1337/api/books?populate=thumbnail&filter[level][id]=1
    CMS_BASE_URL = 'http://localhost:1337'
    url_params = {
        "populate": "thumbnail",
        "filters[level][id]": level_id
    }
    r = requests.get(
        f'{CMS_BASE_URL}/api/books',
        params=url_params
    )
    data = r.json()['data']
    print(data)
    context = {'data': data}
    return render(request, 'book_list.html', context)


def book_detail(request, book_id):
    # http://localhost:1337/api/books/1?populate=week.days.videos&populate=week.days.thumbnail&populate=week.thumbnail&populate=level
    CMS_BASE_URL = 'http://localhost:1337'
    
    r = requests.get(
        f'{CMS_BASE_URL}/api/books/{book_id}?populate=weeks.days.videos&populate=weeks.week_detail&populate=weeks.week_detail.thumbnail&populate=weeks.days.day.thumbnail&populate=weeks.thumbnail&populate=level',
    )
    data = r.json()['data']
    print(data)

    weeks = data['attributes']['weeks']
    ordered_weeks = sorted(weeks, key=lambda d: d['week_detail']['data']['attributes']['ordering']) 
    week_1 = sorted(ordered_weeks[0]['days'], key=lambda d: d['day']['data']['attributes']['ordering'])
    week_2 = sorted(ordered_weeks[1]['days'], key=lambda d: d['day']['data']['attributes']['ordering'])
    week_3 = sorted(ordered_weeks[2]['days'], key=lambda d: d['day']['data']['attributes']['ordering'])
    week_4 = sorted(ordered_weeks[3]['days'], key=lambda d: d['day']['data']['attributes']['ordering'])

    ordered_weeks = [week_1, week_2, week_3, week_4]

    
    context = dict(
        data=data,
        week_1=week_1, 
        week_2=week_2, 
        week_3=week_3, 
        week_4=week_4,
        ordered_weeks=ordered_weeks
    )
    return render(request, 'book_detail.html', context)


class Login(LoginView):
    template_name = 'login.html'

class Main(LoginRequiredMixin, TemplateView):
    template_name = "main.html"

class LevelA(TemplateView):
    template_name = "level/A/index.html"

class Book_1A(TemplateView):
    template_name = "level/A/1.html"

class Checkhomework(TemplateView):
    template_name = "checkhomework.html"

class Board_Notice(TemplateView):
    template_name = "board/notice/index.html"

class Board_Notice4(TemplateView):
    template_name = "board/notice/4.html"

class Board_Studyplan40(TemplateView):
    template_name = "board/studyplan/40.html"

class Board_Studyplan34(TemplateView):
    template_name = "board/studyplan/34.html"

class Contents_Nemies(TemplateView):
    template_name = "contents/nemies.html"
    



