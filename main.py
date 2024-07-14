import os
import json
import uvicorn
from openai import OpenAI
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException

from src.prompts import *
from src.logger import logger
from src.exceptions import DetailedHTTPException


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)

app = FastAPI()

def story_telling(prompt):
    """
    Generates a story based on the provided prompt using the GPT-3.5 model. 
    Inputs:
        - prompt: The text prompt for generating the story.
    Outputs:
        - The generated story in JSON format.
    """
    response = client.chat.completions.create(
    model="gpt-3.5-turbo-0125", # gpt-4-0125-preview
    messages=[
        {"role": "system", "content": prompt},
        ],
        temperature=1,
        response_format={'type':"json_object"}  
        )

    data = response.choices[0].message.content
    # Directly parse the JSON response
    return json.loads(data)

@app.get("/")
async def root():
    logger.info("Server is up and running")
    return {"message": "Server is up and running"}

class StoryIntroduction(BaseModel):
    story_title: str

@app.post("/story_introduction/")
async def get_story(request: StoryIntroduction):
    try:
        logger.info(f"Story title: {request.story_title}")
        response = story_telling(STORY_INTRODUCTION_SYSTEM_TEMPLATE.format(story_title=request.story_title, example=STORY_INTRODUCTION_EXAMPLE_TEMPLATE))
        logger.info(f"Response: {response}")
        story_line = response['story_line']
        return story_line
    except Exception as e:
        logger.error(str(e))
        raise DetailedHTTPException(status_code=500, detail=str(e))

class StoryTelling(BaseModel):
    story_title: str
    story_introduction: str

@app.post("/story_telling/")
async def get_story(request: StoryTelling):
    try:
        logger.info(f"Story title: {request.story_title}, story introduction: {request.story_introduction}")
        response = story_telling(STORY_TELLING_SYSTEM_TEMPLATE.format(story_title=request.story_title, story_line=request.story_introduction, example=STORY_TELLING_EXAMPLE_TEMPLATE))
        logger.info(f"Response: {response}")
        story = response['story']
        return story
    except Exception as e:
        logger.error(str(e))
        raise DetailedHTTPException(status_code=500, detail=str(e))
    

if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=7000)