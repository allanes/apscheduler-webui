FROM python:3.10.12

WORKDIR /app

# RUN pip install start-manager
# RUN start init
# RUN start install

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .
COPY src/ ./src/
COPY scripts/ ./scripts/

# CMD ["python", "scheduler.py"]
