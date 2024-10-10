from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


# --------------------------------------------------------
# Test Case: test_read_main
# --------------------------------------------------------
# Purpose: Test the main route of the API to ensure the welcome message is returned correctly.
# Input: A GET request to the /v1/ endpoint.
# Expected Output:
# - Status Code: 200 OK
# - Response Body: {"message": "Welcome to the Medlm World!"}
def test_read_main():
    response = client.get("/v1/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Medlm World!"}


# --------------------------------------------------------
# Test Case: test_delete_appointment
# --------------------------------------------------------
# Purpose: Test deleting an appointment report by its ID.
# Input: A DELETE request to /v1/appointment-report/795a708b-e788-4ae2-b097-a2fa9d813690/
# Expected Output:
# - Status Code: 200 OK
# - Response Body: {"message": "Appointment report deleted successfully"}
def test_delete_appointment():
    response = client.delete(
        "/v1/appointment-report/795a708b-e788-4ae2-b097-a2fa9d813690/"
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Appointment report deleted successfully"}
    assert (
        client.get(
            "/v1/appointment-report/795a708b-e788-4ae2-b097-a2fa9d813690/"
        ).status_code
        == 404
    )


# --------------------------------------------------------
# Test Case: test_delete_appointment_not_found
# --------------------------------------------------------
# Purpose: Test attempting to delete an appointment report that does not exist.
# Input: A DELETE request to /v1/appointment-report/1/
# Expected Output:
# - Status Code: 404 Not Found
# - Response Body: {"detail": "Appointment report not found"}
def test_delete_appointment_not_found():
    response = client.delete("/v1/appointment-report/1/")
    assert response.status_code == 404
    assert response.json() == {"detail": "Appointment report not found"}


# --------------------------------------------------------
# Test Case: test_post_appointment_report
# --------------------------------------------------------
# Purpose: Test creating a new appointment report with the provided data.
# Input: A POST request to /v1/appointment-report with a JSON payload:
# {
#   "appointment_id": "795a708b-e788-4ae2-b097-a2fa9d813690",
#   "doctor_observation": "7",
#   "triage_information": "2"
# }
# Expected Output:
# - Status Code: 200 OK
# - Response Body: Contains the "appointment_id", a "None" definitive diagnosis,
#   and a list of differential diagnoses.
def test_post_appointment_report():
    response = client.post(
        "/v1/appointment-report/",
        json={
            "appointment_id": "795a708b-e788-4ae2-b097-a2fa9d813690",
            "doctor_observation": "7",
            "triage_information": "2",
        },
    )
    assert response.status_code == 200
    response_json = response.json()
    assert response_json["id"] == "795a708b-e788-4ae2-b097-a2fa9d813690"
    assert response_json["definitive_diagnosis"] is None
    assert len(response_json["differential_diagnosis"]) > 0


# --------------------------------------------------------
# Test Case: test_get_appointment_report
# --------------------------------------------------------
# Purpose: Test getting a single appointment report with data.
# Input: A GET request to /v1/appointment-report/{appointment_id}/
# Expected Output:
# - Status Code: 200 OK
# - Response Body: Contains the "appointment_id", a "None" definitive diagnosis,
#   and a list of differential diagnoses.


def test_get_single_appointment():
    response = client.get(
        "/v1/appointment-report/795a708b-e788-4ae2-b097-a2fa9d813690/"
    )
    assert response.status_code == 200
    response_json = response.json()
    assert response_json["id"] == "795a708b-e788-4ae2-b097-a2fa9d813690"
    assert response_json["definitive_diagnosis"] is None
    assert len(response_json["differential_diagnosis"]) > 0


# --------------------------------------------------------
# Test Case: test_put_appointment_report
# --------------------------------------------------------
# Purpose: Test updating an appointment report with new data.
# Input: A PUT request to /v1/appointment-report/{appointment_id}/ with a JSON payload:
# {
#   "appointment_id": "795a708b-e788-4ae2-b097-a2fa9d813690",
#   "doctor_observation": "hola a todos",
#   "triage_information": "el triage importante que tenemos"
# }
# Expected Output:
# - Status Code: 200 OK
# - Response Body: Contains the "appointment_id", a "None" definitive diagnosis,
#   and a list of differential diagnoses.
def test_put_appointment_report():
    response = client.put(
        "/v1/appointment-report/795a708b-e788-4ae2-b097-a2fa9d813690/",
        json={
            "appointment_id": "795a708b-e788-4ae2-b097-a2fa9d813690",
            "doctor_observation": "hola a todos",
            "triage_information": "el triage importante que tenemos ",
        },
    )
    assert response.status_code == 200
    response_json = response.json()
    assert response_json["id"] == "795a708b-e788-4ae2-b097-a2fa9d813690"
    assert response_json["definitive_diagnosis"] is None
    assert len(response_json["differential_diagnosis"]) > 0


# --------------------------------------------------------
# Test Case: test_put_appointment_report_not_found
# --------------------------------------------------------
# Purpose: Test updating an appointment report that does not exist.
# Input: A PUT request to /v1/appointment-report/1/ with a JSON payload:
# {
#   "appointment_id": "795a708b-e788-4ae2-b097-a2fa9d813690",
#   "doctor_observation": "hola a todos",
#   "triage_information": "el triage importante que tenemos"
# }
# Expected Output:
# - Status Code: 404 Not Found
# - Response Body: {"detail": "Appointment report not found"}
def test_put_appointment_report_not_found():
    response = client.put(
        "/v1/appointment-report/1/",
        json={
            "appointment_id": "795a708b-e788-4ae2-b097-a2fa9d813690",
            "doctor_observation": "hola a todos",
            "triage_information": "el triage importante que tenemos ",
        },
    )
    assert response.status_code == 404
    assert response.json() == {"detail": "Appointment report not found"}
