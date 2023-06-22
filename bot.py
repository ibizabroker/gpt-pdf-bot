import streamlit as st

def main():
  st.set_page_config(page_title="PDF Bot", page_icon=":robot_face:")

  st.header("Chat with multiple pdfs")
  st.text_input("Ask a question about your documents:")

  with st.sidebar:
    st.subheader("Your documents")
    pdfs = st.file_uploader("Upload your PDFs here and click 'Upload to DB'", accept_multiple_files=True)
    st.button("Upload to DB")

if __name__ == '__main__':
  main()