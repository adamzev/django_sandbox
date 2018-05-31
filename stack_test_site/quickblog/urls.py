from django.urls import path

from . import views

app_name = 'quickblog'
urlpatterns = [
    path('', views.category_dropdown, name='category_dropdown'),
    path('page2', views.page2, name='page2'),

]