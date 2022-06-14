import requests

from django.conf import settings
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import TemplateView


@login_required
def main(request):
    r = requests.get(
        f'{settings.CMS_BASE_URL}/api/levels?'
        f'populate=thumbnail&populate=vertical_cover&'
        f'populate=age_badge&sort[0]=ordering',
        headers={'Authorization': f'bearer {settings.STRAPI_API_KEY}'}
    )
    data = r.json()['data']
    print(data)
    context = {'data': data}
    return render(request, 'main.html', context)


@login_required
def book_list(request, level_id):
    
    # url_params = {
    #     "populate": "level.thumbnail",
    #     "filters[level][id]": level_id
    # }
    r = requests.get(
        f'{settings.CMS_BASE_URL}/api/books?'
        f'populate=level.thumbnail&populate=thumbnail&'
        f'filters[level][id]={level_id}',
        # params=url_params,
        headers={'Authorization': f'bearer {settings.STRAPI_API_KEY}'}
    )
    # data = r.json()['data']
    data = sorted(r.json()['data'], key=lambda d: d['attributes']['book_number'])
    print(data)
    context = {'data': data}
    return render(request, 'book_list.html', context)


@login_required
def book_detail(request, book_id):
    
    r = requests.get(
        f'{settings.CMS_BASE_URL}/api/books/{book_id}?'
        f'populate=weeks.days.videos&populate=weeks.week_detail&'
        f'populate=weeks.week_detail.thumbnail&'
        f'populate=weeks.days.day.thumbnail&populate=weeks.thumbnail&populate=level',
        headers={'Authorization': f'bearer {settings.STRAPI_API_KEY}'}
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

class Checkhomework(TemplateView):
    template_name = "checkhomework.html"

class Main(LoginRequiredMixin, TemplateView):
    template_name = "main.html"

@login_required
def tutorial_video(request):
    r = requests.get(
        f'{settings.CMS_BASE_URL}/api/video-tutorials?populate=thumbnail&populate=file',
        headers={'Authorization': f'bearer {settings.STRAPI_API_KEY}'}
    )
    data = r.json()['data']
    print(data)
    context = {'data': data}
    return render(request, 'tutorial_video.html', context)

@login_required
def tutorial_pdf(request):
    r = requests.get(
        f'{settings.CMS_BASE_URL}/api/pdf-tutorials?populate=thumbnail&populate=file',
        headers={'Authorization': f'bearer {settings.STRAPI_API_KEY}'}
    )
    data = r.json()['data']
    print(data)
    context = {'data': data}
    return render(request, 'tutorial_pdf.html', context)


@login_required
def rpp(request):
    r = requests.get(
        f'{settings.CMS_BASE_URL}/api/rpps?populate=thumbnail&populate=file',
        headers={'Authorization': f'bearer {settings.STRAPI_API_KEY}'}
    )
    data = r.json()['data']
    print(data)
    context = {'data': data}
    return render(request, 'rpp.html', context)


@login_required
def activity_book(request):
    r = requests.get(
        f'{settings.CMS_BASE_URL}/api/activity-books?populate=thumbnail&populate=file',
        headers={'Authorization': f'bearer {settings.STRAPI_API_KEY}'}
    )
    data = r.json()['data']
    print(data)
    context = {'data': data, 'kind': 'activity'}
    return render(request, 'activity_book.html', context)


@login_required
def story_book(request):
    r = requests.get(
        f'{settings.CMS_BASE_URL}/api/activity-books?populate=thumbnail&populate=file',
        headers={'Authorization': f'bearer {settings.STRAPI_API_KEY}'}
    )
    data = r.json()['data']
    print(data)
    context = {'data': data, 'kind': 'story'}
    return render(request, 'activity_book.html', context)

@login_required
def course_book(request):
    r = requests.get(
        f'{settings.CMS_BASE_URL}/api/activity-books?populate=thumbnail&populate=file',
        headers={'Authorization': f'bearer {settings.STRAPI_API_KEY}'}
    )
    data = r.json()['data']
    print(data)
    context = {'data': data, 'kind': 'course'}
    return render(request, 'activity_book.html', context)


@login_required
def tutorial_pdf_detail(request):
    r = requests.get(
        f'{settings.CMS_BASE_URL}/api/levels?populate=thumbnail&'
        f'populate=vertical_cover&populate=age_badge&sort[0]=ordering',
        headers={'Authorization': f'bearer {settings.STRAPI_API_KEY}'}
    )
    data = r.json()['data']
    print(data)
    context = {'data': data}
    return render(request, 'tutorial_pdf_detail.html', context)


class LevelA(TemplateView):
    template_name = "level/A/index.html"

class Book_1A(TemplateView):
    template_name = "level/A/1.html"

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
    



