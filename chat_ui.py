import streamlit as st

def message_display(text, is_user=False):
  if is_user:
    avatar_url = "https://i.ibb.co/XjRF0xF/user.png"
    message_alignment = "flex-end"
    message_bg_color = "linear-gradient(135deg, #00B2FF 0%, #006AFF 100%)"
    avatar_class = "user-avatar"
    st.write(
      f"""
        <div style="display: flex; align-items: center; margin-bottom: 10px; justify-content: {message_alignment};">
          <div style="background: {message_bg_color}; color: white; border-radius: 20px; padding: 10px; margin-right: 5px; max-width: 75%;">
            {text}
          </div>
          <img src="{avatar_url}" class="{avatar_class}" alt="user" width="50" height="50" />

        </div>
      """, 
      unsafe_allow_html=True
    ) 

  else:
    avatar_url = "https://i.ibb.co/kXXytK7/robot.png"
    message_alignment = "flex-start"
    message_bg_color = "#71797E"
    avatar_class = "bot-avatar"
    st.write(
      f"""
        <div style="display: flex; align-items: center; margin-bottom: 10px; justify-content: {message_alignment};">
          <img src="{avatar_url}" class="{avatar_class}" alt="robot" width="50" height="50" />
          <div style="background: {message_bg_color}; color: white; border-radius: 20px; padding: 10px; margin-left: 5px; margin-bottom: 30px; max-width: 75%;">
            {text} \n
          </div>
        </div>
      """, 
      unsafe_allow_html=True
    )  

def reset_chat_history():
  st.session_state["generated"] = ["Hey there, I'm PDF Bot, ready to chat up on any questions you might have regarding the documents you have uploaded."]
  st.session_state["past"] = ["Hi..."]
  st.session_state["conversation"] = []
  st.session_state["messages"] = [("Hello! I'm a chatbot designed to help you with pdf documents.")]