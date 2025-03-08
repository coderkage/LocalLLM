import streamlit as st
import ollama

model = "deepseek-r1:7b"

def chat_with_deep(prompt):
    response = ollama.chat(model=model, messages=[{"role": "user", "content": prompt}])
    return response

st.title("DeepDisaster")
st.write("You need anything?")

user_input = st.text_area("Your Message:")

if st.button("Send"):
    if user_input:
        response = chat_with_deep(user_input)
        st.write("### Response:")
        st.write(response["message"]["content"])
    else:
        st.warning("Please enter a message before sending.")
