from django.contrib import admin
from django.urls import path
import app.views as view

urlpatterns = [
    path('', view.Index),
    path('Result', view.Result),
]
