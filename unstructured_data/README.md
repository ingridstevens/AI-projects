# Unstructured Data Extraction 
Use Case: Competitor Intelligence Data Extraction

## Overview

This project demonstrates how to extract structured data from unstructured text, specifically focusing on competitor intelligence data in the bakery industry.

## Use Case

![baked_goods](img/sweets.jpeg)

Imagine you own a bakery and your confectioner intelligence team gathers competitor data. This project helps analyze unstructured information, providing insights into competitor offerings, advantages, and products mentioned, allowing you to prioritize business strategies.

## Quick Start

1. **Clone Repository:**
   ```bash
   git clone https://github.com/ingridstevens/AI-projects.git
   cd competitor-intelligence
2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt

3. **Run the Notebook:**
   ```bash
   jupyter notebook
   ```
   Then open `unstructured_extraction_chain.ipynb` or `unstructured_pydantic.ipynb` in a browser.


## Usage

## Note on OpenAI
This project uses the OpenAI API to generate text. You will need to create an account and get an API key to use it. You can get an API key here: [here](https://platform.openai.com/api-keys). 

When you have your API key, store it in a file called `.env` in the root directory of this project. Please rename the `example.env` file to `.env`. The file should look like this:
```
OPENAI_API_KEY=your-api-key-here
```

## Alternatives to OpenAI
If you don't want to use OpenAI, you can use a different language model. You can use any language model that works with LangChain. You can find a list of models [here](https://python.langchain.com/docs/models).

I would recommend using Ollama, which is available for Mac and Linux. You can find instructions for installing Ollama [here](https://ollama.ai).

When you've downloaded Ollama, you can install models via the command line. For example, to install mistral, run `ollama run mistral` (~4GB)

In the code, change where it says `OpenAI()` to `Ollama(model='mistral')`.

For more information on Ollama within Langchain, see [LangChain's Ollama LLM Documentation](https://python.langchain.com/docs/integrations/llms/ollama).

## Data: 
I've provided a sample of competitive intelligence data in `data.csv`. It currently has 6 rows, and the columns are MONTH, INTEL, REPORTER, and RESPONSIBLE. The INTEL column contains unstructured text, and the other columns are metadata.

## Two Paths:
This project demonstrates two paths to extract structured data from unstructured text: using the `extraction_chain` or using the `PydanticOutputParser`, both from LangChain.

Please see this [Documentation about Extraction from LangChain](https://python.langchain.com/docs/use_cases/extraction) for more information.

### Define Schema:
Identify the structure to extract, including competitor name, offering, advantage, mentioned product, and additional details.

### Create Extraction Chain / or Pydantic Output Parser Class:
Use LangChain's create_extraction_chain and a language model to create an extraction chain based on the defined schema.
Alternatively, use the PydanticOutputParser class to create a parser based on the defined schema. (see each respective notebook for more details)

### Run the Chain:
Apply the chain to examples or real data to get structured outputs.

### Apply to Real Data:
Load a CSV with competitive intelligence, pass it through the extraction chain, and add the parsed information back into the original data.

## Dependencies
Python 3.11
OpenAI + API Key
LangChain
Pandas
NumPy
Jupyter Notebook

## License
This project is licensed under the MIT License - see the LICENSE file for details.