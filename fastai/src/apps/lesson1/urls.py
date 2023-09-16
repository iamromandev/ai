from django.urls import path
from . import views

urlpatterns = [
    path("lesson1/download/image", views.download_image, name="download-image"),
]