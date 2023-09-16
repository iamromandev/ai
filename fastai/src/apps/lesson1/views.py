import json

from typing import Optional

from loguru import logger

from django.shortcuts import render
from django.http import HttpResponse

from . import services


# Create your views here.
def download_image(request):
    category = request.GET.get("category", "man")
    fastai_images = services.download_image(category)

    logger.debug(f"Type of Images: {type(fastai_images)}")

    data = {
        "category": category,
        "images_size": len(fastai_images),
        "images": [fi for fi in fastai_images],
    }
    return HttpResponse(json.dumps(data, sort_keys=False, indent=4))


def download_all_image(request):
    category = request.GET.get("category", "man")
    fastai_images = services.download_all_image(category)

    logger.debug(f"Type of Images: {type(fastai_images)}")

    data = {
        "category": category,
        "images_size": len(fastai_images),
        "images": [fi for fi in fastai_images],
    }
    return HttpResponse(json.dumps(data, sort_keys=False, indent=4))
