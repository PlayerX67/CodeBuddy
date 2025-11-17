import streamlit as st
import ollama
import time

st.set_page_config(page_title="Your Private Coding AI", page_icon="🤖", layout="wide")

st.title("🤖 Your Private Coding AI Assistant")
st.caption("Running DeepSeek-Coder-V2 16B locally on Render • 100% private • No data leaves this instance")

# Model warming
if 'ready' not in st.session_state:
    with st.spinner("Warming up the 16B coding model (first start takes ~2-3 min)..."):
        for _ in range(10):
            try:
                ollama.list()
                st.session_state.ready = True
                break
            except:
                time.sleep(10)
    st.success("Model ready!")

if 'messages' not in st.session_state:
    st.session_state.messages = []

# Chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
if prompt := st.chat_input("Ask me to code, debug, explain, or refactor anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = ollama.chat(model='deepseek-coder-v2:16b', messages=[
                {
                    'role': 'system',
                    'content': 'You are an expert coding assistant. Be precise, helpful, and format code properly.'
                },
                {
                    'role': 'user',
                    'content': prompt
                }
            ])
            answer = response['message']['content']
            st.markdown(answer)
            st.session_state.messages.append({"role": "assistant", "content": answer})
