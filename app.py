import openai
import PyPDF2
import streamlit as st

# Set your OpenAI API key
openai.api_key = "Your_OpenAI_Key"

# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    text = ""
    try:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        for page in pdf_reader.pages:
            text += page.extract_text()
    except Exception as e:
        st.error(f"Error reading PDF: {e}")
    return text

# Function to send a prompt to the LLM
def send_prompt_to_llm(pdf_text, user_prompt):
    # Combine PDF content and user prompt for context
    combined_prompt = f"""
    The following is the content of a PDF document:
    {pdf_text}

    Based on this document, answer the following question or perform the requested task:
    {user_prompt}
    """
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": combined_prompt}
            ],
            max_tokens=1000,
            temperature=0.7,
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Error communicating with the LLM: {e}"

# Streamlit UI
def main():
    st.title("📄 PDF Analysis with OpenAI")
    st.write("Upload a PDF, choose a task, and let the AI generate a detailed report for you.")

    # File uploader
    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
    
    # Prompt selection
    prompts = [
        "Summarize the key points in this document.",
        "What are the main findings or conclusions in this document?",
        "Generate a detailed report based on this document.",
        "List any statistical data or figures mentioned in the document.",
        "Extract any actionable recommendations or suggestions.",
    ]
    prompt_choice = st.selectbox("Select a task:", prompts)
    custom_prompt = st.text_input("Or enter your custom prompt (optional):")
    
    # Use custom prompt if provided
    final_prompt = custom_prompt if custom_prompt.strip() else prompt_choice

    # Button to generate report
    if st.button("Generate Report"):
        if uploaded_file is not None:
            # Extract text from the PDF
            with st.spinner("Extracting text from the PDF..."):
                pdf_text = extract_text_from_pdf(uploaded_file)
            
            if not pdf_text.strip():
                st.error("The PDF appears to be empty or could not be read.")
                return
            
            # Send prompt to the LLM
            with st.spinner("Generating report with AI..."):
                report = send_prompt_to_llm(pdf_text, final_prompt)
            
            # Display the generated report
            st.subheader("Generated Report:")
            st.write(report)
        else:
            st.error("Please upload a PDF file first.")

if __name__ == "__main__":
    main()
