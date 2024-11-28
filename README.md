## 📄 PDF Analysis with OpenAI 📄  
PDF Analysis with OpenAI is a Python-based application that uses OpenAI's GPT-4 model to analyze and generate insights from PDF documents. With a user-friendly Streamlit interface, it allows users to upload a PDF, choose tasks, and receive AI-generated reports in real time.

---

## 🚀 Features  
- **PDF Content Extraction:** Extracts text from uploaded PDF documents using `PyPDF2`.  
- **AI-Powered Insights:** Utilizes OpenAI's GPT-4 for generating summaries, reports, and actionable insights based on the document's content.  
- **Interactive UI:** Built with Streamlit for an intuitive and seamless user experience.  
- **Predefined and Custom Tasks:** Offers a set of predefined tasks and supports user-defined custom prompts.  
- **Error Handling:** Provides clear feedback for issues like empty PDFs or API errors.  

---

## 🛠️ Tech Stack  
- **Language Model:** OpenAI GPT-4  
- **Programming Language:** Python  
- **Frameworks & Libraries:**  
  - [Streamlit](https://streamlit.io/) for UI  
  - [PyPDF2](https://pypi.org/project/PyPDF2/) for PDF text extraction  
  - [OpenAI Python SDK](https://github.com/openai/openai-python) for LLM integration  
- **Deployment:** Local Python environment  

---

## 📋 Requirements  
1. **Python**: Version 3.7 or higher.  
2. **Dependencies**:  
   Install required libraries:  
   ```bash
   pip install streamlit openai PyPDF2
