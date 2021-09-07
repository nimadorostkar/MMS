from django.urls import path, re_path
from app import views

app_name='app'



urlpatterns = [
    # Matches any html file
    re_path(r'^.*\.html', views.pages, name='pages'),
    # The home page
    path('', views.index, name='index'),
    # other
    path('profile', views.profile, name='profile'),
    path('search',views.search,name='search'),
    ]
