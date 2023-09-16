import json

from typing import Optional

from loguru import logger

from django.shortcuts import render
from django.http import HttpResponse



from duckduckgo_search import ddg_images
from fastcore.all import (
    L as fastai_list,
)


# Create your views here.
def download_image(request):
    image = "bird"
    max = 1000

    images = ddg_images(image, max_results=max)
    fastai_images = fastai_list(images).itemgot("image")

    logger.debug(f"Type of Images: {type(fastai_images)}")

    data = {
        "images": [fi for fi in fastai_images],
        "images_size": len(fastai_images)
    }
    return HttpResponse(json.dumps(data, sort_keys=False, indent=4))
