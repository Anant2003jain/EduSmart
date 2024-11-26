# EduSmart 🎓

EduSmart is an **AI-powered learning hub** designed to help students and professionals understand, summarize, and quiz themselves on any PDF document. With advanced **AI models** from **Azure** and **OpenAI**, EduSmart provides intelligent features like **summarization**, **quiz generation**, and **real-time Q&A** to make your study sessions more efficient and interactive. 📚✨

## Features 🌟
- **📄 PDF Text Extraction**: Upload any PDF, and EduSmart extracts the text from it.
- **📝 Summarization**: Generate clear, concise summaries of your document to help you grasp key concepts.
- **❓ Quiz Generation**: Create personalized quizzes based on the document’s content to test your knowledge.
- **💬 Real-Time Q&A**: Ask questions about the document and get answers based on its content instantly.
- **📚 AI-Powered**: Utilizes **Azure AI** and **OpenAI** models to ensure the most accurate responses, summaries, and quizzes.

## Getting Started 🚀

### Prerequisites 🔧

To run EduSmart locally, you will need to have the following installed:
- **Python 3.8+**
- **Streamlit**
- **Azure SDK** (Form Recognizer, OpenAI, etc.)
- **Environment variables** configured for Azure services (API keys, endpoints, etc.).

You can create a `.env` file with the following variables:
```plaintext
DOC_ENDPOINT=your_azure_endpoint
DOC_KEY=your_azure_key
LANGUAGE_ENDPOINT=your_language_endpoint
LANGUAGE_KEY=your_language_key
AZURE_OAI_ENDPOINT=your_openai_endpoint
AZURE_OAI_KEY=your_openai_key
AZURE_OAI_DEPLOYMENT=your_openai_model_deployment
```

### Install Dependencies 🛠️
Clone this repository and install the necessary packages:

```bash
git clone https://github.com/Anant2003jain/EduSmart.git
cd EduSmart
pip install -r requirements.txt
```

### Run the Application 🚀
Once the dependencies are installed, you can run the application using Streamlit:

```bash
streamlit run EduSmart_v5.py
```

This will start the app and open it in your default web browser.

## How to Use EduSmart 🖥️

1. **Upload your PDF document**: Click the **Upload PDF** button to select and upload a document.
2. **Generate Summaries**: Once the document is uploaded, you can generate a concise summary of the content. Just click **Generate Summary**.
3. **Create Quizzes**: Generate a quiz from the content by clicking **Generate Quiz**. This will produce a mix of multiple-choice, fill-in-the-blank, and short-answer questions.
4. **Real-Time Q&A**: Ask questions about the document in the **Real-Time Q&A** tab and get immediate answers from the system.

## Screenshots 📸

Here are some screenshots of EduSmart in action:

### 1. **Main Interface**
![EduSmart Main Interface](assets/main_interface.png)

### 2. **Summary Tab**
![Summary Tab](assets/summary_tab.png)

### 3. **Quiz Tab**
![Quiz Tab](assets/quiz_tab.png)

### 4. **Real-Time Q&A Tab**
![Real-Time Q&A](assets/qa_tab.png)

## Video Demonstration 🎥

Check out this video demonstration to see EduSmart in action:

[![EduSmart Demo](https://img.youtube.com/vi/your_video_id/0.jpg)](https://www.youtube.com/watch?v=your_video_id)

## Technologies Used ⚙️

- **Streamlit**: Fast app framework for building beautiful web applications with Python.
- **Azure Form Recognizer**: For extracting text from PDF documents.
- **Azure OpenAI**: For generating summaries, quizzes, and answering questions based on the content.
- **Python**: The core programming language used to build the application.
- **dotenv**: To manage environment variables securely.

## Contributing 🤝

We welcome contributions! If you would like to contribute to EduSmart, follow these steps:

1. Fork this repository.
2. Create a new branch for your changes.
3. Commit your changes and push them to your fork.
4. Open a pull request with a description of what you’ve done.

## License 📄

EduSmart is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements 🙏

- **Azure Cognitive Services** for providing powerful text recognition and AI capabilities.
- **OpenAI** for providing advanced language models for summarization, quiz generation, and Q&A.
- **Streamlit** for making app development easy and fast.


## Connect with Me  
Feel free to star the repository and share your feedback!

For updates, insights, or to connect, feel free to check out my [LinkedIn profile](https://www.linkedin.com/in/anant-jain-1720671a7).
