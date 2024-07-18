
# Interactive Storytelling Platform

Flow diagram
![Screenshot 2024-07-18 183930](https://github.com/user-attachments/assets/cd377e0b-4c7c-4b47-b5b1-b85b456e0215)


Welcome to the Interactive Storytelling Platform! This project leverages FastAPI and Streamlit to create an engaging AI-driven storytelling experience. Users can interact with the AI to generate and develop stories dynamically.

Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)

## Introduction
This platform is designed to provide an interactive storytelling experience where users can collaborate with an AI to craft unique narratives. Whether for entertainment, educational purposes, or creative inspiration, our platform offers a versatile tool for all storytelling enthusiasts.

## Features
AI-Powered Story Generation: Leverage advanced AI to generate story introductions and continuations.
Interactive Interface: User-friendly interface built with Streamlit for easy interaction with the AI.
Flexible API: FastAPI backend provides robust endpoints for story generation and management.
Real-Time Interaction: Generate and interact with stories in real-time.

## Installation
To get started with the Interactive Storytelling Platform, follow these steps:

1. Clone the Repository

```
git clone https://github.com/saisubhasish/InteractiveStoryTelling.git
cd InteractiveStoryTelling
```

2. Create a Virtual Environment

```
Conda create -p venv python=3.12 -y
conda activate venv/
```

3. Install Dependencies

```
pip install -r requirements.txt
```

4. Run the Application

```
streamlit run app.py
```

## Usage
Once the application is running, navigate to http://localhost:8000/docs in your web browser. You'll be greeted with the interactive interface where you can start generating and interacting with stories.

## API Endpoints
The platform provides two primary API endpoints:

Story Introduction
Endpoint: (http://localhost:8000/story_introduction)
Method: POST
Description: Generate a story introduction.

Request Body:
```
{
    "story_title": "Write your story title here"
}
```

Response
```
{
    "story_line":"Model's response"
}
```

Story Telling
Endpoint: (http://localhost:8000/story_telling)
Method: POST
Description: Generate a continuation for the given story.
Request Body:
```
{
    "story_title": "Write your story title here",
    "story_line": "Write the modified story introduction here"
}
```

Response
```
{
    "story":"Model's response"
}
```
