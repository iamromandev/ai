from django.urls import path
from . import views

urlpatterns = [
    path("lesson1/download/image", views.download_image, name="download-image"),
    path("lesson1/download/image/all", views.download_all_image, name="download-all-image"),
    path("lesson1/train", views.train_model, name="train-model"),
]