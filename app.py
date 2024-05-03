import logging
import os
import time

from flask import Flask, send_file
from picamera2 import Picamera2

app = Flask(__name__)

@app.route('/')
def snapshot():
    image_name = 'snapshot.jpg'

    picam2 = Picamera2()
    config = picam2.create_preview_configuration()
    picam2.configure(config)
    picam2.start()
    time.sleep(1)
    metadata = picam2.capture_file(image_name)
    print(metadata)
    picam2.stop()

    filepath = os.path.join(app.config['UPLOAD_FOLDER'], image_name)
    return send_file(filepath, as_attachment=False, download_name="snapshot.jpg",  mimetype='image/jpeg')

if __name__ == "__main__":
    # Configure logging
    logging.basicConfig(level=logging.INFO)  # Change the level to DEBUG for more detailed logging

    # Start the Flask application
    app.run(debug=False, host='0.0.0.0', port=8080)
