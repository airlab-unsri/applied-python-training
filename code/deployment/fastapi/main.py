import numpy as np
import tensorflow as tf
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

class_names = [
    "T-shirt/top",
    "Trouser",
    "Pullover",
    "Dress",
    "Coat",
    "Sandal",
    "Shirt",
    "Sneaker",
    "Bag",
    "Ankle boot",
]


class PredictInput(BaseModel):
    instances: list


app = FastAPI()

model = tf.keras.models.load_model("./model/1.keras")


@app.get("/")
def hello_world():
    return "Hello, world!"


@app.post("/predict")
def predict(input: PredictInput):
    instances = tf.constant(input.instances, dtype=tf.float32)
    predictions = model(instances)
    response = {
        "predictions": predictions.numpy().tolist(),
        "message": f"The model thought this was a {class_names[np.argmax(predictions)]} (class {np.argmax(predictions)})",
    }
    return JSONResponse(content=response)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
