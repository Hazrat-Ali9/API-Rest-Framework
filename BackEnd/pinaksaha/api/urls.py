from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register(r'infos', views.DataList, basename='info')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('infos/',views.DataList.as_view()),
    path('infos/<int:pk>/', views.DataUpdateDelete.as_view()),
]