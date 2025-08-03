FROM python:3.9

WORKDIR /app

# Copy application code
COPY . .

# Install required Python packages
RUN pip install flask aws-xray-sdk

# Expose Flask app port
EXPOSE 5000

# Start the Flask app
CMD ["python", "app.py"]
