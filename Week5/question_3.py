import pickle

# 1. Load the models using Pickle.
with open("dv.bin", "rb") as file:
    dv = pickle.load(file)

with open("model1.bin", "rb") as file:
    model = pickle.load(file)

# 2. Vectorize the client's data.
client_data = {"job": "retired", "duration": 445, "poutcome": "success"}
X_client = dv.transform([client_data])

# 3. Predict the probability using the model.
probability = model.predict_proba(X_client)[0, 1]
print(probability)  # 0.902
