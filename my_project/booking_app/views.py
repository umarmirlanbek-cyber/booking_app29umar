from rest_framework import generics,viewsets
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly,AllowAny,IsAdminUser
from .pagination import HotelListPagination,RoomListPagination
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .filters import RoomFilter,HotelFilter
from .models import (
    Country, UserProfile, City, Service,
    Hotel, HotelImage, Room, RoomImage, Booking, Review
)
from .serializers import (
    RoomSerializer,HotelSerializer,CountrySerializer, UserProfileListSerializer,UserProfileDetailSerializer, CityDetailSerializer,CityListSerializer, ServiceSerializer,
    HotelListSerializer,HotelDetailSerializer, HotelImageSerializer, RoomListSerializer,RoomDetailSerializer, RoomImageSerializer,
    BookingSerializer, ReviewListSerializer,ReviewDetailSerializer,ReviewSerializer
)
from .permissions import ClientPermission,OwnerPermission

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class HotelCreateViewAPIView(generics.CreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = [OwnerPermission]

class HotelEditViewAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = [OwnerPermission]

class UserProfileListAPIView(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileListSerializer

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)

class UserProfileDetailAPIView(generics.RetrieveAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileDetailSerializer

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)

class CityListAPIView(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CityListSerializer

class CityDetailAPIView(generics.RetrieveAPIView):
    queryset = City.objects.all()
    serializer_class = CityDetailSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class HotelListAPIView(generics.ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelListSerializer
    pagination_class = HotelListPagination
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    search_fields = ['hotel_name']
    ordering_fields = ['hotel_stars']
    filterset_class = HotelFilter

class HotelDetailAPIView(generics.RetrieveAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelDetailSerializer

class HotelImageViewSet(viewsets.ModelViewSet):
    queryset = HotelImage.objects.all()
    serializer_class = HotelImageSerializer

class RoomListAPIView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomListSerializer
    pagination_class = RoomListPagination
    filter_backends = [DjangoFilterBackend,OrderingFilter]
    ordering_fields = ['price']
    filterset_class = RoomFilter

class RoomCreateViewAPIView(generics.CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [OwnerPermission]

class RoomEditViewAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [OwnerPermission]

    def get_queryset(self):
        return Hotel.objects.filter(owner=self.request.user)

class RoomDetailAPIView(generics.RetrieveAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomDetailSerializer

class RoomImageViewSet(viewsets.ModelViewSet):
    queryset = RoomImage.objects.all()
    serializer_class = RoomImageSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [ClientPermission]

class ReviewListAPIView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewListSerializer

class ReviewDetailAPIView(generics.RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewDetailSerializer

class ReviewCreateAPIView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [ClientPermission]

class ReviewUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [ClientPermission]

    def get_queryset(self):
        return Review.objects.filter(user=self.request.user)