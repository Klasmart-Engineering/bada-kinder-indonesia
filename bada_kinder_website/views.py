from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin


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
    



