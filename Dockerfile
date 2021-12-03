FROM python:3.9

EXPOSE 5000

WORKDIR /pythonProject2

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

