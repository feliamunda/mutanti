from django.urls import path

from .views import *

from . import views

app_name = 'mutants'

urlpatterns = [
    path('', views.HumanView.as_view(),name='human_list'),
]