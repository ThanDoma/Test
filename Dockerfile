FROM python:3.10-slim-buster
RUN apt update -y && apt upgrade -y

WORKDIR /app
COPY . .

COPY requirements.txt requirements.txt
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip3 install -r requirements.txt


CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
