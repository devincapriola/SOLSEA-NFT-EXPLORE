FROM python:latest

EXPOSE 8501

WORKDIR /app

COPY requirements.txt ./requirements.txt
RUN pip install -U pip && pip install -r requirements.txt

COPY . .

CMD streamlit run app.py
