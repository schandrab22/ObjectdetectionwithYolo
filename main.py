from flask import Flask, request, render_template
import os
from flask_cors import CORS, cross_origin

import yolo3image

#
# os.putenv('LANG', 'en_US.UTF-8')
# os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)


# CORS(app)


# @cross_origin()
class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"


@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')


@app.route("/predict", methods=['POST', 'GET'])
# @cross_origin()
def predictRoute():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        base_path = os.path.dirname(__file__)
        file_path = os.path.join(
            base_path, 'uploads')
        f.save(file_path)
        print("File path", file_path)

        file = 'result.jpg'

        # File location
        location = "static/images/"
        path = os.path.join(location, file)
        # os.remove(path)
        if os.path.exists(path):
            os.remove(path)
            print("removed image")

        # Make prediction
        yolo3image.yolo3(file_path)
        result = 'success'
        return result
    return None


clApp = ClientApp()
# #port = int(os.getenv("PORT"))
if __name__ == "__main__":
    # clApp = ClientApp()
    # app.run(host='0.0.0.0', port=port)
    app.run(port=5002, debug=True)
