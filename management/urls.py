from django.urls import path
from . import views

urlpatterns = [
    # Dashboard
    path('dashboard/', views.dashboard, name='admin_dashboard'),

    # Enquiries
    path('enquiries/', views.enquiries, name='admin_enquiries'),
    path('enquiry/contacted/<int:id>/', views.mark_contacted, name='mark_contacted'),
    path('enquiry/delete/<int:id>/', views.delete_enquiry, name='delete_enquiry'),

    # Assets (Images + Videos)
    path('assets/', views.assets, name='admin_assets'),
    path('asset/upload/', views.upload_asset, name='upload_asset'),
    path('asset/delete/<int:id>/', views.delete_asset, name='delete_asset'),

    # Reviews
    path('reviews/', views.reviews, name='admin_reviews'),
    path('review/approve/<int:id>/', views.approve_review, name='approve_review'),
    path('review/delete/<int:id>/', views.delete_review, name='delete_review'),

    # Advertisements
    path('advertisements/', views.advertisements, name='admin_advertisements'),
    path('advertisement/upload/', views.upload_advertisement, name='upload_advertisement'),
    path('advertisement/delete/<int:id>/', views.delete_advertisement, name='delete_advertisement'),
    
    # Successful Batches
    path('batches/', views.batches, name='admin_batches'),
    path('batch/upload/', views.upload_batch, name='upload_batch'),
    path('batch/delete/<int:id>/', views.delete_batch, name='delete_batch'),


]
