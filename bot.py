import streamlit as st
import pinecone
from langchain.vectorstores.pinecone import Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
from ingest import create_vector_db
from chain import get_conversation_chain
from chat_ui import message_display, reset_chat_history

def load_chain(openai_api_key, pinecone_api_key, pinecone_env_key):
  embeddings = OpenAIEmbeddings(
    openai_api_key=openai_api_key
  )

  pinecone.init(
    api_key=pinecone_api_key,
    environment=pinecone_env_key
  )
  index_name = "storage"

  db = Pinecone.from_existing_index(index_name, embeddings)

  return get_conversation_chain(db, openai_api_key)

def execute_chain(query, openai_api_key, pinecone_api_key, pinecone_env_key):
  chain = load_chain(openai_api_key, pinecone_api_key, pinecone_env_key)
  chain_result = None
  chain_result = chain({
    "question": query
  })

  return chain_result

def main():
  st.set_page_config(
    page_title="PDF Bot",
    page_icon=":robot_face:",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items={
      'Report a bug': "https://github.com/ibizabroker/gpt-pdf-bot",
      'About': '''PDF Bot is a chatbot designed to help you answer questions from pdfs. It is built using OpenAI's GPT, Pinecone and Streamlit. 
               To learn more about the project go to the GitHub repo. https://github.com/ibizabroker/gpt-pdf-bot 
               '''
    }
  )

  with st.sidebar:
    with st.expander("How to use?"):
      st.write("""
        - Enter your openAI api key in the given field.
        - Create a free pinecone account to enter the api and environment keys.

        **To upload your pdfs in the database:**
        - Drag n drop your file in the given section or browse and select your files.
        - Once the files are selected press the button `Upload to DB`.

        **To chat with your document:**
        - Make sure you have entered your keys and there is data ingested in your pinecone database.
        - Ask the question and press `Submit` to get the output.
        - To clear chat history, press the `Reset` button.  
               
        Raise an issue in the [repo](https://github.com/ibizabroker/gpt-pdf-bot) if you have any questions.
      """)
    openai_api_key = st.text_input(
      label="OpenAI API Key", 
      type="password",
      key="openai_api_key", 
      value="", 
      placeholder="sk-...",
    )

    pinecone_api_key = st.text_input(
      label="Pinecone API Key", 
      type="password",
      key="pinecone_api_key", 
      value="", 
      placeholder="Pinecone api key...",
    )

    pinecone_env_key = st.text_input(
      label="Pinecone Environment Key", 
      type="password",
      key="pinecone_env_key", 
      value="", 
      placeholder="Pinecone env key...",
    )

    st.session_state["OPENAI_API_KEY"]=openai_api_key
    st.session_state["PINECONE_API_KEY"]=pinecone_api_key
    st.session_state["PINECONE_ENV_KEY"]=pinecone_env_key

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

        st.session_state.conversation = get_conversation_chain(vector_store, st.session_state["OPENAI_API_KEY"])
        st.write("Processing Done")

  st.title("PDF Bot")
  st.caption("Easily chat with pdfs.")

  messages_container = st.container()

  if "generated" not in st.session_state:
    st.session_state["generated"] = ["Hey there, I'm PDF Bot, ready to chat up on any questions you might have regarding the documents you have uploaded."]
  if "past" not in st.session_state:
    st.session_state["past"] = ["Hey!"]
  if "input" not in st.session_state:
    st.session_state["input"] = ""
  if "stored_session" not in st.session_state:
    st.session_state["stored_session"] = []

  if "messages" not in st.session_state:
    st.session_state["messages"] = [("Hello! I'm a chatbot designed to help you with pdf documents.")]

  c1, c2, c3 = st.columns([6.2, 1, 1])
  with c1:
    query = st.text_input(
      label="Query", 
      key="input", 
      value="", 
      placeholder="Ask your question here...",
      label_visibility = "collapsed"
    )
  
  with c2:
    submit_button = st.button("Submit")

  with c3:
    reset_button = st.button("Reset")

  if reset_button:
    reset_chat_history()

  if len(query) > 1 and submit_button:
    messages = st.session_state['messages']

    result = execute_chain(query, st.session_state["OPENAI_API_KEY"], st.session_state["PINECONE_API_KEY"], st.session_state["PINECONE_ENV_KEY"])

    for i, message in enumerate(result['chat_history']):
      if i % 2 == 0:
        st.session_state.past.append(message.content)
        # print("user:" + message.content)
      else:
        messages.append((query, message.content))
        st.session_state.generated.append(message.content)
        # print("bot:" + message.content)

  with messages_container:
    if st.session_state["generated"]:
      for i in range(len(st.session_state["generated"])):
        message_display(st.session_state["past"][i], is_user=True)
        message_display(st.session_state["generated"][i])

  hide_footer = """
                  <style>
                    footer {visibility: hidden;}
                  </style>
                """
  st.markdown(hide_footer, unsafe_allow_html=True) 

if __name__ == '__main__':
  main()