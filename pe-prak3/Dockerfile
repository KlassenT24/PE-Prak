FROM ubuntu:latest

RUN apt-get update && apt-get install -y git python3 python3-pip

WORKDIR /app

# Klone das Repo in einen Unterordner
RUN git clone https://github.com/KlassenT24/PE-Prak.git

# Installiere Abhängigkeiten, falls requirements.txt existiert
RUN if [ -f PE-Prak/requirements.txt ]; then pip3 install -r PE-Prak/requirements.txt; fi

# Standard-Kommando (optional)
CMD ["python3", "PE-Prak/src/main.py"]