import vertexai
import os
from vertexai.preview.language_models import TextGenerationModel
from vertexai.generative_models import GenerativeModel, SafetySetting
import vertexai.generative_models as generative_models
from app import schemas
from fastapi import HTTPException
import re


parameters_gemini = {
    "max_output_tokens": 8192,
    "temperature": 0.1,
    "top_p": 0.95,
}

safety_settings_gemini = [
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
        threshold=SafetySetting.HarmBlockThreshold.BLOCK_ONLY_HIGH,
    ),
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
        threshold=SafetySetting.HarmBlockThreshold.BLOCK_ONLY_HIGH,
    ),
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
        threshold=SafetySetting.HarmBlockThreshold.BLOCK_ONLY_HIGH,
    ),
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_HARASSMENT,
        threshold=SafetySetting.HarmBlockThreshold.BLOCK_ONLY_HIGH,
    ),
]


prompts_folder = os.getenv("PROMPT_FOLDER", "/app/prompts")


def load_prompt_template(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        prompt_template = file.read()
    return prompt_template


def get_prompt(prompt_template, **params):
    return prompt_template.format(**params)


def initialize_vertex_ai():
    PROJECT_ID = os.getenv("PROJECT_ID")
    vertexai.init(project=PROJECT_ID, location="us-central1")


def generate_text_with_gemini(prompt: str):
    gemini_model = GenerativeModel("gemini-1.5-flash-001")
    responses = gemini_model.generate_content(
        prompt,
        generation_config=parameters_gemini,
        safety_settings=safety_settings_gemini,
        stream=True,
    )
    full_response = "".join([response.text for response in responses])
    return full_response
