import random
from http.client import HTTPException

import numpy as np
from fastapi import FastAPI, Form, Request, Response, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import io

from generate_image import generate_image
from get_emotions import get_emotions
from translate import translate

origins = [
    "http://localhost",
    "http://localhost:3000"
]


class FastApiApp:
    def __init__(self):
        self.app = FastAPI()
        self.app.mount("/static", StaticFiles(directory="static"), name="static")
        self.templates = Jinja2Templates(directory="templates")
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

        @self.app.get("/")
        def read_root(request: Request):
            return self.templates.TemplateResponse("form.html", {"request": request})

        @self.app.post("/process_text")
        def process_text(text: str = Form(...)):
            if not text.strip():
                raise HTTPException(status_code=400,
                                    detail="Введите текст для обработки.")
            emotion_dict = self.vectorize(text)
            image = self.generate_image(emotion_dict)
            img_byte_array = io.BytesIO()
            image.save(img_byte_array, format='PNG')
            img_byte_array = img_byte_array.getvalue()
            return Response(content=img_byte_array, media_type="image/png")

    @staticmethod
    def generate_random_emotion_dict():
        emotion_dict = {
            'Happy': random.random(),
            'Angry': random.random(),
            'Surprise': random.random(),
            'Sad': random.random(),
            'Fear': random.random(),
        }
        return emotion_dict

    @staticmethod
    def vectorize(text):
        en_text = translate(text)
        emotion_dict = get_emotions(en_text)
        salted_dict = get_salt(emotion_dict)
        # print(f'Emotions: {emotion_dict}')
        # print(f'Salted:   {salted_dict}')
        return salted_dict

    @staticmethod
    def generate_image(emotion_dict):
        image = generate_image(emotion_dict, 200, 200)
        return image


def get_salt(input_dict):
    values = np.array(list(input_dict.values()))
    random_numbers = np.random.uniform(0, 0.05, len(values))
    output_dict = {key: value + random
                   for key, value, random
                   in zip(input_dict.keys(), values, random_numbers)}
    return output_dict

