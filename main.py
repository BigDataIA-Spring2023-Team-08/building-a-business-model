import streamlit as st
import openai 


openai.api_key = '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'

def translate_anything(anything, prompt_lang):
    prompt_base = "Translate this into "
    prompt_col =": "

    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt_base+prompt_lang+prompt_col+"/n/n"+anything,
    temperature=0.3,
    max_tokens=400,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
    )

    translation = response.choices[0].text
    return translation



## page 1 - get recipe from ingredients
def get_recipe_from_ingredients():
    prompt_base = "Write a recipe based on these ingredients and instructions:"
    #st.text(prompt_base)
    #ingredients = ["Apple","Flour","Sugar","Cinnamon"]

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        ingredients_1 = st.selectbox(
        "Select a Protein",
        ('Tuna', 'Chicken', 'Lamb', 'Shrimp'),
        #label_visibility=st.session_state.visibility,
        #disabled=st.session_state.disabled,
        )

    with col2:
        ingredients_2 = st.selectbox(
        "Select a Vegetable",
        ('Asparagus', 'Potato', 'Broccoli', 'Brussel Sprouts'),
        #label_visibility=st.session_state.visibility,
        #disabled=st.session_state.disabled,
        )
    
    with col3:
        ingredients_3 = st.selectbox(
        "Select a Spice",
        ('Chillies', 'Oregano', 'Thyme', 'Rosemary'),
        #label_visibility=st.session_state.visibility,
        #disabled=st.session_state.disabled,
        )
    
    with col4:
        ingredients_4 = st.selectbox(
        "Select a Carb",
        ('Rice','Flour', 'Pasta'),
        #label_visibility=st.session_state.visibility,
        #disabled=st.session_state.disabled,
        )



    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt_base+": /n"+ingredients_1+"/n"+ingredients_2+"/n"+ingredients_3+"/n"+ingredients_4,
    temperature=0.3,
    max_tokens=300,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
    )

    recipe = response.choices[0].text


    #translation 
    language = st.radio(
    "Set Language for Recipe",
    ('English','French', 'Spanish', 'Japanese'))

    if language == 'English':
        pass
    else:
        with st.spinner("Translating..."):
            recipe=translate_anything(recipe,language)

    #print(recipe+"/n /n")
    st.write(recipe)

## ad generator
def ad_generator():

    prompt_base = "Write a creative ad for the following restaurant: "
    text_input = st.text_input(
        "Enter Name of restaurant and some description about your business! 👇")

    if text_input:
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt_base + text_input,
        temperature=0.5,
        max_tokens=100,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
        )

        ad = response.choices[0].text
        st.write(ad)

def review_sentiment():

    prompt_base = "Decide whether a Tweet's sentiment is positive, neutral, or negative.\n\n Tweet:"
    text_input = st.text_input(
        "Enter a review about a restaurant you recently visited👇")

    if text_input:
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt_base + text_input,
        temperature=0.5,
        max_tokens=100,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
        )

        review_sent = response.choices[0].text
        st.write(review_sent)



# main functionality begins here

page = st.sidebar.selectbox("Select a page", ["Recipe Ideas", "Generate a Restaurant Ad", "Get Review Sentiment"])   #main options of streamlit app

if page == "Recipe Ideas":
    with st.spinner("Loading..."): #spinner element
        get_recipe_from_ingredients()
elif page == "Generate a Restaurant Ad":
    with st.spinner("Loading..."): #spinner element
        ad_generator()
elif page == "Get Review Sentiment":
    with st.spinner("Loading..."): #spinner element
        review_sentiment()