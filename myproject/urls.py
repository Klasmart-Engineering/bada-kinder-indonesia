"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path("", Login.as_view(), name="login"),
    path("main", Main.as_view(), name="main"),
    path("level/A", LevelA.as_view(), name="levelA"),
    path("book/1/A", Book_1A.as_view(), name="book_1A"),
    path("checkhomework", Checkhomework.as_view(), name="checkhomework"),
    path("board/notice", Board_Notice.as_view(), name="board_notice"),
    path("board/notice/4", Board_Notice4.as_view(), name="board_notice_4"),
    path("board/studyplan/34", Board_Studyplan34.as_view(), name="board_studyplan_34"),
    path("board/studyplan/40", Board_Studyplan40.as_view(), name="board_studyplan_40"),
    path("contents/nemies", Contents_Nemies.as_view(), name="contents_nemies"),
]
