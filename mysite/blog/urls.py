from django.urls import path
from .views import *

urlpatterns = [
    path('user_profile/', UserProfileViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='user_profile'),
    path('user_profile/<int:pk>/', UserProfileViewSet.as_view({'get': 'retrieve', 'put': 'update','delete': 'destroy'}),
         name='hotel_detail'),

    path('hotel/', HotelViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='hotel'),
    path('hotel/<int:pk>/', HotelViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='hotel_detail'),

    path('comment', CommentViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='comment'),
    path('comment/<int:pk>/', CommentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='comment_detail'),

    path('images', ImagesViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='images'),
    path('images/<int:pk>/', ImagesViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='images_detail'),

    path('room', RoomViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='room'),
    path('room/<int:pk>/', RoomViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='room_detail'),

    path('book', BookingViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='booking'),
    path('book/<int:pk>/', BookingViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='booking_detail'),

]