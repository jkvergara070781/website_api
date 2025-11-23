from flask import Flask, render_template, request
import requests

app = Flask(__name__)

DOG_API_BASE = "https://dog.ceo/api"

@app.route('/', methods=['GET'])
def home():
    breeds_response = requests.get(f"{DOG_API_BASE}/breeds/list/all")
    breeds = breeds_response.json()["message"]

    breed = request.args.get("breed")

    if breed and breed != "random":
        img_response = requests.get(f"{DOG_API_BASE}/breed/{breed}/images/random")
    else:
        img_response = requests.get(f"{DOG_API_BASE}/breeds/image/random")  

    dog_image = img_response.json()["message"]

    return render_template("index.html", breeds=breeds, dog_image=dog_image, selected_breed=breed)

if __name__ == '__main__':
    app.run(debug=True)

    