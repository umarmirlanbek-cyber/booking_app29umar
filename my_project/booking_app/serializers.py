from rest_framework import serializers
from .models import (
    Country, UserProfile, City, Service,
    Hotel, HotelImage, Room, RoomImage, Booking, Review
)

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['country_name']

class CountryNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['country_name','country_image']


class CityListSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'city_name', 'city_image']

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['service_name','service_image']


class UserProfileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id','first_name','last_name','role']

class UserProfileDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class UserProfileReviewSerializer(serializers.ModelSerializer):
    country = CountryNameSerializer()
    class Meta:
        model = UserProfile
        fields = ['username','user_image','country']

class RoomImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomImage
        fields = ['room_photo']


class RoomListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id','room_type','hotel_number','price','room_status','max_guest','room_description']

class RoomDetailSerializer(serializers.ModelSerializer):
    room_image = RoomImageSerializer(read_only=True,many=True)
    class Meta:
        model = Room
        fields = ['room_type','hotel_number','room_description','room_image']


class HotelImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelImage
        fields = '__all__'


class ReviewListSerializer(serializers.ModelSerializer):
    user = UserProfileReviewSerializer()
    class Meta:
        model = Review
        fields = ['id','user','text']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class ReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['user','text','rating','created_date']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

class HotelDetailSerializer(serializers.ModelSerializer):
    owner = UserProfileListSerializer()
    service = ServiceSerializer(read_only=True,many=True)
    images = HotelImageSerializer(read_only=True,many=True)
    rooms = RoomListSerializer(read_only=True,many=True)
    reviews = ReviewListSerializer(read_only=True,many=True)
    avg_rating = serializers.SerializerMethodField()
    count_review = serializers.SerializerMethodField()
    class Meta:
        model = Hotel
        fields = ['id', 'hotel_name', 'city', 'country', 'hotel_stars',
                  'street', 'postal_index', 'description', 'owner',
                  'service', 'images', 'rooms', 'reviews','count_review','avg_rating']

    def get_avg_rating(self,obj):
        return obj.get_avg_rating()

    def get_count_review(self,obj):
        return obj.get_count_review()

class HotelListSerializer(serializers.ModelSerializer):
    country = CountryNameSerializer()
    photo_hotel = HotelImageSerializer(read_only=True,many=True)
    avg_rating = serializers.SerializerMethodField()
    count_review = serializers.SerializerMethodField()
    class Meta:
        model = Hotel
        fields = ['id', 'hotel_name', 'city', 'country', 'hotel_stars','avg_rating',
                  'street', 'postal_index','count_review','photo_hotel']

    def get_avg_rating(self,obj):
        return obj.get_avg_rating()

    def get_count_review(self,obj):
        return obj.get_count_review()

class CityDetailSerializer(serializers.ModelSerializer):
    country = CountrySerializer(read_only=True)
    hotels = HotelListSerializer(read_only=True,many=True)

    class Meta:
        model = City
        fields = ['id', 'city_name', 'city_image', 'country', 'hotels']

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'