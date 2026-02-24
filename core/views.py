from django.shortcuts import render, redirect
from management.models import Enquiry, Asset, Review, Advertisement, Batch
from django.db.models import Avg
from datetime import date
from django.utils import timezone
from django.contrib import messages
from django.http import JsonResponse
from django.conf import settings
from django.core.mail import send_mail


# Home Page
def home(request):
    assets = Asset.objects.all().order_by('-uploaded_at')
    reviews = Review.objects.filter(is_approved=True).order_by('-created_at')
    ads = Advertisement.objects.order_by('-created_at')[:4]
    batch_images = Batch.objects.all().order_by('-created_at')  # ADD THIS

    avg_rating = reviews.aggregate(avg=Avg('rating'))['avg']
    total_reviews = reviews.count()

    return render(request, 'index.html', {
        'assets': assets,
        'reviews': reviews,
        'avg_rating': round(avg_rating, 1) if avg_rating else 0,
        'total_reviews': total_reviews,
        'ads': ads,
        'batch_images': batch_images,   # ADD THIS
    })

# About Page
def about(request):
    assets = Asset.objects.all().order_by('-uploaded_at')
    reviews = Review.objects.all().order_by('-created_at')
    batch_images = Batch.objects.all().order_by('-created_at')   

    return render(request, 'about.html', {
        'assets': assets,
        'reviews': reviews,
        'batch_images': batch_images,
    })


# Courses Page (Static)
def courses(request):
    return render(request, 'courses.html')


# Contact Page
def contact(request):
    return render(request, 'contact.html')


# Save Enquiry (Form Handler)
def save_enquiry(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        profession = request.POST.get("profession")

        # Save to database
        Enquiry.objects.create(
            name=name,
            email=email,
            phone=phone,
            profession=profession
        )

        # ======================
        # Send Email to Admin
        # ======================
        subject = "New Enquiry - English Bell"

        message = f"""
New enquiry received from website

Name: {name}
Email: {email}
Phone: {phone}
Profession: {profession}

Date: {request.headers.get('Date', '')}
        """

        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [settings.ADMIN_EMAIL],
            fail_silently=True,
        )

        return JsonResponse({"status": "success"})

    return JsonResponse({"status": "error"})


def save_review(request):
    if request.method == "POST":
        Review.objects.create(
            name=request.POST.get("name"),
            date=request.POST.get("date"),
            rating=int(request.POST.get("rating")),
            comment=request.POST.get("comment")
        )

        messages.success(request, "review_submitted")
        return JsonResponse({"status": "success"})

    return redirect('home')


def submit_review(request):
    if request.method == "POST":
        name = request.POST.get("name")
        date = request.POST.get("date")
        rating = request.POST.get("rating")
        comment = request.POST.get("comment")

        Review.objects.create(
            name=name,
            date=date,
            rating=int(rating),
            comment=comment,
            is_approved=False
        )

        return JsonResponse({"status": "success"})

    return JsonResponse({"status": "error"})