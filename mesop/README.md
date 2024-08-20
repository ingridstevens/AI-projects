# Mesop Chat Applications

This repository contains multiple chat applications built using the Google Mesop framework along with different model integrations. Each application provides a web-based chat interface with distinct backend setups for generating responses.

## Introduction to Google Mesop

**Google Mesop** is a framework designed for building and deploying interactive web applications with integrated chat functionalities. It allows developers to create pages that can host chatbots or interactive agents, managing user interactions and providing a seamless experience.

## Applications Overview

### 1. `ollama_app.py`

This application demonstrates a chat interface using the `ollama` library with the `llama3` model. It leverages Mesop to create a web-based chat experience where users can interact with the model. The application streams responses from the model and displays them in real-time.

**Key Features:**
- Integration with the `ollama` library.
- Real-time streaming of responses from the `llama3` model.
- Web-based chat interface created with Mesop.

**To Run:**
```bash
mesop ollama_app.py
```

### 2. ollama_langchain_app.py
This script integrates LangChain's Ollama with Mesop to provide a chat interface. It uses LangChain’s capabilities to interact with the llama3 model, handling message history and generating responses based on user inputs. The application is set up to deliver a chat experience through a web page.

**Key Features:**
- Utilizes LangChain’s Ollama for interacting with the llama3 model.
- Constructs message history and streams responses using LangChain.
- Web-based chat interface managed by Mesop.

**To Run:**
```bash
mesop ollama_langchain_app.py
```

### 3. lmstudio_langchain_app.py
This application integrates LangChain’s OpenAI model with Mesop, specifically using LM Studio for model inference. It sets up a chat interface that interacts with the LM Studio model to generate responses. The application is designed to work with a local LM Studio inference server.

**Key Features:**

Uses LangChain’s OpenAI model with LM Studio for inference.
Constructs message history and streams responses.
Configured for local deployment with LM Studio.

**To Run:**

```bash
mesop lmstudio_langchain_app.py
```

### Getting Started

**Clone the Repository:**
    
```bash
git clone https://github.com/ingridstevens/AI-projects
cd AI-projects/mesop
```
**Install Dependencies:**

Make sure you have Python 3.12 installed. Install the required packages using:

```bash
pip install -r requirements.txt
```


### Run the Applications:

To start any of the applications, use the following command with the respective script:

```bash
mesop ollama_app.py
mesop ollama_langchain_app.py
mesop lmstudio_langchain_app.py
```

### Contributing
Feel free to open issues or submit pull requests if you have suggestions or improvements for these applications.
