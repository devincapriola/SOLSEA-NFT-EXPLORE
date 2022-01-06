FROM python:3.7-buster

RUN \
    apt-get update && \
    apt-get install -y gcc &&\
    apt-get install -y g++

COPY ./requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD streamlit run app.py
