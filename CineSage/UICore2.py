import streamlit as st

from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from pydantic import BaseModel
from typing import List, Optional
from langchain_core.output_parsers import PydanticOutputParser


load_dotenv()

model = ChatGroq(
    model="openai/gpt-oss-20b"
)


class Movie(BaseModel):
    title: str
    release_year: Optional[int]
    genre: List[str]
    director: Optional[str]
    cast: List[str]
    rating: Optional[float]
    summary: str


parser = PydanticOutputParser(pydantic_object=Movie)


prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
Extract movie information from the paragraph

{format_instructions}
"""
    ),
    (
        "human",
        "{paragraph}"
    )
])


# ---------------- Streamlit UI ----------------

st.set_page_config(
    page_title="Movie Information Extractor",
    page_icon="🎬"
)

st.title("🎬 Movie Information Extractor")

para = st.text_area(
    "Enter Movie Paragraph",
    height=250,
    placeholder="Give your movie paragraph here..."
)

if st.button("Extract Information", use_container_width=True):

    if para.strip():

        final_prompt = prompt.invoke({
            "paragraph": para,
            "format_instructions": parser.get_format_instructions()
        })

        response = model.invoke(final_prompt)

        st.subheader("Movie Information")

        st.write(response.content)

    else:
        st.warning("Please enter a movie paragraph.")