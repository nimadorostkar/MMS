from django.urls import path, re_path
from app import views

app_name='app'



urlpatterns = [
    # The home page
    path('', views.index, name='index'),
    # other
    path('profile', views.profile, name='profile'),
    path('search',views.search,name='search'),
    ]
