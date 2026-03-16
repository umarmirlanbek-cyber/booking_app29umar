from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models.fields import DateTimeField
from phonenumber_field.modelfields import PhoneNumberField

class Country(models.Model):
    country_name = models.CharField(max_length=64, unique=True)
    country_image = models.ImageField(upload_to='country_photo')

    def __str__(self):
        return self.country_name

class UserProfile(AbstractUser):
    ROLE_CHOICES = (
        ('client', 'client'),
        ('owner', 'owner'),
    )
    phone_number = PhoneNumberField(null=True, blank=True)
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(18),
                                                       MaxValueValidator(100)], null=True, blank=True)
    user_image = models.ImageField(upload_to='photo_user/', null=True, blank=True)
    data_register = models.DateTimeField(auto_now_add=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True,
                                related_name='users')
    role = models.CharField(choices=ROLE_CHOICES, default='client', max_length=32)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class City(models.Model):
    city_name = models.CharField(max_length=56)
    city_image = models.ImageField(upload_to='photo_city', null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE,
                                related_name='cities')

    def __str__(self):
        return self.city_name

class Service(models.Model):
    service_name = models.CharField(max_length=32, unique=True)
    service_image = models.ImageField(upload_to='service_photo')

    def __str__(self):
        return self.service_name

class Hotel(models.Model):
    hotel_name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE,
                             related_name='hotels')
    country = models.ForeignKey(Country, on_delete=models.CASCADE,
                                related_name='hotels')
    hotel_stars = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 6)],
                                                   null=True, blank=True)
    street = models.CharField(max_length=100)
    postal_index = models.PositiveSmallIntegerField(unique=True)
    service = models.ManyToManyField(Service, related_name='hotels')
    description = models.TextField()
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE,
                              related_name='hotels')

    def __str__(self):
        return f'{self.hotel_name} {self.hotel_stars}'

    def get_avg_rating(self):
        ratings = self.reviews.all()
        if ratings.exists():
            return round(sum([i.rating for i in ratings]) / ratings.count(), 2)
        return 0

    def get_count_review(self):
        return self.reviews.count()

class HotelImage(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE,
                              related_name='images')
    hotel_image = models.ImageField(upload_to='image_hotel')

class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE,
                              related_name='rooms')
    hotel_number = models.SmallIntegerField(unique=True)
    TYPE_CHOICES = (
        ('люкс', 'люкс'),
        ('полулюкс', 'полулюкс'),
        ('стандарт', 'стандарт'),
        ('эконом', 'эконом'),
        ('семейный', 'семейный'),
    )
    room_type = models.CharField(max_length=32, choices=TYPE_CHOICES)
    STATUS_ROOM = (
        ('свободный', 'свободный'),
        ('забронированный', 'забронированный'),
        ('занят', 'занят'),
    )
    room_status = models.CharField(max_length=32, choices=STATUS_ROOM)
    price = models.PositiveSmallIntegerField()
    room_description = models.TextField()
    max_guest = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.room_type} {self.room_status}'

class RoomImage(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE,
                             related_name='images')
    room_photo = models.ImageField(upload_to='image_room/')

class Booking(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE,
                              related_name='bookings')
    room = models.ForeignKey(Room, on_delete=models.CASCADE,
                             related_name='bookings')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE,
                             related_name='bookings')
    check_in = models.DateField()
    check_out = models.DateField()
    created_date = DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.hotel.hotel_name} {self.user.first_name}"

class Review(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE,
                              related_name='reviews')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE,
                             related_name='reviews')
    text = models.TextField(null=True, blank=True)
    rating = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 11)], null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.text