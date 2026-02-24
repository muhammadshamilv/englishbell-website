from django.db import models
from django.contrib.auth.hashers import make_password, check_password


class AdminUser(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    # Set hashed password
    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    # Verify password
    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    # Restrict to SINGLE ADMIN
    def save(self, *args, **kwargs):
        if not self.pk and AdminUser.objects.exists():
            raise ValueError("Only one admin account is allowed.")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email
