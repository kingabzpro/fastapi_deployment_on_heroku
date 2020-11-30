from fastapi import FastAPI
import uvicorn
import pickle
import os
from banknote import BankNote

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'data/model.pkl')
TEMPLATES_PATH = os.path.join(BASE_DIR, 'templates')

app = FastAPI()
file_in = open(MODEL_PATH, 'rb')
classifier = pickle.load(file_in)
file_in.close()

@app.get("/")
def index():
    return {"message" : "Hello World" }

@app.get("/welcome")
def get_name(name : str):
    return {'Welcome to Python Mr.':f'{name}'}

@app.post("/predict")
def predict_banknote(data:BankNote):
    data = data.dict()
    variance = data['variance']
    skewness = data['skewness']
    curtosis = data['curtosis']
    entropy  = data['entropy']

    prediction = classifier.predict([[variance, skewness, curtosis, entropy]])
    if prediction[0] > 0.5:
        prediction = 'Fake Note'
    else:
        prediction = 'Original Note'

    return {'prediction' : prediction}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

# uvicorn app:app --reload