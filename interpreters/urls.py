from django.urls import path
from . import views

urlpatterns = [
    path('interpreter/', views.InterpreterView.as_view()),
]
