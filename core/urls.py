from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('courses/', views.courses, name='courses'),  
    path('contact/', views.contact, name='contact'),

    # Enquiry form submit
    path('save-enquiry/', views.save_enquiry, name='save_enquiry'),

    path('save-review/', views.save_review, name='save_review'),
    path('submit-review/', views.submit_review, name='submit_review'),

]
