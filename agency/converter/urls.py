from django.urls import path

from .views import *


urlpatterns = [
    path('rates', ConvertView.as_view()),
]