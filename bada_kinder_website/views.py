import requests

from django.conf import settings
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from utils.models import Subscription

def get_pacakage_id(request):
    try:
        pacakage_id = Subscription.objects.get(user=request.user).package_id
        if not pacakage_id:
            pacakage_id = 0
    except ObjectDoesNotExist:
        pacakage_id = 0

    return pacakage_id

@login_required
def main(request):
    pacakage_id = get_pacakage_id(request)
    if not pacakage_id:
        return redirect('/tutorial-video')
    r = requests.get(
        f'{settings.CMS_BASE_URL}/api/levels?'
        f'populate=thumbnail&populate=vertical_cover&'
        f'populate=age_badge&sort[0]=ordering&',
        f'filters[package][id]={pacakage_id}',
        headers={'Authorization': f'bearer {settings.STRAPI_API_KEY}'}
    )
    data = r.json()['data']
    print(data)
    context = {'data': data}
    return render(request, 'main.html', context)


@login_required
def book_list(request, level_id):

    r = requests.get(
        f'{settings.CMS_BASE_URL}/api/books?'
        f'populate=level.thumbnail&populate=thumbnail&'
        f'filters[level][id]={level_id}',
        # params=url_params,
        headers={'Authorization': f'bearer {settings.STRAPI_API_KEY}'}
    )
    # data = r.json()['data']
    data = sorted(r.json()['data'], key=lambda d: d['attributes']['month_number'])
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
    # print(data)

    weeks = data['attributes']['weeks']
    print('week', weeks[0])
    ordered_weeks = sorted(weeks, key=lambda d: d['week_name']) 
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
    page = request.GET.get('page', 1)
    page = int(page)
    r = requests.get(
        f'{settings.CMS_BASE_URL}/api/video-tutorials?populate=thumbnail&populate=file'
        f'&pagination[pageSize]=8&pagination[page]={page}',
        headers={'Authorization': f'bearer {settings.STRAPI_API_KEY}'}
    )
    data = r.json()['data']
    meta = r.json()['meta']
    page_count = meta['pagination']['pageCount']
    page_range = range(1, page_count + 1)
    
    item_range = range(1, meta['pagination']['total'] + 1)
    item_list = list(item_range)

    paginator = Paginator(item_list, 8) # Show 8 contacts per page.
    page_obj = paginator.get_page(page)

    context = {
        'data': data, 
        'meta': meta, 
        'page_obj': page_obj,
        'page_range': page_range, 
        'page': page,
    }
    return render(request, 'tutorial_video.html', context)

@login_required
def tutorial_pdf(request):
    page = request.GET.get('page', 1)
    page = int(page)
    r = requests.get(
        f'{settings.CMS_BASE_URL}/api/pdf-tutorials?populate=thumbnail&populate=file'
        f'&pagination[pageSize]=8&pagination[page]={page}',
        headers={'Authorization': f'bearer {settings.STRAPI_API_KEY}'}
    )
    data = r.json()['data']
    meta = r.json()['meta']
    page_count = meta['pagination']['pageCount']
    page_range = range(1, page_count + 1)
    
    item_range = range(1, meta['pagination']['total'] + 1)
    item_list = list(item_range)

    paginator = Paginator(item_list, 8) # Show 8 contacts per page.
    page_obj = paginator.get_page(page)

    context = {
        'data': data, 
        'meta': meta, 
        'page_obj': page_obj,
        'page_range': page_range, 
        'page': page,
    }
    return render(request, 'tutorial_pdf.html', context)


