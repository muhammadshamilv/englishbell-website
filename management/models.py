from django.db import models


# -------------------------
# Enquiry Model
# -------------------------
class Enquiry(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    profession = models.CharField(max_length=100, blank=True, null=True)

    contacted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.phone}"


# -------------------------
# Asset Model (Images + Videos)
# -------------------------
class Asset(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='assets/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def is_video(self):
        return self.file.url.lower().endswith(('.mp4', '.webm', '.ogg'))

    def is_image(self):
        return self.file.url.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.webp'))

    def __str__(self):
        return self.title


# -------------------------
# Review Model
# -------------------------
class Review(models.Model):
    name = models.CharField(max_length=150)
    date = models.DateField()
    rating = models.IntegerField()
    comment = models.TextField()

    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def month_year(self):
        return self.date.strftime("%b %Y")

    def __str__(self):
        return f"{self.name} - {self.rating}⭐"


# -------------------------
# Advertisement Model
# -------------------------
class Advertisement(models.Model):
    AD_TYPE_CHOICES = (
        ('image', 'Image'),
        ('video', 'Video'),
        ('link', 'External Link'),
    )

    title = models.CharField(max_length=200)
    ad_type = models.CharField(
        max_length=10,
        choices=AD_TYPE_CHOICES,
        default='image'
    )

    file = models.FileField(upload_to='advertisements/%Y/%m/', blank=True, null=True)
    external_link = models.URLField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def is_video(self):
        return self.ad_type == 'video'

    def is_image(self):
        return self.ad_type == 'image'

    def __str__(self):
        return self.title


class Batch(models.Model):
    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='batches/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or f"Batch {self.id}"