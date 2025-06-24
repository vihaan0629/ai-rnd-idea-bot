import streamlit as st
from idea_generator import generate_rnd_ideas

st.title("💡 AI R&D Idea Generator")

query = st.text_input("Describe your R&D challenge:")

if st.button("Generate Ideas") and query:
    with st.spinner("Generating ideas..."):
        ideas = generate_rnd_ideas(query)
        for i, idea in enumerate(ideas, 1):
            st.markdown(f"### Idea Set {i}\n{idea}")

