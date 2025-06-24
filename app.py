import streamlit as st
from idea_generator import generate_rnd_ideas

st.set_page_config(page_title="AI R&D Idea Generator", page_icon="💡")

st.title("💡 AI R&D Idea Generator")
st.markdown("A simple AI bot that suggests **innovative ideas** for your R&D challenges.")

query = st.text_input("🔍 Describe your research or development challenge:")

if st.button("Generate Ideas") and query:
    with st.spinner("Thinking..."):
        ideas = generate_rnd_ideas(query)
        st.success("Here are some ideas:")
        for idx, idea in enumerate(ideas, 1):
            st.markdown(f"**Idea {idx}:** {idea}")
