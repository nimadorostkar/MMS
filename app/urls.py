from django.urls import path, re_path
from app import views

app_name='app'



urlpatterns = [
    # The home page
    path('', views.mold, name='mold'),

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

    # Manufacture Request
    path('manufacture_req', views.manufacture_req, name='manufacture_req'),
    path('manufacture_req_detail/<int:id>/',views.manufacture_req_detail,name='manufacture_req_detail'),

    # Repair request
    path('repair_req', views.repair_req, name='repair_req'),
    path('repair_req_detail/<int:id>/',views.repair_req_detail,name='repair_req_detail'),
    path('repair_operation_detail/<int:id>/',views.repair_operation_detail,name='repair_operation_detail'),

    # Component Request
    path('component_req', views.component_req, name='component_req'),
    path('component_req_detail/<int:id>/',views.component_req_detail,name='component_req_detail'),

    # Other
    path('profile', views.profile, name='profile'),
    path('search',views.search,name='search'), 
    ]
