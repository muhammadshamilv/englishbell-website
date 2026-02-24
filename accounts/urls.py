from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_login, name='admin_login'),   # /admin/
    path('login/', views.admin_login, name='admin_login'),
    path('logout/', views.admin_logout, name='admin_logout'),
    path('forgot-password/', views.admin_forgot_password, name='admin_forgot_password'),

]
