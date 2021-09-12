from django.urls import path, re_path
from app import views

app_name='app'



urlpatterns = [
    # The home page
    path('', views.index, name='index'),

    # Molds
    path('mold', views.mold, name='mold'),
    path('mold_detail/<int:id>/',views.mold_detail,name='mold_detail'),

    # Category
    path('category', views.category, name='category'),
    path('category_detail/<int:id>/',views.category_detail,name='category_detail'),

    # Manufacturer
    path('manufacturer', views.manufacturer, name='manufacturer'),
    path('manufacturer_detail/<int:id>/',views.manufacturer_detail,name='manufacturer_detail'),

    # Product
    path('product', views.product, name='product'),
    path('product_detail/<int:id>/',views.product_detail,name='product_detail'),

    # Other
    path('profile', views.profile, name='profile'),
    path('search',views.search,name='search'),
    ]
