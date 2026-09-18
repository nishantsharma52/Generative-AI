from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from pydantic import BaseModel
from typing import List,Optional
from langchain_core.output_parsers import PydanticOutputParser

load_dotenv()

model = ChatGroq(
    model="openai/gpt-oss-20b"
)

class Movie(BaseModel):
    title: str
    release_year:Optional[int]
    genre:List[str]
    director:Optional[str]
    cast:List[str]
    rating:Optional[float]
    summary:str

parser = PydanticOutputParser(pydantic_object=Movie)    

prompt = ChatPromptTemplate.from_messages([
    ('system', """
Extract movie information from the paragraph
{format_instructions}
"""),
("human","{paragraph}")]
)

para = input("Give your paragraph: ")

final_prompt = prompt.invoke({
    "paragraph": para,
    'format_instructions': parser.get_format_instructions()
})

response = model.invoke(final_prompt)
movieData = parser.parse(response.content)

print(movieData)