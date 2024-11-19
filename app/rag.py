from vertexai.preview import rag
from vertexai.preview.generative_models import GenerativeModel, Tool, SafetySetting
from google.cloud import aiplatform
from vertexai.preview import rag
from vertexai.preview.rag import RagCorpus, RagResource
from google.auth import default
from utils import load_prompt_template, get_prompt
from parameters import (
    PROJECT_ID,
    LOCATION,
    INDEX,
    INDEX_ENDPOINT,
    RAG_CORPORA,
    MODEL_ID,
)
from datetime import datetime

safety_settings_gemini = [
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
        threshold=SafetySetting.HarmBlockThreshold.BLOCK_ONLY_HIGH,
    ),
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
        threshold=SafetySetting.HarmBlockThreshold.OFF,
    ),
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
        threshold=SafetySetting.HarmBlockThreshold.OFF,
    ),
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_HARASSMENT,
        threshold=SafetySetting.HarmBlockThreshold.OFF,
    ),
]

parameters_gemini = {
    "max_output_tokens": 8192,
    "temperature": 0.1,
    "top_p": 0.95,
}


def get_parameters_gemini(query: str) -> str:

    params = {"query": query}
    prompt_path = r"./prompts/filter_parameters.txt"
    prompt_template = load_prompt_template(prompt_path)
    prompt = get_prompt(prompt_template, **params)

    try:
        # Generate the response
        responses = model.generate_content(
            prompt,
            generation_config=parameters_gemini,
            safety_settings=safety_settings_gemini,
            stream=True,
        )

        full_response = "".join([response.text for response in responses])
        # print(f"**** get_parameters_gemini:\n{full_response}")

        return full_response

    except Exception as e:
        print(f"Error in text generation: {e}")


def get_exercises_rag_gemini(parameters: str):

    params = {"parameters": parameters}
    prompt_path = r"./prompts/query_exercises.txt"
    system_prompt = load_prompt_template(prompt_path)

    try:

        rag_corpus = RagCorpus(name=RAG_CORPORA)
        # print(f"**** RAG Corpus loaded: {rag_corpus}")

        rag_resource = RagResource(rag_corpus=rag_corpus.name)
        # print(f"**** RAG Resource loaded: {rag_resource}")

        rag_retrieval_tool = Tool.from_retrieval(
            retrieval=rag.Retrieval(
                source=rag.VertexRagStore(
                    rag_resources=[rag_resource],  # Currently only 1 corpus is allowed.
                    similarity_top_k=5,
                    vector_distance_threshold=0.5,
                ),
            )
        )

        # print(f"**** RAG Retrieval Rool Created: {rag_retrieval_tool}")

        # Create the RAG model using the system prompt and the retrieval tool
        rag_model = GenerativeModel(
            model_name=MODEL_ID,
            generation_config=parameters_gemini,
            tools=[rag_retrieval_tool],
            system_instruction=system_prompt,
        )

        # print(f"**** Rag Model loaded: {rag_model}")

        response = rag_model.generate_content(parameters)

        # print(f"**** response: {response} \n")
        # print(f"**** response: {response.text} \n")
        return response.text

    except Exception as e:
        print(f"Error in text generation: {e}")


if __name__ == "__main__":

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    model = GenerativeModel(MODEL_ID)

    credentials, project = default()
    print(f"**** credentials:{credentials}, project:{project}")

    # Initialize the Vertex AI SDK
    aiplatform.init(project=PROJECT_ID, location=LOCATION, credentials=credentials)

    query = "Tengo un equipo de 10 jugadores, tienen entre 5 y 6 años, que tipos de ejercicios de técnica me puedes recomendar?"
    query = "Tengo un equipo de 12 jugadores, tienen entre 5 y 6 años, que tipos de ejercicios de técnica me puedes recomendar?"

    print(f"**** query: {query}")

    parameters = get_parameters_gemini(query)

    print(f"**** parameters: {parameters}")

    response = get_exercises_rag_gemini(parameters)
    print(f"**** response: {response}")
