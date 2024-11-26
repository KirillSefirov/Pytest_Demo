FROM python:3.11
LABEL authors="dpkarasev"

WORKDIR /pytest_demo

ENV BASE_URL='https://thinking-tester-contact-list.herokuapp.com/'

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["pytest", "--alluredir", "allure-results"]