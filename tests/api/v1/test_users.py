from uuid import uuid4
from json import dumps


def test_create_user(client):
    user_id = str(uuid4())
    response = client.post(
        "/api/v1/users",
        content_type="application/json",
        data=dumps({"id": user_id, "atat_role": "ccpo"}),
    )
    assert response.status_code == 201
    assert response.json["id"] == user_id
    assert response.json["atat_role"] == "ccpo"


def test_create_existing_user(client):
    user_id = str(uuid4())
    client.post(
        "/api/v1/users",
        content_type="application/json",
        data=dumps({"id": user_id, "atat_role": "ccpo"}),
    )
    response = client.post(
        "/api/v1/users",
        content_type="application/json",
        data=dumps({"id": user_id, "atat_role": "ccpo"}),
    )
    assert response.status_code == 200


def test_update_user(client):
    user_id = str(uuid4())
    client.post(
        "/api/v1/users",
        content_type="application/json",
        data=dumps({"id": user_id, "atat_role": "ccpo"}),
    )
    response = client.put(
        "/api/v1/users/{}".format(user_id),
        content_type="application/json",
        data=dumps({"atat_role": "developer"}),
    )
    assert response.status_code == 200
    assert response.json["id"] == user_id
    assert response.json["atat_role"] == "developer"


def test_update_nonexistent_user(client):
    user_id = str(uuid4())
    response = client.put(
        "/api/v1/users/{}".format(user_id),
        content_type="application/json",
        data=dumps({"atat_role": "developer"}),
    )
    assert response.status_code == 404


def test_update_user_with_nonexistent_atat_role(client):
    user_id = str(uuid4())
    client.post(
        "/api/v1/users",
        content_type="application/json",
        data=dumps({"id": user_id, "atat_role": "ccpo"}),
    )
    response = client.put(
        "/api/v1/users/{}".format(user_id),
        content_type="application/json",
        data=dumps({"atat_role": "invalid_role"}),
    )
    assert response.status_code == 404
