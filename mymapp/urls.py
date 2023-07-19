from django.urls import path
from . import views

app_name = 'mymapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('shop/<int:shop_id>/', views.shop_detail, name='shop_detail'),
    path('add_shop/', views.add_shop, name='add_shop'),
    path('edit_shop/<int:shop_id>/', views.edit_shop, name='edit_shop'), 
    path('add_menu/<int:shop_id>/', views.add_menu, name='add_menu'),
    path('delete_shop/<int:shop_id>/', views.delete_shop, name='delete_shop'),
]

