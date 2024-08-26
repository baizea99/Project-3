FROM python:3.9

WORKDIR /app

COPY requirements.txt .

COPY . .

RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    libffi-dev \
    libssl-dev \
    python3-dev

RUN apt-get update && apt-get install -y libhdf5-dev

RUN pip install --no-binary h5py h5py

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]
