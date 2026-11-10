from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
]
urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('update/<int:id>/', views.update_menu, name='update_menu'),
    path('delete/<int:id>/', views.delete_menu, name='delete_menu'),
    path('order/', views.place_order, name='place_order'),
    path('orders/', views.order_list, name='order_list'),
    path('bill/<int:id>/', views.download_bill, name='download_bill'),
    path('tables/', views.table_list, name='table_list'),
    path('sales-report/', views.sales_report, name='sales_report'),
]