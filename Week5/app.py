from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load pre-trained models (assuming they are in the same directory)
with open("dv.bin", "rb") as f:
    dv = pickle.load(f)

with open("model2.bin", "rb") as f:
    model = pickle.load(f)


@app.route('/predict', methods=['POST'])
def predict():
    client_data = request.json
    X_client = dv.transform([client_data])
    probability = model.predict_proba(X_client)[0, 1]
    return jsonify({'probability': probability})


if __name__ == "__main__":
    app.run(host='0.0.0.0:8080', debug=True)
