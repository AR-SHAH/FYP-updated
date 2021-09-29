
from django.urls import path
from mainApp import views
urlpatterns = [
    path('', views.DetailView.as_view()),
    path('create/', views.CreateView.as_view()),
    path('read/', views.ReadView.as_view())
]
