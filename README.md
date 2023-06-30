<h1 align="center">
  <br>
    PDF Bot: Your Intelligent PDF Assistant
  <br>
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
- Clone the repository: `git clone https://github.com/ibizabroker/gpt-pdf-bot.git`
- Create a virtual environment
```
$ pip install virtualenv
$ virtualenv venv
$ .\venv\Scripts\activate
```
- Once your virtual environment is activated, install the required pacakges: `pip install -r requirements.txt`
- Create a `.env` file in the working directory. Copy the contents of [.env.example](.env.example) and fill it with your openai key.
- Run the streamlit app in an activated virtual environment: `streamlit run bot.py`

# Instructions to Use
- The repository has a [sample pdf](pdfs/Intro%20to%20environment.pdf), which has already been embedded in vector form using [chroma db](db).
- You can either drag and drop or browse files to upload pdfs, after the pdfs have been uploaded press on 'Upload to DB' for it to get embedded.
- Start chatting with the bot :)

![Example Screenshot](screenshot/example.png)

# Contribution
Feel free to open an issue or submit a pull request. Your feedback and suggestions are greatly appreciated :)

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.