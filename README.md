<h1 align="center">
  <br>
  PDF Bot: Your Intelligent PDF Assistant
</h1>

<p align="center"> 
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
  </a>
  <a href="https://python.langchain.com/docs/get_started/introduction.html">
    <img src="https://img.shields.io/badge/-%F0%9F%A6%9C%EF%B8%8F%F0%9F%94%97_LangChain-000000?style=flat-square" alt="LangChain">
  </a>
  <a href="https://openai.com/">
    <img src="https://img.shields.io/badge/-OpenAI-412991?style=flat-square&logo=openai&logoColor=white" alt="OpenAI">
  </a>
  <a href="https://streamlit.io/">
    <img src="https://img.shields.io/badge/-Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white" alt="Streamlit">
  </a>
  <a href="https://docs.pinecone.io/docs/overview/">
    <img src="https://img.shields.io/badge/Pinecone-FFFFFF?style=flat-square&logo=data:image/png;base64,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" alt="Pinecone">
  </a>
</p>

<p align="center">
  <a href="#overview">Overview</a>
  •
  <a href="#installation">Installation</a>
  •
  <a href="#instructions-to-use">Instructions to Use</a>
  •
  <a href="#contribution">Contribution</a>
</p>

# Overview
PDF Bot is an advanced AI-powered bot designed to assist you with questions and queries related to PDF documents. Leveraging the power of OpenAI's GPT model, PDF Bot offers a seamless experience for users seeking information and insights from their PDF files. Whether you have a single file or multiple documents, PDF Bot is here to help.

# Installation
- Clone this branch: `git clone --single-branch --branch pinecone https://github.com/ibizabroker/gpt-pdf-bot.git`
- Create a virtual environment
```
$ pip install virtualenv
$ virtualenv venv
$ .\venv\Scripts\activate
```
- Once your virtual environment is activated, install the required pacakges: `pip install -r requirements.txt`
- Run the streamlit app in an activated virtual environment: `streamlit run bot.py`

# Instructions to Use
- Enter your openai and [pincone](https://www.pinecone.io/) keys in the text input.
- In pinecone create an index named `storage`, select `cosine` and give the dimensions as `1536`.
- You can either drag and drop or browse files to upload pdfs, after the pdfs have been uploaded press on `Upload to DB` for it to get embedded.
- Start chatting with the bot :)

![Hosting Screenshot](screenshot/pinecone.png)

# Contribution
Feel free to open an issue or submit a pull request. Your feedback and suggestions are greatly appreciated :)

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.