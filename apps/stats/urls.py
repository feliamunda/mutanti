from django.urls import path

from .views import *

from . import views

app_name = 'stats'

urlpatterns = [
    path('', views.HumanStatsView.as_view(),name='human_stats'),
]