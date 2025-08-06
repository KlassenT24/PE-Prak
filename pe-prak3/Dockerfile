FROM ubuntu:latest

RUN apt-get update && apt-get install -y python3 python3-pip

WORKDIR /app

# Kopiere das lokale Projektverzeichnis in den Container
COPY aqm-vergleich/ ./aqm-vergleich/

# Installiere Abhängigkeiten, falls requirements.txt existiert
RUN if [ -f aqm-vergleich/requirements.txt ]; then pip3 install -r aqm-vergleich/requirements.txt; fi

CMD ["python3", "aqm-vergleich/src/main.py"]