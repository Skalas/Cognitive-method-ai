#!/bin/bash

# Lista de preguntas
questions=(
    "Tengo un equipo de 12 jugadores, tienen entre 5 y 6 años, que tipos de ejercicios de técnica me puedes recomendar?"
    "Tengo un equipo cuyas edades están entre 5 y 6 años, que tipos de ejercicios de técnica me puedes recomendar?"
    "cuál es la capital de francia?"
)

# URL del endpoint
url="https://metodocognitivo-262720144455.us-central1.run.app"

# Obtener el token de identidad de Google Cloud
identity_token=$(gcloud auth print-identity-token)

# Verificar si se obtuvo el token correctamente
if [ -z "$identity_token" ]; then
    echo "No se pudo obtener el token de identidad."
    exit 1
fi

# Iterar sobre cada pregunta
for question in "${questions[@]}"; do
    echo "Enviando pregunta: $question"

    # Realizar la solicitud POST
    response=$(curl -s -X POST "$url/v1/generate-training" \
        -H "Content-Type: application/json" \
        -H "Authorization: Bearer $identity_token" \
        -d "{\"question\":\"$question\"}")

    # Verificar si la solicitud fue exitosa
    if [ $? -eq 0 ]; then
        echo "Respuesta: $response"
    else
        echo "Error al realizar la solicitud"
    fi
done
