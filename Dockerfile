FROM python:3.13-slim

WORKDIR /app

# Install dependencies
RUN pip install --no-cache-dir flask ansible pyyaml

# Copy application files
COPY jinja_tester.py .
COPY static/ ./static/
COPY templates/ ./templates/

# Expose port
EXPOSE 5002

# Run application
CMD ["python", "jinja_tester.py"]
