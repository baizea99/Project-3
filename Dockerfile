FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install spacy

RUN python -m spacy download en_core_web_sm

RUN pip install git+https://github.com/amos6224/preprocess_kgptalkie.git --upgrade --force-reinstall

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]