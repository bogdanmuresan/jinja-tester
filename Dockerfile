FROM python:3.13-slim

WORKDIR /app

# Install dependencies
RUN pip install --no-cache-dir flask ansible pyyaml

# Copy application files
COPY jinja_tester_simple.py .
COPY static/ ./static/

# Expose port
EXPOSE 5002

# Run application
CMD ["python", "jinja_tester_simple.py"]
