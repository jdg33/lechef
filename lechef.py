import openai
import streamlit as st
import time

# Set up your OpenAI API key
api_key = st.secrets["OAPI"]
openai.api_key = api_key

def chat_with_model(messages):
    response = openai.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=messages
    )
    return response.choices[0].message.content

def generate_random_recipe():
    response = chat_with_model([
        {"role": "system", "content": "You are a recipe bot. Include ingredients, cooking instructions, and related notes/tips at the end. Please make sure to include a title and description. Format neatly with headers"},
        {"role": "user", "content": "Generate a random recipe."}
    ])
    return response

def generate_recipe_with_input(diet, allergies, req, cuisine, meal, time_constraint, audience):
    response = chat_with_model([
        {"role": "system", "content": "You are a recipe bot. Include ingredients, cooking instructions, and related notes/tips at the end. Please make sure to include a title and description. Format neatly with headers"},
        {"role": "user", "content": f"My diet is {diet}, I have allergies to {allergies}, I have {time_constraint} to make a meal, I must use {req} in this meal, I prefer to eat {cuisine} for this meal. I will be eating this for {meal}. I will be cooking this for {audience} people. Generate a recipe."}
    ])
    return response

def generate_recipe_with_idea(idea):
    response = chat_with_model([
        {"role": "system", "content": "You are a recipe bot. Include ingredients, cooking instructions, and related notes/tips at the end. Please make sure to include a title and description. Format neatly with headers"},
        {"role": "user", "content": f"My rough idea for a meal is {idea}. Generate a recipe from that."}
    ])
    return response

st.title("What to cook, what to cook...")

option = st.radio("Choose your option", ("Generate Recipe with Variables","Generate Random Recipe", "Generate Recipe from an Idea"))

if option == "Generate Recipe with Variables":
    diet = st.text_input("Do you want to adhere to any specific diets? (e.g. vegetarian, no red meat, paleo, keto, etc.)")
    allergies = st.text_input("What allergies do you have? (comma-separated list, or none)")
    req = st.text_input("Are there any ingredients you definitely want to use?")
    cuisine = st.text_input("Preference on cuisine type (Italian, Chinese, American, Etc)?")
    meal = st.selectbox('Is this for a specific meal of the day?',('Does not matter!','Breakfast','Lunch','Dinner','Dessert'))
    time_constraint = st.selectbox('How long do you want to spend making this meal?',('15 minutes','30 minutes','45 minutes','1 hour','More than hour'))
    audience = st.selectbox('How many people are you cooking for?',('1','2','3','4','5','6'))

    if st.button("Generate Recipe"):
        with open("RECIPESTEXT.txt", "a") as text_file:
            with st.spinner('Preparing your recipe...'):
                recipe = generate_recipe_with_input(diet, allergies, req, cuisine, meal, time_constraint, audience)
                st.write(f"Your new recipe:\n{recipe}")
                text_file.write("\n\n\n" + recipe + "\n\n\n")

elif option == "Generate Random Recipe":
    if st.button("Generate Recipe"):
        with open("/lechef/main/RECIPESTEXT.txt", "a") as text_file:
            with st.spinner('Preparing your recipe...'):
                recipe = generate_random_recipe()
                st.write(f"Your new recipe:\n{recipe}")
                text_file.write("\n\n\n" + recipe + "\n\n\n")


elif option == "Generate Recipe from an Idea":
    idea = st.text_input("What are you interested in making?")

    if st.button("Generate Recipe"):
        with open("RECIPESTEXT.txt", "a") as text_file:
            with st.spinner('Preparing your recipe...'):
                recipe = generate_recipe_with_idea(idea)
                st.write(f"Your new recipe:\n{recipe}")
                text_file.write("\n\n\n" + recipe + "\n\n\n")
                
