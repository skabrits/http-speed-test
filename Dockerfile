FROM python:3.11
LABEL authors="sevak"

RUN apt update && apt install -y iperf

WORKDIR /app

COPY src/requirements.txt .
RUN pip install -r requirements.txt

COPY src/main.py entrypoint.sh ./
RUN chmod +x entrypoint.sh

COPY src/templates ./templates

EXPOSE 5000
EXPOSE 5001

ENTRYPOINT ["bash", "entrypoint.sh"]