from loguru import logger

from duckduckgo_search import ddg_images
from fastcore.all import (
    L as fastai_list,
)
from fastdownload import download_url

from config.settings import BASE_DIR

IMAGE_PARENT = BASE_DIR.joinpath('data/output')


def download_image(category):
    max = 1
    images = ddg_images(category, max_results=max)
    fastai_images = fastai_list(images).itemgot("image")

    saving_path = f"{IMAGE_PARENT}/{category}.jpg"
    download_url(fastai_images[0], saving_path, show_progress=False)

    return fastai_images
