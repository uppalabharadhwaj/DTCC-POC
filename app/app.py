from flask import Flask
import logging
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.ext.flask.middleware import XRayMiddleware

app = Flask(__name__)

# Integrate X-Ray
xray_recorder.configure(service='DTCC-Flask-App')
XRayMiddleware(app, xray_recorder)

# Setup logging to file (for CloudWatch)
logging.basicConfig(
    filename='/home/ubuntu/app/app.log',
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
