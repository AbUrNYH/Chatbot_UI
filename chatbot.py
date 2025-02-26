import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage, AIMessage
from sympy import content

base_url="http://127.0.0.1:1234/v1"
api_key="lm-studio"
MODEL = "phi-3-mini-4k-instruct"

LLM = ChatOpenAI(
  openai_api_base = base_url,
  openai_api_key = api_key,
  model_name = MODEL,
  streaming = True
)

st.title("CHATBOT LILY AI")

if "messages" not in st.session_state:
  st.session_state.messages = [
    SystemMessage(content = 'You are a helpful and knowledgeable assistant. Your primary function is to provide accurate and concise answers. Maintain a professional yet friendly tone. When answering technical questions, explain concepts clearly with examples. If the question is unclear, ask for clarification before responding. If a question is outside your knowledge, respond with: \"I currently do not have enough information on that topic.')
  ]
  
  intro_message = HumanMessage(content = "Introduce yourself to someone opening this program for the first time.")
  
  response = LLM.stream([intro_message])
  history_chat = ""
   
  with st.chat_message("assistant"):
    with st.spinner("In Progress..."):
      response_placeholder = st.empty()
      for chunk in response:
        history_chat += chunk.content
        response_placeholder.markdown(history_chat)

for msg in st.session_state.messages:
  if isinstance(msg, HumanMessage):
      with st.chat_message("user"):
        with st.spinner("In Progress..."):
          st.markdown(msg.content)
  elif isinstance(msg, AIMessage):
      with st.chat_message("assistant"):
          st.markdown(msg.content)

user_input = st.chat_input("> ")

if user_input:
  st.session_state.messages.append(HumanMessage(content=user_input))
  
  with st.chat_message("user"):
    st.markdown(user_input)
    
  response = LLM.stream(st.session_state.messages)
  history_chat = ""
  
  with st.chat_message("assistant"):
    response_placeholder = st.empty()
    for chunk in response:
      history_chat += chunk.content
      response_placeholder.markdown(history_chat)
      
  st.session_state.messages.append(AIMessage(content=history_chat))