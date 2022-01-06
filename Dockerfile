FROM python:3.7-buster

RUN pip install -r requirements.txt

CMD streamlit run app.py
