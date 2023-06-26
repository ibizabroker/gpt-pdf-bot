import streamlit as st

form_remove_border = r'''
  <style>
    [data-testid="stForm"] {border: 0px}
  </style>
'''

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

  # with st.form(key='my_form'):
  query = st.text_input(
    label="Query", 
    key="input", 
    value="", 
    placeholder="Ask your question here...",
    label_visibility = "hidden"
  )

  # st.markdown(form_remove_border, unsafe_allow_html=True)
  with st.sidebar:
    st.subheader("Your documents")
    pdfs = st.file_uploader("Upload your PDFs here and click 'Upload to DB'", accept_multiple_files=True)
    st.button("Upload to DB")

if __name__ == '__main__':
  main()