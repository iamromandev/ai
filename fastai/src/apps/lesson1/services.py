from pathlib import Path

from loguru import logger

from duckduckgo_search import ddg_images
from fastcore.all import (
    L as FASTAI_LIST,
)
from fastai.vision.all import (
    download_images,
    resize_images,
    verify_images,
    get_image_files,
    DataBlock,
    ImageBlock,
    CategoryBlock,
    RandomSplitter,
    Resize,
    parent_label,
    vision_learner,
    resnet18,
    error_rate
)
from fastdownload import download_url

from config.settings import BASE_DIR

IMAGE_PARENT = BASE_DIR.joinpath('data/output/lesson1')
MAX_RESULTS = 10
LEARN_MODEL = None


def search_images(query: str, max_results: int = 0) -> FASTAI_LIST:
    images = ddg_images(query, max_results=max_results) if max_results > 0 else ddg_images(query)
    fastai_images = FASTAI_LIST(images).itemgot("image")
    return fastai_images


def download_image(category: str):
    saving_path = f"{IMAGE_PARENT}/{category}.jpg"

    images = search_images(category, max_results=1)
    download_url(images[0], saving_path, show_progress=False)

    return images


def download_all_image(category: str) -> list:
    saving_dir = IMAGE_PARENT.joinpath(category)
    saving_dir.mkdir(exist_ok=True, parents=True)

    suffixes = ["photo", "sun photo", "shade photo"]

    images = []

    # download images
    for suffix in suffixes:
        image_urls = search_images(query=f'{category} {suffix}', max_results=MAX_RESULTS)
        download_images(saving_dir, urls=image_urls)
        for url in image_urls:
            images.append(url)

    # resize images
    resize_images(saving_dir, max_size=400, dest=saving_dir)

    # remove corrupted images
    failed = verify_images(get_image_files(saving_dir))
    failed.map(Path.unlink)

    for image in images:
        logger.debug(image)

    return images


def train_model():
    dls = DataBlock(
        blocks=(ImageBlock, CategoryBlock),
        get_items=get_image_files,
        splitter=RandomSplitter(valid_pct=0.2, seed=42),
        get_y=parent_label,
        item_tfms=[Resize(192, method='squish')]
    ).dataloaders(IMAGE_PARENT, bs=32)

    # train
    global LEARN_MODEL
    logger.debug("Training Model...")
    LEARN_MODEL = vision_learner(dls, resnet18, metrics=error_rate)
    LEARN_MODEL.fine_tune(3)

    return {"Status": "Completed"}

def predict():

