import streamlit as st
from summerizer import summerizer

def main():
    st.title("Text Summarization App")

    # Input text paragraph from user
    user_input = st.text_area("Enter the text paragraph you want to summarize:")

    # Check if user provided input
    if st.button("Summarize"):
        if user_input:
            # Call your summarization function here and get the summarized text
            summarized_text = summerizer(user_input) 
            st.subheader("Summarized Text:")
            st.write(summarized_text)
        else:
            st.warning("Please enter a text paragraph.")

if __name__ == "__main__":
    main()