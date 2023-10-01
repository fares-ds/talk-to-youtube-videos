from langchain.llms import OpenAI
from dotenv import load_dotenv

load_dotenv()

def generate_pet_name():
    llm = OpenAI(temperature=0.7)
    prompt = "I have a dog pet and I want a cool name for it. suggest five cool names for my pet."
    names = llm(prompt=prompt)
    return names

if __name__ == "__main__":
    print(generate_pet_name())
