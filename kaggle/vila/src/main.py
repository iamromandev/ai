from fastapi import FastAPI

app = FastAPI(
    title="AI Kaggle Vila",
    version="0.0.1",
)


@app.get("/")
def read_root():
    apply()

    return {"Hello": "World"}


def apply():
    print("Called Apply Method")
    import tensorflow_hub as hub

    images = ["/data/source/000000039769.jpg"]
    # image_bytes = load_image('image.png')
    model = hub.load("https://tfhub.dev/google/vila/image/1")
    predict_fn = model.signatures["serving_default"]
    # for image in images:
    #    image_bytes = load_image(image)
    #    predictions = predict_fn(tf.constant(image_bytes))
    #    aesthetic_score = predictions['predictions']


if __name__ == "__main__":
    apply()
