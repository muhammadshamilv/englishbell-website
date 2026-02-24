from django.contrib import admin
from .models import Enquiry, Asset, Review,  Advertisement


# Enquiry Admin
@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'profession', 'contacted', 'created_at')
    list_filter = ('contacted', 'profession')
    search_fields = ('name', 'email', 'phone')


# Asset Admin (Images + Videos)
@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at')
    search_fields = ('title',)


# -------------------------
# Review Admin
# -------------------------
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating', 'date', 'is_approved')
    list_filter = ('is_approved', 'rating')
    search_fields = ('name',)
    list_editable = ('is_approved',)


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ('title', 'ad_type', 'external_link', 'created_at')
    list_filter = ('ad_type',)
    search_fields = ('title',)
    ordering = ('-created_at',)
