from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from secret_key import openapi_key

import os
os.environ['OPENAI_API_KEY'] = openapi_key

llm = OpenAI(temperature=0.7)

def generate_movie_name_and_tags(language):
    # Chain 1: Movie Name in English
    prompt_template_name = PromptTemplate(
        input_variables=['language'],
        template="I want to make a movie. Suggest a fancy name for this."
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="movie_name_english")

    # Chain 2: Translate Movie Name to the selected language
    prompt_template_translate = PromptTemplate(
        input_variables=['movie_name_english', 'language'],
        template="Translate the movie name '{movie_name_english}' to {language}."
    )

    translate_chain = LLMChain(llm=llm, prompt=prompt_template_translate, output_key="movie_name_translated")

    # Chain 3: Movie Tags
    prompt_template_items = PromptTemplate(
        input_variables=['movie_name_english'],
        template="Suggest some movie titles for {movie_name_english}. Return it as a comma separated string."
    )

    tags_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="movie_tags")

    chain = SequentialChain(
        chains=[name_chain, translate_chain, tags_chain],
        input_variables=['language'],
        output_variables=['movie_name_english', 'movie_name_translated', 'movie_tags']
    )

    response = chain({'language': language})

    return response

if __name__ == "__main__":
    print(generate_movie_name_and_tags("Telugu"))
