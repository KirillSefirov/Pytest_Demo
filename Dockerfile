FROM python:3.11
LABEL authors="dpkarasev"

WORKDIR /pytest_demo

COPY . .
RUN pip install -r requirements.txt

CMD ["pytest"]