@login_required
def rpp(request):
    pacakage_id = get_pacakage_id(request)
    page = request.GET.get('page', 1)
    page = int(page)
    r = requests.get(
        f'{settings.CMS_BASE_URL}/api/rpps?populate=thumbnail&populate=file&'
        f'filters[package][id]={pacakage_id}'
        f'&pagination[pageSize]=8&pagination[page]={page}',
        headers={'Authorization': f'bearer {settings.STRAPI_API_KEY}'}
    )
    data = r.json()['data']
    meta = r.json()['meta']
    page_count = meta['pagination']['pageCount']
    page_range = range(1, page_count + 1)
    
    item_range = range(1, meta['pagination']['total'] + 1)
    item_list = list(item_range)

    paginator = Paginator(item_list, 8) # Show 8 contacts per page.
    page_obj = paginator.get_page(page)

    context = {
        'data': data, 
        'meta': meta, 
        'page_obj': page_obj,
        'page_range': page_range, 
        'page': page,
    }
    return render(request, 'rpp.html', context)


@login_required
def activity_book(request):
    pacakage_id = get_pacakage_id(request)
    page = request.GET.get('page', 1)
    page = int(page)
    r = requests.get(
        f'{settings.CMS_BASE_URL}/api/activity-books?populate=thumbnail&populate=file&populate=level&'
        f'filters[package][id]={pacakage_id}'
        f'&pagination[pageSize]=8&pagination[page]={page}',
        headers={'Authorization': f'bearer {settings.STRAPI_API_KEY}'}
    )
    data = r.json()['data']
    meta = r.json()['meta']
    page_count = meta['pagination']['pageCount']
    page_range = range(1, page_count + 1)
    
    item_range = range(1, meta['pagination']['total'] + 1)
    item_list = list(item_range)

    paginator = Paginator(item_list, 8) # Show 8 contacts per page.
    page_obj = paginator.get_page(page)

    context = {
        'data': data, 
        'meta': meta, 
        'page_obj': page_obj,
        'page_range': page_range, 
        'page': page,
        'kind': 'activity'
    }
    return render(request, 'activity_book.html', context)


@login_required
def story_book(request):
    pacakage_id = get_pacakage_id(request)
    page = request.GET.get('page', 1)
    page = int(page)
    r = requests.get(
        f'{settings.CMS_BASE_URL}/api/story-books?populate=thumbnail&populate=file&populate=level&'
        f'filters[package][id]={pacakage_id}'
        f'&pagination[pageSize]=8&pagination[page]={page}',
        headers={'Authorization': f'bearer {settings.STRAPI_API_KEY}'}
    )
    data = r.json()['data']
    meta = r.json()['meta']
    page_count = meta['pagination']['pageCount']
    page_range = range(1, page_count + 1)
    
    item_range = range(1, meta['pagination']['total'] + 1)
    item_list = list(item_range)

    paginator = Paginator(item_list, 8) # Show 8 contacts per page.
    page_obj = paginator.get_page(page)

    context = {
        'data': data, 
        'meta': meta, 
        'page_obj': page_obj,
        'page_range': page_range, 
        'page': page,
        'kind': 'story'
    }
    return render(request, 'activity_book.html', context)

@login_required
def course_book(request):
    pacakage_id = get_pacakage_id(request)
    page = request.GET.get('page', 1)
    page = int(page)
    r = requests.get(
        f'{settings.CMS_BASE_URL}/api/course-books?populate=thumbnail&populate=file&populate=level&'
        f'filters[package][id]={pacakage_id}'
        f'&pagination[pageSize]=8&pagination[page]={page}',
        headers={'Authorization': f'bearer {settings.STRAPI_API_KEY}'}
    )
    data = r.json()['data']
    meta = r.json()['meta']
    page_count = meta['pagination']['pageCount']
    page_range = range(1, page_count + 1)
    
    item_range = range(1, meta['pagination']['total'] + 1)
    item_list = list(item_range)

    paginator = Paginator(item_list, 8) # Show 8 contacts per page.
    page_obj = paginator.get_page(page)

    context = {
        'data': data, 
        'meta': meta, 
        'page_obj': page_obj,
        'page_range': page_range, 
        'page': page,
        'kind': 'course'
    }
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
    



