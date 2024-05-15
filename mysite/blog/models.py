from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    age = models.PositiveIntegerField(default=0, blank=True, null=True)
    country = models.CharField(max_length=32, blank=True,null=True)
    photo = models.ImageField(upload_to="images/", blank=True, null=True)
    phone_number = models.IntegerField()
    email = models.EmailField()


class Hotel(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    country = models.CharField(max_length=32)
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(0, 6)],
                                default=0, verbose_name="Оценка")


class Comment(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(0, 6)],
                                default=0, verbose_name="Оценка")




class Images(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/", blank=True, null=True)


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_number = models.PositiveSmallIntegerField(default=0)
    capacity = models.PositiveSmallIntegerField(default=0)
    price_per_night = models.DecimalField(max_digits=5, decimal_places=2)


class Booking(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    total_price = models.DecimalField(max_digits=5, decimal_places=2)
    STATUS_CHOICES = (
        ('zanit', 'Zanit'),
        ('bron', 'Bron'),
        ('svobodno', 'Svobodno'),
    )
    status = models.CharField(max_length=32, choices=STATUS_CHOICES, default='simple')