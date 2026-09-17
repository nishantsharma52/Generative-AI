import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

load_dotenv()

model = ChatGroq(
    model="openai/gpt-oss-20b"
)

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are a professional Movie Information Extraction Assistant.

Your task:

Extract useful structured information from a movie paragraph and present it in a clean readable format.

Rules:

- Do NOT add explanations
- Do NOT add extra commentary
- Follow the exact format
- If information is missing, write NULL
- Keep summary short (2-3 lines max)
- Do NOT guess unknown facts

Output Format:

Movie Title:

Release Year:

Genre:

Director:

Main Cast:

Setting/Location:

Plot:

Themes:

Ratings:

Notable Features:

Short Summary:
"""
    ),
    (
        "human",
        """
Extract information from this paragraph:

{paragraph}
"""
    )
])


# ---------------- UI ----------------

st.set_page_config(
    page_title="Movie Information Extractor",
    page_icon="🎬",
    layout="centered"
)

st.title("🎬 Movie Information Extractor")
st.write("Enter a movie paragraph to extract structured information.")

para = st.text_area(
    "Movie Paragraph",
    height=250,
    placeholder="Enter your movie paragraph here..."
)

if st.button("Extract Information", use_container_width=True):

    if para.strip():

        final_prompt = prompt.invoke({
            "paragraph": para
        })

        response = model.invoke(final_prompt)

        st.subheader("Extracted Information")
        st.write(response.content)

    else:
        st.warning("Please enter a movie paragraph.")