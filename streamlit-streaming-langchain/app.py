####
#### Streamlit Streaming using LM Studio as OpenAI Standin
#### run with `streamlit run app.py`

# !pip install pypdf langchain langchain_openai 

import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

# app config
st.set_page_config(page_title="LM Studio Streaming Chatbot", page_icon="🤖")
st.title("LM Studio Streaming Chatbot")

def get_response(user_query, chat_history):

    template = """
    You are a helpful assistant. Use the chat history if it helps, otherwise ignore it:

    Chat history: {chat_history}

    User response: {user_question}
    """

    prompt = ChatPromptTemplate.from_template(template)

    # Using LM Studio Local Inference Server
    llm = ChatOpenAI(base_url="http://localhost:1234/v1")

    chain = prompt | llm | StrOutputParser()
    
    return chain.stream({
        "chat_history": chat_history,
        "user_question": user_query,
    })

# session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        AIMessage(content="Hello, I am a bot. How can I help you?"),
    ]

    
# conversation
for message in st.session_state.chat_history:
    if isinstance(message, AIMessage):
        with st.chat_message("AI"):
            st.write(message.content)
    elif isinstance(message, HumanMessage):
        with st.chat_message("Human"):
            st.write(message.content)

# user input
user_query = st.chat_input("Type your message here...")
if user_query is not None and user_query != "":
    st.session_state.chat_history.append(HumanMessage(content=user_query))

    with st.chat_message("Human"):
        st.markdown(user_query)

    with st.chat_message("AI"):
        response = st.write_stream(get_response(user_query, st.session_state.chat_history))

    st.session_state.chat_history.append(AIMessage(content=response))