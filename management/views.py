from django.shortcuts import render, redirect
from .models import Enquiry, Asset, Review, Advertisement, Batch
from django.contrib import messages


# ===============================
# Helper: Check admin session
# ===============================
def check_admin_session(request):
    return 'admin_id' in request.session


# ===============================
# Dashboard
# ===============================
def dashboard(request):
    if not check_admin_session(request):
        return redirect('admin_login')

    total_enquiries = Enquiry.objects.count()
    pending_enquiries = Enquiry.objects.filter(contacted=False).count()
    total_assets = Asset.objects.count()

    total_reviews = Review.objects.count()
    pending_reviews = Review.objects.filter(is_approved=False).count()

    recent_enquiries = Enquiry.objects.order_by('-created_at')[:5]

    return render(request, 'custom_admin/dashboard.html', {
        'total_enquiries': total_enquiries,
        'pending_enquiries': pending_enquiries,
        'total_assets': total_assets,
        'total_reviews': total_reviews,
        'pending_reviews': pending_reviews,
        'recent_enquiries': recent_enquiries,
    })


# ===============================
# Enquiries
# ===============================
def enquiries(request):
    if not check_admin_session(request):
        return redirect('admin_login')

    enquiries = Enquiry.objects.all().order_by('-created_at')

    return render(request, 'custom_admin/enquiries.html', {
        'enquiries': enquiries
    })


def mark_contacted(request, id):
    if not check_admin_session(request):
        return redirect('admin_login')

    enquiry = Enquiry.objects.filter(id=id).first()
    if enquiry:
        enquiry.contacted = True
        enquiry.save()

    return redirect('admin_enquiries')


# Delete Enquiry
def delete_enquiry(request, id):
    if not check_admin_session(request):
        return redirect('admin_login')

    enquiry = Enquiry.objects.filter(id=id).first()
    if enquiry:
        enquiry.delete()

    return redirect('admin_enquiries')


# ===============================
# Asset Management (Images + Videos)
# ===============================
def assets(request):
    if not check_admin_session(request):
        return redirect('admin_login')

    assets = Asset.objects.all().order_by('-uploaded_at')

    # Detect file type
    for asset in assets:
        file_name = asset.file.name.lower()
        if file_name.endswith(('.mp4', '.webm', '.mov', '.avi')):
            asset.is_video = True
        else:
            asset.is_video = False

    return render(request, 'custom_admin/assets.html', {
        'assets': assets
    })


def upload_asset(request):
    if not check_admin_session(request):
        return redirect('admin_login')

    if request.method == "POST":
        file = request.FILES.get("file")
        title = request.POST.get("title")

        if file:
            Asset.objects.create(
                title=title,
                file=file
            )

    return redirect('admin_assets')


def delete_asset(request, id):
    if not check_admin_session(request):
        return redirect('admin_login')

    asset = Asset.objects.filter(id=id).first()

    if asset:
        asset.file.delete()
        asset.delete()

    return redirect('admin_assets')


def reviews(request):
    if not check_admin_session(request):
        return redirect('admin_login')

    reviews = Review.objects.all().order_by('-created_at')

    return render(request, 'custom_admin/reviews.html', {
        'reviews': reviews
    })


def approve_review(request, id):
    if not check_admin_session(request):
        return redirect('admin_login')

    review = Review.objects.filter(id=id).first()
    if review:
        review.is_approved = True
        review.save()

    return redirect('admin_reviews')


def delete_review(request, id):
    if not check_admin_session(request):
        return redirect('admin_login')

    review = Review.objects.filter(id=id).first()
    if review:
        review.delete()

    return redirect('admin_reviews')

# ===============================
# Advertisements
# ===============================
def advertisements(request):
    if not check_admin_session(request):
        return redirect('admin_login')

    ads = Advertisement.objects.all().order_by('-created_at')

    return render(request, 'custom_admin/advertisements.html', {
        'ads': ads
    })


def upload_advertisement(request):
    if not check_admin_session(request):
        return redirect('admin_login')

    if request.method == "POST":
        title = request.POST.get("title")
        ad_type = request.POST.get("ad_type")
        file = request.FILES.get("file")
        link = request.POST.get("external_link")

        # Basic validation
        if not title or not ad_type:
            messages.error(request, "Title and type are required.")
            return redirect('admin_advertisements')

        # Type-based validation
        if ad_type in ['image', 'video']:
            if not file:
                messages.error(request, "Please upload a file.")
                return redirect('admin_advertisements')
            link = None  # Remove link if file type

        if ad_type == 'link':
            if not link:
                messages.error(request, "Please provide a valid link.")
                return redirect('admin_advertisements')
            file = None  # Remove file if link type

        # Save advertisement
        Advertisement.objects.create(
            title=title,
            ad_type=ad_type,
            file=file,
            external_link=link
        )

        messages.success(request, "Advertisement added successfully.")

    return redirect('admin_advertisements')



def delete_advertisement(request, id):
    if not check_admin_session(request):
        return redirect('admin_login')

    ad = Advertisement.objects.filter(id=id).first()

    if ad:
        if ad.file:
            ad.file.delete()
        ad.delete()

    return redirect('admin_advertisements')


# ===============================
# Successful Batches
# ===============================
def batches(request):
    if not check_admin_session(request):
        return redirect('admin_login')

    batches = Batch.objects.all().order_by('-created_at')

    return render(request, 'custom_admin/batches.html', {
        'batches': batches
    })


def upload_batch(request):
    if not check_admin_session(request):
        return redirect('admin_login')

    if request.method == "POST":
        title = request.POST.get("title")
        image = request.FILES.get("image")

        if image:
            Batch.objects.create(
                title=title,
                image=image
            )

    return redirect('admin_batches')


def delete_batch(request, id):
    if not check_admin_session(request):
        return redirect('admin_login')

    batch = Batch.objects.filter(id=id).first()

    if batch:
        batch.image.delete()
        batch.delete()

    return redirect('admin_batches')