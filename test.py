import requests

response = requests.get("https://bank-notes.herokuapp.com/")
header = {"accept: application/json", "Content-Type: application/json"}
print(response.text)
params = {
    "variance": -0.36506,
    "skewness": 2.8928,
    "curtosis": -3.6461,
    "entropy": -3.0603,
}

article = requests.post(f"https://bank-notes.herokuapp.com/predict/", json=params)


data_dick = article.json()
data_dick.keys()
print(article.text)
# print(data_dick.keys())
# print(list(data_dick["ents"][1].values())[0])
