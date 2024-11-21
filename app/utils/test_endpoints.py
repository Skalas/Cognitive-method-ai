import requests
import subprocess

# List of questions
questions = [
    "Tengo un equipo de 12 jugadores, tienen entre 5 y 6 años, que tipos de ejercicios de técnica me puedes recomendar?",
    "Tengo un equipo cuyas edades están entre 5 y 6 años, que tipos de ejercicios de técnica me puedes recomendar?",
    "cuál es la capital de francia?",
]

# The URL for the API endpoint
url = "https://metodocognitivo-262720144455.us-central1.run.app"

# Run the gcloud command to get the identity token
result = subprocess.run(
    ["gcloud", "auth", "print-identity-token"],
    capture_output=True,
    text=True,
    check=True,
)

# Capture the identity token from the result
identity_token = result.stdout.strip()

# Loop through each question and make the POST request
for question in questions:
    print(f"Sending question: {question}")

    try:
        response = requests.post(
            f"{url}/v1/generate-training",  # Using https as required
            json={"question": question},
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {identity_token}",
            },
        )

        # If the request is successful, print the response JSON
        if response.status_code == 200:
            print(response.json())
        else:
            print(f"Request failed with status code {response.status_code}")
            print(f"Error details: {response.text}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
