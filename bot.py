import streamlit as st
from ingest import create_vector_db

def main():
  st.set_page_config(
    page_title="PDF Bot",
    page_icon=":robot_face:",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items={
      'Report a bug': "https://github.com/ibizabroker/gpt-pdf-bot",
      'About': '''PDF Bot is a chatbot designed to help you answer questions from pdfs. It is built using OpenAI's GPT, chromadb and Streamlit. 
               To learn more about the project go to the GitHub repo. https://github.com/ibizabroker/gpt-pdf-bot 
               '''
    }
  )

  st.title("PDF Bot")
  st.caption("Easily chat with pdfs.")

  messages_container = st.container()

  query = st.text_input(
    label="Query", 
    key="input", 
    value="", 
    placeholder="Ask your question here...",
    label_visibility = "hidden"
  )

  with st.sidebar:
    st.subheader("Your documents")
    pdfs = st.file_uploader(
      "Upload your PDFs here and click 'Upload to DB'", 
      type=['pdf'],
      accept_multiple_files=True
    )
    if pdfs is not None:
      for pdf in pdfs:
        with open(pdf.name, "wb") as f:
          f.write(pdf.getbuffer())

    if st.button("Upload to DB"):
      with st.spinner("Processing"):
        vector_store = create_vector_db()

        st.write("Processing Done")

if __name__ == '__main__':
  main()