from flask import Flask , jsonify
import requests
import openai
from tenacity import retry, wait_random_exponential, stop_after_attempt
from termcolor import colored
import requests 
import json
import config

GPT_MODEL = "gpt-3.5-turbo-0613"
openai.api_key = config.KEY
@retry(wait=wait_random_exponential(min=1, max=40), stop=stop_after_attempt(3))
def chat_completion_request(messages, functions=None, model=GPT_MODEL):
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + openai.api_key,
    }
    json_data = {"model": model, "messages": messages}
    if functions is not None:
        json_data.update({"functions": functions})
    try:
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers=headers,
            json=json_data,
        )
        return response
    except Exception as e:
        print("Unable to generate ChatCompletion response")
        print(f"Exception: {e}")
        return e
    
class Conversation:
    def __init__(self):
        self.conversation_history = []

    def add_message(self, role, content):
        message = {"role": role, "content": content}
        self.conversation_history.append(message)

    def display_conversation(self, detailed=False):
        role_to_color = {
            "system": "red",
            "user": "green",
            "assistant": "blue",
            "function": "magenta",
        }
        for message in self.conversation_history:
            print(
                colored(
                    f"{message['role']}: {message['content']}\n\n",
                    role_to_color[message["role"]],
                )
            )



app = Flask(__name__)
@app.route('/')
def home():
    return "Hello World"

@app.route('/sentiment/<text>')
def sentiment(text):
    conversation = Conversation()
    conversation.add_message("user", f"Analyze the sentiment of following text and only output sentiment nothing else ex - positive , negative etc :{text}")
    chat_response = chat_completion_request(
    conversation.conversation_history,
    # functions = None
)
    output = json.loads(chat_response.text)
    return jsonify(output)
    

@app.route('/named-entity/<text>')
def named_entity(text):
    conversation = Conversation()
    conversation.add_message("user", f"Do named entity recognition in the given sentence and also which type of entity is that please also provide and only output i want nothing extra explaination :{text}")
    chat_response = chat_completion_request(
    conversation.conversation_history,
    # functions = None
)
    output = json.loads(chat_response.text)
    return jsonify(output)

@app.route('/translation/<text>/<language>')
def translation(text,language):
    conversation = Conversation()
    conversation.add_message("user",f"Translate this sentence to {language} only output the translation nothing extra : {text}")
    chat_response = chat_completion_request(
    conversation.conversation_history,
    # functions = None
)
    output = json.loads(chat_response.text)
    return jsonify(output)


@app.route('/pos/<text>')
def pos(text):
    conversation = Conversation()
    conversation.add_message("user",f"Please provide the parts of speech tagging and only output for the {text}")
    chat_response = chat_completion_request(
    conversation.conversation_history,
    # functions = None
)
    output = json.loads(chat_response.text)
    return jsonify(output)

@app.route('/grammar_check/<text>')
def grammar_check(text):
    conversation = Conversation()
    conversation.add_message("user",f"Check the grammar and spelling and correct them return only originial sentence with corrected grammar and spelling  nothing extra : {text}")
    chat_response = chat_completion_request(
    conversation.conversation_history,
    # functions = None
)
    output = json.loads(chat_response.text)
    return jsonify(output)

@app.route('/summary/<text>')
def summary(text):
    conversation = Conversation()
    conversation.add_message("user",f"For the given text give best summary of the text as output nothing extra : {text}")
    chat_response = chat_completion_request(
    conversation.conversation_history,
    # functions = None
)
    output = json.loads(chat_response.text)
    return jsonify(output)

@app.route('/question-answer/<question>/<context>')
def question_answer(question,context):
    conversation = Conversation()
    conversation.add_message("user",f"Answer the following question only output answer nothing extra: {question}\nContext: {context}")
    chat_response = chat_completion_request(
    conversation.conversation_history,
    # functions = None
)
    output = json.loads(chat_response.text)
    return jsonify(output)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)