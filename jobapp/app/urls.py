
from django.http import HttpResponse
from django.contrib import admin
from django.urls import path
from app import views


urlpatterns = [
    path('', views.job_list, name="jobs_home"),
    # path('', views.job_list, name="jobs_home"),
    path('hello/', views.hello, name='hello'),
    path('job/<int:id>', views.jobDetails, name='jobs_detail')
]
