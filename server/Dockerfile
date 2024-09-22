FROM python:3.11-alpine
WORKDIR /server/app
COPY server/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY server/app/ ./
CMD ["python", "websocket.py"]