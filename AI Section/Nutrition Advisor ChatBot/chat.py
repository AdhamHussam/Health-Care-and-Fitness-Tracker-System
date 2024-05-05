import random
import json
import torch
from model import NeuralNet
from nltk_utils import bag_of_words, tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)

FILE = "data.pth"
data = torch.load(FILE)  #save

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

def process(message):
        sentence = message
        sentence = tokenize(sentence)
        X = bag_of_words(sentence, all_words)
        X = X.reshape(1, X.shape[0])
        X = torch.from_numpy(X).to(device)

        output = model(X)
        _, predicted = torch.max(output, dim=1)

        tag = tags[predicted.item()]

        probs = torch.softmax(output, dim=1)
        prob = probs[0][predicted.item()]
        if prob.item() > 0.8:
            for intent in intents['intents']:
                if tag == intent["tag"]:
                    #print(f"{bot_name}: {random.choice(intent['responses'])}")
                    myresponse=intent['responses']
                    mybot=random.choice(myresponse)
                    return mybot
        else:
            #print(f"{bot_name}: I do not understand...")
            return("I don't understand!")


from flask import Flask, render_template, request
from jinja2 import Environment, FileSystemLoader

app = Flask(__name__)

# Use forward slashes or raw string for the template folder
template_folder = r"C:\Users\IShop\Documents\chattbot"
env = Environment(loader=FileSystemLoader(template_folder))
app.jinja_env = env

@app.route('/')
def home():
    # Render the template without the file extension
    return render_template('temp.html')

@app.route("/get")
def get_bot_response():
    user_text = request.args.get('msg')
    return str(process(user_text))

if __name__ == "__main__":
    app.run(debug=True)

