FROM python:3.11
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /code/app
CMD ["uvicorn", "--host", "0.0.0.0", "--reload", "--reload-dir", "/code/app", "app.main:app", "--port", "80"]

