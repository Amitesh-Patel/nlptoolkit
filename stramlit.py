import openai
import streamlit as st
import os 
from tenacity import retry, wait_random_exponential, stop_after_attempt
from termcolor import colored
import json
import requests
import confi
from streamlit_option_menu import option_menu

GPT_MODEL = "gpt-3.5-turbo-0613"
openai.api_key = confi.KEY
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


with st.sidebar:
    selected = option_menu('NLP ToolKit',
                          
                          ['Sentiment',
                           'Question-Answering',
                           'NER',
                           'Text Summarization',
                           'Translation',
                           'Grammar Check',
                           'POS'],
                          icons=['activity','heart','person'],
                          default_index=0)

st.title("NLP ToolKit")

if (selected == 'Sentiment'):
    st.header("Sentiment Analysis")
    
    user_input = st.text_input("Enter Text:", key='input')
    
    if user_input:
        conversation = Conversation()
        conversation.add_message("user", f"Analyze the sentiment of the following text and only output Negative, Positive sentiment, etc. nothing else:\n{user_input}")

        chat_response = chat_completion_request(
            conversation.conversation_history,
            # functions = None
        )

        output = json.loads(chat_response.text)

        # Display the output
        if output['choices']:
            sentiment = output['choices'][0]['message']['content']
            
            st.subheader("Input Text:")
            st.info(user_input)
            
            st.subheader("Sentiment:")
            st.success(sentiment)
            
            # Visualize sentiment with a color bar
            sentiment_score = 0.5  # Assume sentiment score is between 0 and 1
            
            if "Positive" in sentiment:
                sentiment_score = 0.8
            elif "Negative" in sentiment:
                sentiment_score = 0.2
            
            color_bar = f'''
                <style>
                .color-bar-container {{
                    width: 100%;
                    height: 20px;
                    background-color: #eee;
                    border-radius: 10px;
                    margin-top: 10px;
                }}
                .color-bar {{
                    height: 100%;
                    border-radius: 10px;
                    background-image: linear-gradient(to right, green 0%, green {sentiment_score*100}%, red {sentiment_score*100}%, red 100%);
                }}
                </style>
                <div class="color-bar-container">
                    <div class="color-bar"></div>
                </div>
            '''
            
            st.markdown(color_bar, unsafe_allow_html=True)
    else:
        st.info("Please enter a text for sentiment analysis.")



if (selected == 'Question-Answering'):
    st.header("Question-Answering")
    context = st.text_area("Context:")
    question = st.text_input("Question:")

    if context and question:
        conversation = Conversation()
        conversation.add_message("user", f"Answer the following question only output answer, nothing else:\nQuestion: {question}\nContext: {context}")

        chat_response = chat_completion_request(
            conversation.conversation_history,
            # functions = None
        )

        output = json.loads(chat_response.text)

        # Display the output
        if output['choices']:
            content = output['choices'][0]['message']['content']
            st.markdown("## Output:")
            st.info(content)
    elif not context:
        st.warning("Please provide the context.")
    elif not question:
        st.warning("Please provide the question.")


if (selected == 'NER'):
    st.header("Named Entity Recognition")

    user_input = st.text_input("Enter Sentence:", key='input')

    if user_input:
        conversation = Conversation()
        conversation.add_message("user", f"Do named entity recognition in the given sentence and provide the type of entity. Only output the recognized entities, nothing extra:\n{user_input}")

        chat_response = chat_completion_request(
            conversation.conversation_history,
            # functions = None
        )

        output = json.loads(chat_response.text)

        # Display the output
        if output['choices']:
            recognized_entities = output['choices'][0]['message']['content']
            
            st.subheader("Input Sentence:")
            st.info(user_input)
            
            st.subheader("Recognized Entities:")
            st.success(recognized_entities)
    else:
        st.info("Please enter a sentence for named entity recognition.")


if (selected == 'Text Summarization'):
    st.header("Text Summarization")
    
    user_input = st.text_input("Enter Text:", key='input')
    
    if user_input:
        conversation = Conversation()
        conversation.add_message("user", f"For the given text, provide the best summary as output, nothing extra:\n{user_input}")

        chat_response = chat_completion_request(
            conversation.conversation_history,
            # functions = None
        )

        output = json.loads(chat_response.text)

        # Display the output
        if output['choices']:
            summary = output['choices'][0]['message']['content']
            
            st.subheader("Input Text:")
            st.info(user_input)
            
            st.subheader("Summary:")
            st.success(summary)
    else:
        st.info("Please enter a text for text summarization.")


if (selected == 'Translation'):
    st.header("Translation")
    input_col, languages_col = st.columns([2, 1])

    user_input = input_col.text_input("You:", key='input')
    if user_input:
        conversation = Conversation()
        languages = [
            "English", "Spanish", "French", "German", "Italian", "Russian", "Chinese",
            # Add more languages here...
        ]
        # Languages selection
        selected_languages = languages_col.multiselect("Select Languages", languages)

        if not selected_languages:
            st.warning("Please select at least one language.")
        else:
            language = ', '.join(selected_languages)  # Join selected languages into a string

            conversation.add_message("user", f"Translate this sentence to {language} only output the translation, nothing else: {user_input}")
            chat_response = chat_completion_request(
                conversation.conversation_history,
                # functions = None
            )

            output = json.loads(chat_response.text)

            # Display the output
            if output['choices']:
                content = output['choices'][0]['message']['content']
                st.markdown("## Output:")
                st.info(content)
    else:
        st.warning("Please enter a sentence to translate.")


if (selected == 'Grammar Check'):
    st.header("Grammar Check")
    
    user_input = st.text_input("Enter Text:", key='input')
    
    if user_input:
        conversation = Conversation()
        conversation.add_message("user", f"Check the grammar and spelling and correct them. Return only the original sentence with corrected grammar and spelling, nothing extra:\n{user_input}")

        chat_response = chat_completion_request(
            conversation.conversation_history,
            # functions = None
        )

        output = json.loads(chat_response.text)

        # Display the output
        if output['choices']:
            corrected_sentence = output['choices'][0]['message']['content']
            
            st.subheader("Original Sentence:")
            st.info(user_input)
            
            st.subheader("Corrected Sentence:")
            st.success(corrected_sentence)
    else:
        st.info("Please enter a text for grammar check.")


if (selected == 'POS'):
    st.header("Parts of Speech Tagging")

    user_input = st.text_input("Enter Sentence:", key='input')

    if user_input:
        conversation = Conversation()
        conversation.add_message("user", f"Please provide the parts of speech tagging for the following sentence. Only output the POS tags like this example Everything is all about money.\
        Output: [('Everything', 'NN'), ('is', 'VBZ'), \
          ('all', 'DT'),('about', 'IN'), \
          ('money', 'NN'), ('.', '.')] after this also specify what NN means explain for all and your input is this : {user_input}")

        chat_response = chat_completion_request(
            conversation.conversation_history,
            # functions = None
        )

        output = json.loads(chat_response.text)

        # Display the output
        if output['choices']:
            pos_tags = output['choices'][0]['message']['content']
            
            st.subheader("Input Sentence:")
            st.info(user_input)
            
            st.subheader("Parts of Speech Tags:")
            st.success(pos_tags)
    else:
        st.info("Please enter a sentence for parts of speech tagging.")
