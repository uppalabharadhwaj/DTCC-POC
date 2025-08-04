from flask import Flask
import logging
import os
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.ext.flask.middleware import XRayMiddleware

app = Flask(__name__)

# Set up AWS X-Ray tracing
xray_recorder.configure(service='DTCC-Flask-App')
XRayMiddleware(app, xray_recorder)

# Make sure log directory exists
log_path = '/app/app.log'
os.makedirs(os.path.dirname(log_path), exist_ok=True)

# Configure logging to file inside Docker container (mounted to host)
logging.basicConfig(
    filename=log_path,
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)

@app.route('/')
def hello():
    logging.info("Hello endpoint hit")
    return "Hello from Flask with CloudWatch and X-Ray!"

if __name__ == '__main__':
    logging.info("Starting Flask app...")
    app.run(host='0.0.0.0', port=5000)