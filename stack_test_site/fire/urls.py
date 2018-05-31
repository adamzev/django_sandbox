from django.urls import path

from . import views

app_name = 'fire'
urlpatterns = [
    path('', views.status, name='status'),
    path('<int:firefighter_id>/', views.details, name='detail'),
    path('members/', views.members, name='members'),
]