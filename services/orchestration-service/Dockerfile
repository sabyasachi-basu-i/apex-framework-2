FROM python:3.10-slim

# Install curl for container healthchecks
RUN apt-get update \
    && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY apex_orchestration ./apex_orchestration
COPY main.py ./

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8003"]
