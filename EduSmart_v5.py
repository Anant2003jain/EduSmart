#python -m streamlit run EduSmart_v5.py

import streamlit as st
from Edufeatures import *
import time
#from streamlit_custom_notification_box import custom_notification_box

def stream_answer():
    for word in answer.split(" "):
        yield word + " "
        time.sleep(0.02)

def stream_summary():
    for word in summary.split(" "):
        yield word + " "
        time.sleep(0.02)

def stream_quiz():
    for word in quiz.split(" "):
        yield word + " "
        time.sleep(0.02)

if __name__ == "__main__":

    # Set page title and favicon
    st.set_page_config(
        page_title="EduSmart 🎓",
        page_icon="te_logo.png",
        layout="wide",
        initial_sidebar_state="auto"
    )
    
    # Streamlit Interface
    st.title("EduSmart 🎓")
    st.subheader("AI-Powered Learning Hub")


    # Check if uploaded file is stored in session state
    if 'uploaded_file' not in st.session_state:
        st.session_state.uploaded_file = None
    
    uploaded_file = st.file_uploader("Upload your PDF file", type=["pdf"])

    if uploaded_file is not None:
        st.session_state.uploaded_file = uploaded_file  # Store the uploaded file in session state

    # Proceed only if the file is uploaded and saved in session state
    if st.session_state.uploaded_file is not None:
        try:
            # Check if extracted text is already stored in session state
            if 'extracted_text' not in st.session_state:
                with st.spinner("Please wait, we are reading your file..."):                
                    extracted_text = extract_text_from_pdf(st.session_state.uploaded_file)
                    st.session_state.extracted_text = extracted_text  # Store extracted text in session state

            extracted_text = st.session_state.extracted_text

            if extracted_text:
                st.write("Let's start our study! Be focused 😊")

                # Buttons to clear chat history, regenerate summary, and regenerate quiz
                with st.sidebar:
                    #st.image("te_logo.png", width=100)
                    st.title("EduSmart 🎓")
                    
                    st.markdown("""
                        **Welcome to EduSmart!**
                        Your AI-Powered Learning Hub that reads your PDFs and generates summaries, quizzes, and real-time Q&A.
                        
                        ### Features:
                        - 📄 Read and Understand document
                        - 📝 Summarization
                        - ❓ Quiz Generation
                        - 💬 Real-Time Q&A
                    """)
                    
                    st.divider()
                    st.write("")
                    if st.button("Re-Summarize"):
                        if 'summary' in st.session_state:
                            del st.session_state.summary  # Delete existing summary

                    if st.button("Re-Quiz"):
                        if 'quiz' in st.session_state:
                            del st.session_state.quiz  # Delete existing quiz

                    # Clear Chat History, Re-Summarize, Re-Quiz buttons
                    if st.button("Clear Chat History"):
                        st.session_state.chat_history = []

                # Inject custom CSS for centered tabs and larger text
                
                st.markdown("""
                    <style>
                        .stTabs [role="tablist"] {
                            justify-content: center;  /* Centers the tabs */
                            font-size: 50px; /* Increase tab text size */
                        }
                        
                        .stTabs [role="tab"] {
                            font-size: 500px; /* Increase tab text size */
                            font-weight: bold;
                            padding: 10px;
                        }

                        /* Optional: Adding background and hover effects */
                        .stTabs [role="tab"]:hover {
                            background-color: #f0f0f0;
                            color: #333;
                        }
                    </style>
                    """, unsafe_allow_html=True)

                # Tabs content
                tab1, tab2, tab3 = st.tabs(["Summary", "Quiz", "Real-Time QnA"])


                # Summarization
                with tab1:
                    if 'summary' not in st.session_state:
                        if st.button("Generate Summary"):
                            with st.spinner("Generating summary..."):
                                summary = summarize_text(extracted_text)
                                if summary:
                                    st.session_state.summary = summary
                                    st.success("Summary generated successfully!")
                                    st.write_stream(stream_summary)
                    else:
                        st.write(st.session_state.summary)
        

                # Quiz Generation
                with tab2:
                    if 'quiz' not in st.session_state:
                        if st.button("Generate Quiz"):
                            with st.spinner("Generating quiz..."):
                                quiz = generate_quiz(extracted_text)
                                if quiz:
                                    st.session_state.quiz = quiz
                                    st.success("Quiz generated successfully!")
                                    st.write_stream(stream_quiz)
                    else:
                        st.write(st.session_state.quiz)

                # Real-time Q&A    
                with tab3:
                    try:
                        st.info("Please Open Sidebar from top left to chat.")
                        # Initialize chat history in session state
                        if 'chat_history' not in st.session_state:
                            st.session_state.chat_history = []

                        # Display previous chat messages
                        for message in st.session_state.chat_history:
                            with st.chat_message(message['role']):
                                st.write(message['content'])

                        # Use chat_input for new question input
                        if user_input := st.sidebar.chat_input("Ask a question about the content:"):
                            # User's message
                            st.session_state.chat_history.append({'role': 'user', 'content': user_input})
                            
                            try:
                                # Display user's question in the chat
                                with st.chat_message('user'):
                                    st.write(user_input)

                                # AI's response
                                with st.spinner("Processing your question..."):
                                    answer = ask_question(user_input, extracted_text)
                                    if answer:
                                        st.session_state.chat_history.append({'role': 'assistant', 'content': answer})
                                        
                                        # Display AI's answer in the chat
                                        with st.chat_message('assistant'):
                                            st.write_stream(stream_answer)
                    
                            except Exception as e:
                                st.write("Any problem occured, please re submit your question!")

                    except Exception as e:
                                st.write("Any problem occured, please re submit your question!")


        except Exception as e:
            st.error("An error Occurred!!!")
            st.error(f"Error Message:\n\n{e}")

    else:
        st.info("Please upload a PDF file to begin.")
