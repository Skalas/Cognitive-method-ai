import requests

print(requests.get("http://localhost:8000/v1/").json())


print(
    requests.post(
        "http://localhost:8000/v1/generate-training",
        json={"question": "What is the capital of France?"},
    ).json()
)
