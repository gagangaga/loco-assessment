# Stage 1: Build dependencies
FROM python:3.9-slim-buster AS builder
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Build application
FROM python:3.9-slim-buster
WORKDIR /app
COPY --from=builder /usr/local/lib/python3.9/ /usr/local/lib/python3.9/
COPY . .
EXPOSE 80
CMD ["python", "app.py"]
