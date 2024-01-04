# Unstructured Data Extraction with LLMs
Use Case: Competitor Intelligence Data Extraction using Large Language Models

## Overview

This project demonstrates how to extract structured data from unstructured text using Large Language Models. For this demonstration, I'll be specifically focusing on competitor intelligence data in the bakery industry.

## Use Case

![baked_goods](img/sweets.jpeg)

Imagine you own a bakery and your confectioner intelligence team gathers competitor data. This project helps analyze unstructured information, providing insights into competitor offerings, advantages, and products mentioned, allowing you to prioritize business strategies.

## Quick Start

1. **Clone Repository:**
   ```bash
   git clone https://github.com/ingridstevens/AI-projects.git
   cd AI-projects
   cd unstructured_data
   ```
2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt

3. **Run the Notebook:**
   ```bash
   jupyter notebook
   ```
   Then open either the `unstructured_extraction_chain.ipynb` or `unstructured_pydantic.ipynb` in a browser.

   Each notebook takes a slightly different approach to extracting structured data from unstructured inputs. The `unstructured_extraction_chain.ipynb` uses LangChain's `extraction_chain` to extract data, and the `unstructured_pydantic.ipynb` uses LangChain's `PydanticOutputParser` to extract data.


## Notes before We Start

### Note on OpenAI
This project uses the OpenAI API to generate text. You will need to create an account and get an API key to use it. You can [get an API key from OpenAI](https://platform.openai.com/api-keys). 

When you have your API key, store it in a file called `.env` in the root directory of this project. Please rename the `example.env` file to `.env`. The file should look like this:
```
OPENAI_API_KEY=your-api-key-here
```

### Alternatives to OpenAI

Note: if you can find a way to use OpenAI, I would recommend it. It's the easiest way to get started with this project. Otherwise, you will need to find a local model that supports function calling, this is unfortunatelyn not an easy swap.

.... 

If you don't want to use OpenAI, you can use a different language model. You can use any language model that works with LangChain. You can find a list of models [here](https://python.langchain.com/docs/models).


## Useage

### Data: 
I've provided a sample of competitive intelligence data in `data.csv`. The data was generated using ChatGPT and is not real data.
It currently has 6 rows, and the columns are:
* MONTH (the month the intelligence was gathered)
* INTEL (the intelligence)
* REPORTER (the person who gathered the intelligence)
* RESPONSIBLE (the person responsible for acting on the intelligence)

The INTEL column contains unstructured text, and the other columns are metadata.

### Two Paths:
This project demonstrates two paths to extract structured data from unstructured text: using the `extraction_chain` or using the `PydanticOutputParser`, both from LangChain.

Please see this [Documentation about Extraction from LangChain](https://python.langchain.com/docs/use_cases/extraction) for more information.

### Define Schema:
Identify the structure to extract, including competitor name, offering, advantage, mentioned product, and additional details.

### Create Extraction Chain / or Pydantic Output Parser Class:
Use LangChain's create_extraction_chain and a language model to create an extraction chain based on the defined schema.
Alternatively, use the PydanticOutputParser class to create a parser based on the defined schema. (see each respective notebook for more details)

### Run the Chain:
Apply the chain to examples or real data to get structured outputs. You can create a dataframe and export as .csv in order to run a LangChain CSV agent over the data.

### Run the Agent over the Data
Please run this [Notebook about creating the LangChain agent](unstructured_analyze_agent.ipynb) to further analyze the data.

### Taking it Further: Apply this Process to Real Data:
Load a CSV with competitive intelligence, pass it through the extraction chain, and add the parsed information back into the original data.

## Dependencies
```
Python 3.11
OpenAI + API Key
LangChain
Pandas
NumPy
Jupyter Notebook
```

## License
This project is licensed under the MIT License - see the LICENSE file for details.