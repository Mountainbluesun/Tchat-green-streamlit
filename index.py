import streamlit as st
from datetime import  datetime

from pydeck.widget.debounce import debounce
from streamlit_autorefresh import st_autorefresh

st.set_page_config(page_title="Chat Nature")

@st.cache_resource
def get_message_store():
    return list()

messages = get_message_store()
st_autorefresh(interval=2000, limit=None, key="chat", debounce=True)


st.title("Nature Mountain")

if "username" not in st.session_state:
    st.session_state.username = ""

if not st.session_state.username:
    username_input = st.text_input("Enter you pseudo : ")
    if st.button("Join") and username_input:
        st.session_state.username = username_input
        messages.append(
            {
                "author": "System",
                "text": f"{username_input} - joined !",
                "time": datetime.now().strftime("%H:%M:%S")
            }
        )
        st.rerun()
else:
    st.success(f"{st.session_state.username} is online")

    for msg in messages:
        with st.chat_message(msg["author"]):
            st.markdown(f"*{msg["time"]})* - {msg["text"]}")

    input_chat = st.chat_input("Type your message....")
    if input_chat:
        messages.append({
            "author": st.session_state.username,
            "text": input_chat,
            "time": datetime.now().strftime("%H:%M:%S")
        })





