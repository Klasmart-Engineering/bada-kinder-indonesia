"""bada_kinder_website URL Configuration

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
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),  
    path("", views.Login.as_view(redirect_authenticated_user=True), name="login"),
    path("main", views.main, name="main"),
    path("level/<int:level_id>/", views.book_list, name="book_list"),
    path("book/<int:book_id>/", views.book_detail, name="book_detail"),
    path("book/1/A", views.Book_1A.as_view(), name="book_1A"),
    path("tutorial-pdf", views.tutorial_pdf, name="tutorial_pdf"),
    path("tutorial-video", views.tutorial_video, name="tutorial_video"),
    # path("book/1/A", Book_1A.as_view(), name="book_1A"),
    path("checkhomework", views.Checkhomework.as_view(), name="checkhomework"),
    path("board/notice", views.Board_Notice.as_view(), name="board_notice"),
    path("board/notice/4", views.Board_Notice4.as_view(), name="board_notice_4"),
    path("board/studyplan/34", views.Board_Studyplan34.as_view(), name="board_studyplan_34"),
    path("board/studyplan/40", views.Board_Studyplan40.as_view(), name="board_studyplan_40"),
    path("contents/nemies", views.Contents_Nemies.as_view(), name="contents_nemies"),
]
