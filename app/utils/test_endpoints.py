import requests

print(requests.get("http://localhost:8000/v1/").json())

questions = [
    "Tengo un equipo de 12 jugadores, tienen entre 5 y 6 años, que tipos de ejercicios de técnica me puedes recomendar?",
    "Tengo un equipo cuyas edades están entre 5 y 6 años, que tipos de ejercicios de técnica me puedes recomendar?",
    "cuál es la capital de francia?",
]
for question in questions:
    print(question)
    print(
        requests.post(
            "http://localhost:8000/v1/generate-training",
            json={"question": question},
        ).json()
    )
