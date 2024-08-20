import mesop as me
import mesop.labs as mel
from langchain.llms import OpenAI
from mesop import stateclass
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the LM Studio Model Inference Server
llm = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")


@stateclass
class State:
    pass

@me.page(
    security_policy=me.SecurityPolicy(
        allowed_iframe_parents=["https://google.github.io"]
    ),
    path="/",
    title="Mesop Demo Chat",
)
def page():
    mel.chat(transform, title="LangChain Chat using LMStudio for Model Inference", bot_user="LM Studio Mesop Bot")

def transform(input: str, history: list[mel.ChatMessage]):
    # Construct the message history for the Llama3 model
    messages = [f"System: You are a helpful assistant."]
    messages.extend([f"User: {message.content}" for message in history])
    messages.append(f"User: {input}")

    query = "\n".join(messages)
    # Query the Llama3 model and stream the response
    resp = llm.stream(query)
    
    for chunk in resp:
        if chunk:
            yield chunk

if __name__ == "__main__":
    me.run()