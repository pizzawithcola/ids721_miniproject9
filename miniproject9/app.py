import streamlit as st
from transformers import pipeline

# Load the model pipeline
text_generation_pipeline = pipeline("text-generation", model="EleutherAI/gpt-neo-125M")

# Define the Streamlit app
def main():
    st.sidebar.title("Navigation")
    option = st.sidebar.selectbox("Go to", ("Chatbot", "Website Description"))
    st.sidebar.write("\n\n IDS721 miniproject 9 of Jamie Liu")
    st.sidebar.write("©️All rights reserved 2024")


    if option == "Chatbot":
        # Add logo image to the center of the page
        st.image("DukeLogo.png", width=100)

        st.title("Jamie's ChatBox")
        st.write("This app uses the GPT-Neo model for text generation.")

        # User input for text prompt
        max_chars = 100  # Maximum number of characters allowed in the input box
        user_input = st.text_input("You:", "", max_chars)

        # Generate text based on user input
        if st.button("Send"):
            if user_input:
                # Generate response using GPT-Neo
                response = text_generation_pipeline(user_input, max_length=100)[0]["generated_text"]

                # Display response in a chat-like format
                st.text_area("Jamie's Chatbox:", value=response, height=300, max_chars=max_chars, key="generated_text")
            else:
                st.warning("Please enter a message.")
    elif option == "Website Description":
        st.title("Website Description")
        st.image("LLM.png", width=500)
        st.write("This is a streamlit LLM app with hugging face model. It can be quite funny sometimes since it is just a local model but it's fun!")
        st.write("Check https://github.com/pizzawithcola/ids721_miniproject9/tree/main for the source data!")

if __name__ == "__main__":
    main()
