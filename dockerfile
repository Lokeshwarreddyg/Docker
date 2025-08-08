FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1 \
    INPUT_DIR=/working/input \
    OUTPUT_DIR=/output

# Create working/output dirs expected by CyVerse batch jobs
RUN mkdir -p /working /output

WORKDIR /app
COPY app.py /app/app.py

# Default command: run our app
CMD ["python", "/app/app.py"]
