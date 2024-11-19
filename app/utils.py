from google.auth import default
from googleapiclient.discovery import build
from google.cloud import storage
from googleapiclient.http import MediaIoBaseDownload
import os
import re
import numpy as np


def load_prompt_template(file_path) -> str:
    with open(file_path, "r", encoding="utf-8") as file:
        prompt_template = file.read()
    return prompt_template


def get_prompt(prompt_template, **params) -> str:
    return prompt_template.format(**params)
