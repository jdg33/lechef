pip install openai
pip install streamlit

import openai
import streamlit as st

# Set up your OpenAI API key
api_key = "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"
openai.api_key = api_key

def chat_with_model(messages):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages
    )
    return response.choices[0].message['content']

def generate_random_recipe():
    response = chat_with_model([
        {"role": "system", "content": "You are a French recipe bot. Include ingredients, cooking instructions, and related notes/tips at the end. Please make sure to include a title and description. Format neatly with headers"},
        {"role": "user", "content": "Generate a random recipe."}
    ])
    return response

def generate_recipe_with_input(idea, diet, allergies, time_constraint):
    response = chat_with_model([
        {"role": "system", "content": "You are a French recipe bot. Include ingredients, cooking instructions, and related notes/tips at the end. Please make sure to include a title and description. Format neatly with headers"},
        {"role": "user", "content": f"My idea for a recipe is {idea}. My diet is {diet}, I have allergies to {allergies}, and I have {time_constraint} to make a meal. Generate a recipe."}
    ])
    return response

st.title("Frankie Smokes")

option = st.radio("Choose Option", ("Generate Random Recipe", "Generate Recipe with Input"))

if option == "Generate Random Recipe":
    if st.button("Generate Recipe"):
        recipe = generate_random_recipe()
        st.text(f"Your new recipe:\n{recipe}")

elif option == "Generate Recipe with Input":
    idea = st.text_input("Do you have any idea what you might want to eat? If you have no clue, leave this blank.")
    diet = st.text_input("What diet do you have? (e.g. vegetarian, vegan, etc.)")
    allergies = st.text_input("What allergies do you have? (comma-separated list, or none)")
    time_constraint = st.text_input("How long do you have to make a meal? (e.g. 30 minutes)")

    if st.button("Generate Recipe"):
        recipe = generate_recipe_with_input(idea, diet, allergies, time_constraint)
        st.text(f"Your new recipe:\n{recipe}")
