import random
from http.client import HTTPException

from fastapi import FastAPI, Form, Request, Response, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import io

from generate_shapes import generate_shapes


class FastApiApp:
    def __init__(self):
        self.app = FastAPI()
        self.app.mount("/static", StaticFiles(directory="static"), name="static")
        self.templates = Jinja2Templates(directory="templates")

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

    def vectorize(self, text):
        return self.generate_random_emotion_dict()

    @staticmethod
    def generate_image(emotion_dict):
        image = generate_shapes(emotion_dict, 200, 200)
        return image
