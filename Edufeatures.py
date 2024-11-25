import streamlit as st
from openai import AzureOpenAI
from azure.core.exceptions import HttpResponseError
from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
import os
from dotenv import load_dotenv
from docx import Document

# Get configuration settings 
load_dotenv()

doc_endpoint = os.getenv("DOC_ENDPOINT")
doc_key = os.getenv("DOC_KEY")

lang_endpoint = os.getenv("LANGUAGE_ENDPOINT")
lang_key = os.getenv("LANGUAGE_KEY")

oai_endpoint = os.getenv("AZURE_OAI_ENDPOINT")
oai_key = os.getenv("AZURE_OAI_KEY")
oai_model = os.getenv("AZURE_OAI_DEPLOYMENT")
oai_version = os.getenv("AZURE_OAI_VERSION")

# Initialize Azure clients
form_recognizer_client = DocumentAnalysisClient(endpoint=doc_endpoint, credential=AzureKeyCredential(doc_key))
language_client = TextAnalyticsClient(endpoint=lang_endpoint, credential=AzureKeyCredential(lang_key))

# Initialize the Azure OpenAI client
client = AzureOpenAI(
 azure_endpoint = oai_endpoint,
 api_key = oai_key, 
 api_version=oai_version
)

# Function for OCR and text extraction 
#@st.cache_data(show_spinner = False)
def extract_text_from_pdf(file):
    try:
        # Use the "prebuilt-read" model, suitable for general text extraction
        poller = form_recognizer_client.begin_analyze_document("prebuilt-read", document=file)
        result = poller.result()

        extracted_text = ""
        for page in result.pages:
            for line in page.lines:
                extracted_text += line.content + " "
        return extracted_text

    except HttpResponseError as e:
        st.error(f"Error during text extraction: {e}")
        return None
    
    
# Summarize
#@st.cache_data(show_spinner = False)
def summarize_text(text):
    try:
        # Create a system message
        system_message = f"You are a great teacher, Summarize given content in detail. Ensure all topics wrer covered and point out important things from given content."

        # Initialize messages array
        messages_array = [{"role": "system", "content": system_message}]

        # Send request to Azure OpenAI model
        messages_array.append({"role": "user", "content": text})
        
        response = client.chat.completions.create(
        model=oai_model,
        temperature=0.7,
        max_tokens=1200,
        messages=messages_array
        )
        generated_text = response.choices[0].message.content
        # Add generated text to messages array
        messages_array.append({"role": "assistant", "content": generated_text})

        return generated_text

    except Exception as e:
        st.error(f"Error during quiz generation: {e}")
        return None

#@st.cache_data(show_spinner = False)
def generate_quiz(input_text):
    #try:
    # Create a system message
    system_message = f"""Generate 10 quiz questions based on the following content:\n{input_text}.
        Ensure questions are unique each time and increasingly in difficulty from 1 to 10. Give 3 MCQ, 3 Fill in the Blanks, 3 Short Answer typr question, and 1 Long Question. 
        Give all question first, then a list of answers in last.
        Please always take care of output formatting for example:
        Heading:
        MSQs:
            Question 1:
            A) B) C) D)

            Question 2:
            A) B) C) D)

            Question3:
            A) B) C) D)
        
        Fill in the blanks:
            Question 1: 
            Question 2:
            Question 3:

            like that..
            
        Answers:

        Generate quize to prepare them for exams"""

    # Initialize messages array
    messages_array = [{"role": "system", "content": system_message}]

    # Send request to Azure OpenAI model
    messages_array.append({"role": "user", "content": input_text})

    response = client.chat.completions.create(
    model=oai_model,
    temperature=0.7,
    max_tokens=1200,
    messages=messages_array
    )

    generated_text = response.choices[0].message.content
    # Add generated text to messages array

    messages_array.append({"role": "assistant", "content": generated_text})

    return generated_text

#except Exception as e:
    #st.error(f"Error during quiz generation: {e}")
    #return None


# Real-time Q&A function using OpenAI
#@st.dialog("Ask me anything on this topic") #added extra line
#@st.cache_data(show_spinner = False)
def ask_question(question, context):
    try:
        # Create a system message
        system_message = f"Use this content: {context} as a reference and Answer the given question. Please always take care of output formatting, it should be well formatted.\n\n Answer questions that are related to study and education."

        # Initialize messages array
        messages_array = [{"role": "system", "content": system_message}]

        # Send request to Azure OpenAI model
        messages_array.append({"role": "user", "content": question})
        response = client.chat.completions.create(
        model=oai_model,
        temperature=0.7,
        max_tokens=1200,
        messages=messages_array
        )
        generated_text = response.choices[0].message.content
        # Add generated text to messages array
        messages_array.append({"role": "assistant", "content": generated_text})

        return generated_text

    except Exception as e:
        st.error(f"Error during Q&A: {e}")
        return None
    
#Function to save extracted text into a .docx file"""
def save_text_as_docx(text, file_name='extracted_docx_files//textextracted.docx'):
    doc = Document()
    if text!=None:
        for line in text.splitlines():
            doc.add_paragraph(line)
        
        doc.save(file_name)