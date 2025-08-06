FROM ubuntu:latest

RUN apt-get update && apt-get install -y python3 python3-pip

WORKDIR /app

COPY aqm-vergleich/ ./aqm-vergleich/

# Installiere Abhängigkeiten, falls requirements.txt existiert und nicht leer ist
RUN test -s aqm-vergleich/requirements.txt && pip3 install -r aqm-vergleich/requirements.txt || echo "Keine requirements installiert"

CMD ["python3", "aqm-vergleich/src/main.py"]