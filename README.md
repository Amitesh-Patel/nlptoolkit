# TextAI API

The TextAI API is a powerful tool for performing various text
operations and analysis. It allows you to process text input and extract
valuable insights using a wide range of Natural Language Processing
(NLP) techniques. With TextAI, you can perform operations such as
translation, parts of speech tagging, sentiment analysis, question and
answering, text summarization, semantic textual similarity, grammatical
error correction, and topic modeling.


## Getting Started

To get started with the TextAI API, follow the steps below:

1.  Enter  our website [TextAI](https://merconlptoolkit-kyqzsyybbs.streamlit.app/).
2.  Install the required dependencies for your programming language or
    environment.
3.  Make requests to the API endpoints described in the documentation
    below.
    
# API Endpoints

# Translate

Endpoint: '/translate'

Method: 'POST'

## Request Parameters
| Parameter | Type | Description |
|----------|----------|----------|
| text   | string | The text to be translatedt   |
| source_lang   | string   | The language code of the source text.   |
| target_lang   | string   | The language code of the target text.   |

## Response

A JSON object containing the translated text.


# Parts of Speech

Endpoint: '/pos'

Method: 'POST'

## Request Parameters

  |Parameter | Type | Description |
  |----------|------|-------------|
  | text     | string| The text to analyze.|
  
## Response

A JSON object containing a list of tuples where each tuple represents a
word and its corresponding parts of speech.

# Sentiment Analysis

Endpoint: '/sentiment'

Method: 'POST'

## Request Parameters
  | Parameter | Type | Description |
  |-----------|------|-------------|
  | text      |string | Text to analyze |
  
## Response

A JSON object containing the sentiment analysis results such as
sentiment score and sentiment label.

# Question Answering

Endpoint: '/qna'

Method: 'POST'

## Request Parameters

 | Parameter | Type | Description |
  |-----------|------|-------------|
  | passage      |string | Context Passage of text |
  | question | string | The question ask about the text |
  

## Response

A JSON object containing the answer to the question based on the
provided text.

# Text Summarization

[Endpoint: '/summarize'

Method: 'POST'

## Request Parameters
 | Parameter | Type | Description |
  |-----------|------|-------------|
  | text      |string | Text to summarize |
  

## Response

A JSON object containing the summary of the text.

# Semantic Textual Similarity
Endpoint: '/similarity'
Method: 'POST'

## Request Parameters
 | Parameter | Type | Description |
  |-----------|------|-------------|
  | text-1      |string | First text for comparison |
   | text-2      |string | Second text for comparison |
  
## Response
A JSON object containing the similarity score of the two texts.

# Grammatical Error Correction

Endpoint: '/grammatical_error_correction'

Method: 'POST'

## Request Parameters
 | Parameter | Type | Description |
  |-----------|------|-------------|
  | text      |string | The text to correct the grammatical errors.|

    "choices": [
        {
            "finish_reason": "stop",
            "index": 0,
            "message": {
                "content": "positive",
                "role": "assistant"
            }
        }
    ],
    "created": 1688305534,
    "id": "chatcmpl-7XrgMhHcmDJuQASXnqPzLCP0KmjTe",
    "model": "gpt-3.5-turbo-0613",
    "object": "chat.completion",
    "usage": {
        "completion_tokens": 1,
        "prompt_tokens": 34,
        "total_tokens": 35
    }
    
This would be the main response and the the main content will be in response json_output["choices"][0]["message"]["content"]

## Response

A JSON object containing the corrected text with grammatical errors
corrected.

# Topic Modeling

Endpoint: '/topic_modeling'

Method: 'POST'


## Request Parameters

| Parameter | Type | Description |
  |-----------|------|-------------|
  | text      |string | The text to extract topics from |
   | num_topics     |int | Number of topics to extract |
   
## Response

A JSON object containing the  extracted topics from the text.

# Error Handling

If an error occurs during the API request, you will receive a JSON
response with an ]{.c13 .c3}[appropriete]{.c13 .c3}[ error message and
status code.

# Rate Limiting

The TextAI API imposes rate limits to ensure fair usage and server
availability. Please refer to our website for more information on rate
limits and pricing plans.

## Conclusion

The TextAI API provides a comprehensive suite of NLP capabilities for
your text processing needs. Whether you want to translate text, analyze
sentiment, summarize articles, correct grammatical errors, or perform
other advanced operations, TextAI has got you covered. Get started today
and unlock the power of NLP!.
