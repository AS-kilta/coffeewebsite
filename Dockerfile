# syntax=docker/dockerfile:1

FROM python:3.9

WORKDIR /coffeeWebsite

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

COPY . .

RUN pip install --no-cache --upgrade -r /coffeeWebsite/requirements.txt

CMD ["uvicorn", "server:app", "--reload", "--host", "0.0.0.0"]
