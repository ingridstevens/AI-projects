import ollama
import mesop as me
import mesop.labs as mel
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

@me.page(
    security_policy=me.SecurityPolicy(
        allowed_iframe_parents=["https://google.github.io"]
    ),
    path="/",
    title="Mesop Demo Chat",
)
def page():
    mel.chat(transform, title="Ollama Chat", bot_user="Mesop Bot")

def transform(input: str, history: list[mel.ChatMessage]):
    messages = [{"role": "user", "content": message.content} for message in history]
    messages.append({"role": "user", "content": input})
    
    stream = ollama.chat(model='llama3', messages=messages, stream=True)
    
    for chunk in stream:
        content = chunk.get('message', {}).get('content', '')
        if content:
            yield content

if __name__ == "__main__":
    me.run()