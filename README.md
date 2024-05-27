# Movie Name Generator

![Movie Name Generator](https://github.com/cxx5208/Movie-name-generator/assets/76988460/96e6c9bd-f395-4373-8b36-f4b19cec1984)

## Overview

The Movie Name Generator leverages large language models (LLMs) to generate creative and unique movie names. This project integrates state-of-the-art natural language processing techniques to produce engaging movie titles based on user input or predefined prompts.

## Features

- **Advanced Language Model Integration**: Utilizes advanced language models to generate high-quality movie names.
- **Customizable Prompts**: Users can input custom prompts to tailor the generated movie names.
- **Streamlined Workflow**: Efficient and straightforward pipeline for generating and retrieving movie names.

## Technical Specifications

### Architecture

The architecture of the Movie Name Generator is designed to be modular and scalable, consisting of the following components:

1. **Input Module**: Handles user inputs and predefined prompts.
2. **Processing Module**: Integrates with language models to process inputs and generate movie names.
3. **Output Module**: Formats and displays the generated movie names.

### Requirements

The project dependencies are managed via `requirements.txt`. Ensure all dependencies are installed to maintain compatibility and functionality.

```plaintext
openai
langchain
google-search-results
streamlit
```

### Setup and Installation

1. **Clone the Repository**

   ```sh
   git clone https://github.com/cxx5208/Movie-name-generator-using-LLM.git
   cd Movie-name-generator-using-LLM
   ```

2. **Create a Virtual Environment**

   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**

   ```sh
   pip install -r requirements.txt
   ```

### Configuration

Ensure you have the necessary API keys configured for OpenAI and Google Search Results. Create a `.env` file in the root directory and add your API keys:

```plaintext
OPENAI_API_KEY=your_openai_api_key
GOOGLE_SEARCH_API_KEY=your_google_search_api_key
```

### Usage

To generate movie names, run the following command:

```sh
streamlit run MovieNameGenerator/app.py
```


