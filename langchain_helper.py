import os

from langchain_community.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain

if "OPENAI_API_KEY" not in os.environ:
    from keys import openapi_key

    os.environ["OPENAI_API_KEY"] = openapi_key

llm = OpenAI(temperature=0.7)

prompt_template_name = PromptTemplate(
    input_variables=["cuisine"],
    template="I want to open a restaurant for {cuisine} food. Suggest a fancy name for this.",
)

name_chain = LLMChain(
    llm=llm, prompt=prompt_template_name, output_key="restaurant_name"
)

prompt_template_items = PromptTemplate(
    input_variables=["restaurant_name"],
    template="Suggest some menu items for {restaurant_name}. Return the menu items as a single, comma separated string with no additional preamble.",
)

food_items_chain = LLMChain(
    llm=llm,
    prompt=prompt_template_items,
    output_key="menu_items",
)

chain = SequentialChain(
    chains=[name_chain, food_items_chain],
    input_variables=["cuisine"],
    output_variables=["restaurant_name", "menu_items"],
)


def generate_restaurant_name_and_items(cuisine: str) -> dict[str, str]:
    result = chain({"cuisine": cuisine})
    print(result)
    return result

    # return {
    #     "restaurant_name": "Curry Delight",
    #     "menu_items": "Butter Chicken, Naan, Paneer Tikka, Chole Bhature, Lassi, Gulab Jamun",
    # }


if __name__ == "__main__":
    print(generate_restaurant_name_and_items("Singaporean"))
