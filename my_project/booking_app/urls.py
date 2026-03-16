from django.urls import include,path
from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import (
    CountryViewSet, UserProfileListAPIView, UserProfileDetailAPIView, CityListAPIView, CityDetailAPIView,
    ServiceViewSet,
    HotelListAPIView, HotelDetailAPIView, HotelImageViewSet, RoomListAPIView, RoomDetailAPIView, RoomImageViewSet,
    BookingViewSet, ReviewListAPIView, ReviewDetailAPIView, ReviewCreateAPIView,
    ReviewUpdateAPIView,HotelCreateViewAPIView,HotelEditViewAPIView,RoomEditViewAPIView,RoomCreateViewAPIView
)

router = SimpleRouter()
router.register(r'countries', CountryViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'hotel-images', HotelImageViewSet)
router.register(r'room-images', RoomImageViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('hotel/',HotelListAPIView.as_view(),name='hotel_list'),
    path('hotel/<int:pk>', HotelDetailAPIView.as_view(), name='hotel_detail'),
    path('city/', CityListAPIView.as_view(), name='city_list'),
    path('city/<int:pk>', CityDetailAPIView.as_view(), name='city_detail'),
    path('room/', RoomListAPIView.as_view(), name='room_list'),
    path('room/<int:pk>', RoomDetailAPIView.as_view(), name='room_detail'),
    path('review/', ReviewListAPIView.as_view(), name='review_list'),
    path('review/<int:pk>', ReviewDetailAPIView.as_view(), name='review_detail'),
    path('review/create', ReviewCreateAPIView.as_view(), name='review_create'),
    path('review/<int:pk>/update', ReviewUpdateAPIView.as_view(), name='review_update'),
    path('user/', UserProfileListAPIView.as_view(), name='user_list'),
    path('user/<int:pk>', UserProfileDetailAPIView.as_view(), name='user_detail'),
    path('hotel/create', HotelCreateViewAPIView.as_view(), name='hotel_create'),
    path('hotel/<int:pk>/edit', HotelEditViewAPIView.as_view(), name='hotel_edit'),
    path('room/create', RoomCreateViewAPIView.as_view(), name='room_create'),
    path('room/<int:pk>/edit', RoomEditViewAPIView.as_view(), name='room_edit'),
]
