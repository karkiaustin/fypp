from django.core.exceptions import ValidationError
import pytz
from django.core.validators import MaxValueValidator
from django.db import models
from django.utils import timezone
from django.dispatch import receiver
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=500, unique=True)

    def __str__(self):
        return self.name


class Ads(models.Model):
    name = models.CharField(max_length=500)
    image = models.ImageField(upload_to="media")
    rank = models.IntegerField(validators=[MaxValueValidator(3)])

    def clean(self):
        if Ads.objects.count() >= 3 and not self.pk:
            raise ValidationError("Only three ads are allowed.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=500)
    image = models.ImageField(upload_to="media")
    description = models.TextField(max_length=150)
    slug = models.CharField(max_length=500, unique=True)

    def __str__(self):
        return self.name


class Member(models.Model):
    name = models.CharField(max_length=300)
    post = models.CharField(max_length=300)
    review = models.TextField()
    image = models.ImageField(upload_to="media", default="name")

    def __str__(self):
        return self.name


STOCK = (("in_stock", "In Stock"), ("out of stock", "Out of Stock"))
TYPE_CHOICES = [
    ("petrol", "Petrol"),
    ("Diesel", "Diesel"),
    ("electric", "Electric"),
]


class vehicle(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to="media", default="name")
    slug = models.CharField(max_length=500, unique=True)
    vehicle_description = models.TextField(blank=False, max_length=200, default="")
    vehicle_specification = models.TextField(blank=False, max_length=200, default="")
    price_per_day = models.IntegerField()
    vehicle_owner=models.ForeignKey(User, related_name="vehicle_owner", on_delete=models.CASCADE, null=True)
    Company_name = models.CharField(max_length=300)
    Company_contact = models.CharField(max_length=300)
    Vehicle_number = models.CharField(max_length=300)
    color = models.CharField(max_length=300)
    mileage = models.IntegerField()
    engine_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    TermsCondition1 = models.TextField(blank=False, max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    stock = models.CharField(choices=STOCK, max_length=50)

    def __str__(self):
        return self.name


class checkout(models.Model):
    name = models.CharField(max_length=300, null=True)
    vehicle_description = models.ForeignKey(vehicle, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Booking_User", null=True)
    Phone = models.CharField(max_length=300, null=True)
    Address = models.CharField(max_length=300, null=True)
    Start_date = models.DateField(null=True)
    total_days = models.IntegerField(null=True)
    is_ordered = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    def total_cost(self):
        return self.total_days * self.vehicle_description.price_per_day


class staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    Company_name = models.CharField(max_length=300)
    Company_document = models.ImageField(upload_to="media/documents/")
    Citizenship_document = models.ImageField(upload_to="media/citizenship/")

    def __str__(self):
        return self.First_name


class User_review(models.Model):
    username = models.CharField(max_length=300)
    star = models.IntegerField()
    slug = models.CharField(max_length=300)
    review = models.TextField(blank=False, max_length=600)
    date = models.DateField()

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        if self.date is None:
            self.date = timezone.now().date()
        super().save(*args, **kwargs)


class bulkbidding(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Phone = models.CharField(max_length=300)
    requirements = models.TextField(blank=False, max_length=200)
    date = models.DateField()
    is_accepted= models.BooleanField(default=False)

    def __str__(self):
        return self.Phone

class comment(models.Model):
    bid=models.ForeignKey(bulkbidding,on_delete=models.CASCADE, related_name='bid_comments', null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_comments', null=True)
    text=models.TextField()
    is_accepted=models.BooleanField(default=False)
