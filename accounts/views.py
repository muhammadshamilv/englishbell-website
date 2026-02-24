from django.shortcuts import render, redirect
from .models import AdminUser
import random
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from datetime import timedelta
from django.utils.dateparse import parse_datetime



# Admin Login + First Time Setup
def admin_login(request):
    # Check if admin already exists
    admin = AdminUser.objects.first()
    setup_mode = False if admin else True

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        # FIRST TIME SETUP
        if setup_mode:
            confirm_password = request.POST.get("confirm_password")

            if password != confirm_password:
                return render(request, "custom_admin/login.html", {
                    "setup_mode": True,
                    "error": "Passwords do not match"
                })

            # Create Admin
            admin = AdminUser(email=email)
            admin.set_password(password)
            admin.save()

            # Login after setup
            request.session["admin_id"] = admin.id
            return redirect("/custom_admin/dashboard/")

        # NORMAL LOGIN
        else:
            try:
                admin = AdminUser.objects.get(email=email)
            except AdminUser.DoesNotExist:
                return render(request, "custom_admin/login.html", {
                    "setup_mode": False,
                    "error": "Invalid email or password"
                })

            if admin.check_password(password):
                request.session["admin_id"] = admin.id
                return redirect("/custom_admin/dashboard/")
            else:
                return render(request, "custom_admin/login.html", {
                    "setup_mode": False,
                    "error": "Invalid email or password"
                })

    return render(request, "custom_admin/login.html", {
        "setup_mode": setup_mode
    })


# Logout
def admin_logout(request):
    if "admin_id" in request.session:
        del request.session["admin_id"]
    return redirect("admin_login")

def admin_forgot_password(request):
    admin = AdminUser.objects.first()

    if not admin:
        return redirect("admin_login")

    # POST → Send OTP OR Reset Password
    if request.method == "POST":
        email = request.POST.get("email")
        otp_input = request.POST.get("otp")
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password")

        # STEP 1 — Send OTP
        if email and not otp_input:
            if email != admin.email:
                return render(request, "custom_admin/forgot-password.html", {
                    "error": "Email not found"
                })

            otp = str(random.randint(100000, 999999))

            # Store in session
            request.session["reset_otp"] = otp
            request.session["reset_email"] = email
            request.session["otp_expiry"] = (timezone.now() + timedelta(minutes=5)).isoformat()

            # Send email
            send_mail(
                subject="English Bell Admin Password Reset OTP",
                message=f"Your OTP is: {otp}\nValid for 5 minutes.",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[email],
                fail_silently=False,
            )

            return render(request, "custom_admin/forgot-password.html", {
                "otp_sent": True,
                "email": email,
                "success": "OTP sent to your email"
            })

        # STEP 2 — Verify OTP + Reset Password
        if otp_input:
            session_otp = request.session.get("reset_otp")
            expiry = request.session.get("otp_expiry")

            if not session_otp or not expiry:
                return render(request, "custom_admin/forgot-password.html", {
                    "error": "OTP expired. Try again."
                })
            
            expiry_time = parse_datetime(expiry)

            if timezone.now() > expiry_time:
                return render(request, "custom_admin/forgot-password.html", {
                    "error": "OTP expired. Try again."
                })

            if otp_input != session_otp:
                return render(request, "custom_admin/forgot-password.html", {
                    "otp_sent": True,
                    "error": "Invalid OTP"
                })

            # Password match check
            if new_password != confirm_password:
                return render(request, "custom_admin/forgot-password.html", {
                    "otp_sent": True,
                    "error": "Passwords do not match"
                })

            # Reset password
            admin.set_password(new_password)
            admin.save()

            # Clear session
            request.session.pop("reset_otp", None)
            request.session.pop("otp_expiry", None)
            request.session.pop("reset_email", None)

            return redirect("admin_login")

    return render(request, "custom_admin/forgot-password.html")
