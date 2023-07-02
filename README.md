[TextAI API]{.c22 .c33}

[The TextAI API is a powerful tool for performing various text
operations and analysis. It allows you to process text input and extract
valuable insights using a wide range of Natural Language Processing
(NLP) techniques. With TextAI, you can perform operations such as
translation, parts of speech tagging, sentiment analysis, question and
answering, text summarization, semantic textual similarity, grammatical
error correction, and topic modeling.]{.c0}

[]{.c0}

[Getting Started]{.c8}

[To get started with the TextAI API, follow the steps below:]{.c0}

[]{.c0}

1.  [Enter  our website www.textaiapi.com.]{.c0}
2.  [Install the required dependencies for your programming language or
    environment.]{.c0}
3.  [Make requests to the API endpoints described in the documentation
    below.]{.c0}

[]{.c0}

[API Endpoints]{.c9}

[Translate]{.c8}

[Endpoint: ']{.c18 .c3}[/translate]{.c19 .c3}[ ']{.c2}

[Method: ']{.c18 .c3}[POST']{.c19 .c3 .c22}

[Request Parameters]{.c0 .c3}

[]{.c0 .c3}

[]{#t.053a2e3e6c976a5b80c7950f905e95d1ef03e34c}[]{#t.0}

  ------------------------ ------------------- ------------------------------------------------------------------------------------
  [Parameter]{.c0 .c3}     [Type]{.c0 .c3}     [Description]{.c0 .c3}
  [text]{.c0 .c3}          [string]{.c0 .c3}   [The text to be translated]{.c0 .c3}
  [source_lang]{.c0 .c3}   [string]{.c0 .c3}   [The language code of the source text (e.g., \"en\" for English).]{.c0 .c3}
  [target_lang]{.c0 .c3}   [string]{.c0 .c3}   [The language code of the target translation (e.g., \"es\" for Spanish).]{.c0 .c3}
  ------------------------ ------------------- ------------------------------------------------------------------------------------

[]{.c0 .c3}

[]{.c0}

[Response]{.c24 .c22}

[A JSON object containing the translated text.]{.c0}

[]{.c0}

[Parts of Speech]{.c8}

[Endpoint: ']{.c14}[/pos]{.c3 .c19}[']{.c0}

[Method: ']{.c14}[POST]{.c19 .c3}[']{.c0}

[]{.c0}

[Request Parameters]{.c0}

[]{.c0}

[]{#t.6a62312f270b94998e83f74adc18745ddc2bb756}[]{#t.1}

  ------------------ --------------- ----------------------------
  [Parameter]{.c0}   [Type]{.c0}     [Description]{.c0}
  [text]{.c0}        [string]{.c0}   [The text to analyze]{.c0}
  ------------------ --------------- ----------------------------

[]{.c0}

[Response]{.c24 .c22}

[A JSON object containing a list of tuples where each tuple represents a
word and its corresponding parts of speech.]{.c0}

[]{.c0}

[Sentiment Analysis]{.c9}

[Endpoint: ']{.c14}[/sentiment']{.c14 .c20}

[Method: ']{.c14}[POST']{.c20 .c14}

[]{.c20 .c14}

[Request Parameters]{.c0}

[]{.c0}

[]{#t.96781cbf567e2c4ff3d0c1df727b39e44ddbe775}[]{#t.2}

  ------------------ --------------- ------------------------
  [Parameter]{.c0}   [Type]{.c0}     [Description]{.c0}
  [text]{.c0}        [string]{.c0}   [Text to analyze]{.c0}
  ------------------ --------------- ------------------------

[]{.c0}

[Response]{.c22 .c24}

[A JSON object containing the sentiment analysis results such as
sentiment score and sentiment label.]{.c0}

[Question Answering]{.c9}

[Endpoint: ']{.c3 .c18}[qna]{.c3 .c34}[']{.c2}

[Method: ']{.c18 .c3}[POST]{.c34 .c3}[']{.c2}

[]{.c2}

[Request Parameters]{.c2}

[]{.c2}

[]{#t.e026fa930e95b90343132f4837440004a2f43f13}[]{#t.3}

[Parameter]{.c2}

[Type]{.c2}

[Description]{.c2}

[passage]{.c2}

[string]{.c2}

[Context Passage of text]{.c2}

[question]{.c2}

[string]{.c2}

[The question ask about the text]{.c2}

[]{.c2}

[Response]{.c22 .c3 .c23}

[A JSON object containing the answer to the question based on the
provided text.]{.c2}

[]{.c2}

[Text Summarization]{.c22 .c3 .c30}

[Endpoint: ']{.c3 .c27}[/summarize']{.c3 .c11}

[Method: ']{.c13 .c3}[POST']{.c11 .c3}

[]{.c11 .c3}

[Request Parameters]{.c5 .c3}

[]{.c5 .c3}

[]{#t.f7c148a874e93148f73172ff22efc7fb080274b6}[]{#t.4}

  ---------------------- ------------------- ----------------------------------
  [Parameter]{.c5 .c3}   [Type]{.c5 .c3}     [Description]{.c5 .c3}
  [text]{.c5 .c3}        [string]{.c5 .c3}   [The text to summarize]{.c5 .c3}
  ---------------------- ------------------- ----------------------------------

[]{.c5 .c3}

[Response]{.c10 .c3}

[A JSON object containing the summary of the text.]{.c5 .c3}

[]{.c5 .c3}

[Semantic Textual Similarity]{.c22 .c3 .c31}

[Endpoint: ']{.c13 .c3}[/similarity']{.c11 .c3}

[Method: ']{.c3 .c13}[POST']{.c11 .c3}

[]{.c11 .c3}

[Request Parameters]{.c5 .c3}

[]{.c5 .c3}

[]{#t.2ec55e763f437b3a4e2a77c94f2d434803d5a973}[]{#t.5}

  ---------------------- ------------------- -------------------------------------------
  [Parameter]{.c5 .c3}   [Type]{.c5 .c3}     [Description]{.c5 .c3}
  [text-1]{.c5 .c3}      [string]{.c5 .c3}   [The first text for comparison]{.c5 .c3}
  [text-2]{.c5 .c3}      [string]{.c5 .c3}   [The second text for comparison]{.c5 .c3}
  ---------------------- ------------------- -------------------------------------------

[]{.c5 .c3}

[Response]{.c10 .c3}

[A JSON object containing the similarity score of the two texts.]{.c5
.c3}

[]{.c5 .c3}

[Grammatical Error Correction]{.c10 .c3}

[Endpoint: '/grammatical_error_correction']{.c3 .c5}

[Method: 'POST']{.c5 .c3}

[]{.c5 .c3}

[Request Parameters]{.c5 .c3}

[]{.c5 .c3}

[]{#t.d421f120f9ebd053ebe0c7bc6bbbd9bdd783b84b}[]{#t.6}

  ---------------------- ------------------- --------------------------------------------------------
  [Parameter]{.c5 .c3}   [Type]{.c5 .c3}     [Description]{.c5 .c3}
  [text]{.c5 .c3}        [string]{.c5 .c3}   [The text to correct the grammatical errors.]{.c5 .c3}
  ---------------------- ------------------- --------------------------------------------------------

[]{.c5 .c3}

[Response]{.c3 .c10}

[A JSON object containing the corrected text with grammatical errors
corrected.]{.c5 .c3}

[]{.c5 .c3}

[Topic Modeling]{.c31 .c22 .c3}

[Endpoint: '/topic_modeling']{.c5 .c3}

[Method: 'POST']{.c5 .c3}

[]{.c5 .c3}

[Request Parameters]{.c5 .c3}

[]{.c5 .c3}

[]{.c5 .c3}

[]{#t.5f71416d67e90ef52a0d69429a19f4025c79695b}[]{#t.7}

  ----------------------- ------------------- ---------------------------------------------
  [Parameter]{.c5 .c3}    [Type]{.c5 .c3}     [Description]{.c5 .c3}
  [text]{.c5 .c3}         [string]{.c5 .c3}   [The text to extract topics from.]{.c5 .c3}
  [num_topics]{.c5 .c3}   [int]{.c5 .c3}      [Number of topics to extract.]{.c5 .c3}
  ----------------------- ------------------- ---------------------------------------------

[]{.c5 .c3}

[Response]{.c10 .c3}

[A JSON object containing the  extracted topics from the text.]{.c5 .c3}

[]{.c5 .c3}

[]{.c5 .c3}

[Error Handling]{.c21 .c3}

[If an error occurs during the API request, you will receive a JSON
response with an ]{.c13 .c3}[appropriete]{.c13 .c3}[ error message and
status code.]{.c5 .c3}

[]{.c5 .c3}

[Rate Limiting]{.c3 .c21}

[The TextAI API imposes rate limits to ensure fair usage and server
availability. Please refer to our website for more information on rate
limits and pricing plans.]{.c5 .c3}

[]{.c5 .c3}

[Conclusion]{.c21 .c3}

[The TextAI API provides a comprehensive suite of NLP capabilities for
your text processing needs. Whether you want to translate text, analyze
sentiment, summarize articles, correct grammatical errors, or perform
other advanced operations, TextAI has got you covered. Get started today
and unlock the power of NLP!.]{.c13 .c3}

[]{.c5 .c3}

[]{.c5 .c3}
