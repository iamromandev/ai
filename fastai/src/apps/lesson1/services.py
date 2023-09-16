from loguru import logger

from duckduckgo_search import ddg_images
from fastcore.all import (
    L as FASTAI_LIST,
)
from fastai.vision.utils import download_images
from fastdownload import download_url

from config.settings import BASE_DIR

IMAGE_PARENT = BASE_DIR.joinpath('data/output')


def search_images(query: str, max_results: int = 0) -> FASTAI_LIST:
    images = ddg_images(query, max_results=max_results) if max_results > 0 else ddg_images(query)
    fastai_images = FASTAI_LIST(images).itemgot("image")
    return fastai_images


def download_image(category: str):
    saving_path = f"{IMAGE_PARENT}/{category}.jpg"

    images = search_images(category, max_results=1)

    download_url(images[0], saving_path, show_progress=False)

    return images


def download_all_image(category: str):
    saving_dir = IMAGE_PARENT.joinpath(category)
    saving_dir.mkdir(exist_ok=True, parents=True)

    download_images(saving_dir, urls=search_images(f'{category} photo'))
    download_images(saving_dir, urls=search_images(f'{category} sun photo'))
    download_images(saving_dir, urls=search_images(f'{category} shade photo'))

    return ["This"]
