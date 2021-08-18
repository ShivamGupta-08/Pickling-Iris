import pickle
import requests

url = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")

def write_data():
    url_text = url.text
    url_split = url_text.split("\n")
    return url_split


pikling = "data.pkl"
with open(pikling,'wb') as e:
    pickle.dump(write_data(), e)
with open(pikling,'rb') as w:
    load = pickle.load(w)
print("------------------This is your output---------------------")
print("All items in list-")
print(load)
print("No of Items-")
print(len(load))
