from django.urls import path
from . import views

app_name = 'notes'

urlpatterns = [
    path('', views.notes_view, name='notes'),
    path('toggle-theme/', views.toggle_theme, name='toggle_theme'),
]