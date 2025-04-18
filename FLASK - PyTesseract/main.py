from flask import request, render_template, url_for, Flask
import os
from werkzeug.utils import secure_filename
import pytesseract
from PIL import Image

app = Flask(__name__)

app.config["INITIAL_FILE_UPLOADS"] = "static/uploads"


def extract_text(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)

    #remove symbols and split by lines for better display
    characters_to_remove = "!@#$%^&*()_+-=[]{};:'\"\\|,<.>/?`~"
    cleaned = ''.join(char for char in text if char not in characters_to_remove)
    extracted_text = cleaned.split("\n")
    return extracted_text


@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        image_upload = request.files["image_upload"]                                #Grabs the uploaded image file.

        filename = secure_filename(image_upload.filename)
        filepath = os.path.join(app.config["INITIAL_FILE_UPLOADS"], filename)       #Cleans up the filename (removes any malicious paths) and builds the full file path.

        os.makedirs(app.config["INITIAL_FILE_UPLOADS"], exist_ok=True)              # Make sure upload folder exists

        image_upload.save(filepath)                                                 #uploaded image save in filepath

        extracted_text = extract_text(filepath)
        img_url = url_for('static', filename='uploads/'+filename)           #Builds the URL to display the uploaded image.

        return render_template("index.html", img_url=img_url, text=extracted_text)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)