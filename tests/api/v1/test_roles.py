from uuid import uuid4
from json import dumps


def test_get_roles(client):
    response = client.get('/api/v1/roles')
    assert response.status_code == 200
    role_names = [role["name"] for role in response.json]
    assert set(["admin", "owner", "developer"]).issubset(role_names)


def test_get_existing_role(client):
    response = client.get('/api/v1/roles/developer')
    assert response.status_code == 200
    assert response.json["name"] == "developer"
    assert "permissions" in response.json


def test_get_nonexistent_role(client):
    response = client.get('/api/v1/roles/puppy')
    assert response.status_code == 404


def test_create_user(client):
    user_id = str(uuid4())
    response = client.post(
        "/api/v1/users",
        content_type="application/json",
        data=dumps({"id": user_id, "atat_role": "ccpo"}),
    )
    assert response.status_code == 200
    assert response.json["id"] == user_id
    assert response.json["atat_role"] == "ccpo"


def test_update_user(client):
    user_id = str(uuid4())
    client.post(
        "/users",
        content_type="application/json",
        data=dumps({"id": user_id, "atat_role": "ccpo"}),
    )
    response = client.put(
        "/users/{}".format(user_id),
        content_type="application/json",
        data=dumps({"atat_role": "developer"}),
    )
    assert response.status_code == 200
    assert response.json["id"] == user_id
    assert response.json["atat_role"] == "developer"


def test_update_nonexistent_user(client):
    user_id = str(uuid4())
    response = client.put(
        "/users/{}".format(user_id),
        content_type="application/json",
        data=dumps({"atat_role": "developer"}),
    )
    assert response.status_code == 404


def test_update_user_with_nonexistent_role(client):
    user_id = str(uuid4())
    client.post(
        "/users",
        content_type="application/json",
        data=dumps({"id": user_id, "atat_role": "ccpo"}),
    )
    response = client.put(
        "/users/{}".format(user_id),
        content_type="application/json",
        data=dumps({"atat_role": "invalid_role"}),
    )
    assert response.status_code == 404

def test_update_workspace_user_roles(client):
    workspace_id = str(uuid4())
    user1_id = str(uuid4())
    user2_id = str(uuid4())

    new_workspace_users = [
        {"id": user1_id, "workspace_role": "developer"},
        {"id": user2_id, "workspace_role": "owner"},
    ]

    response = client.put(
        '/api/v1/workspaces/{}/users'.format(workspace_id),
        content_type='application/json',
        data=dumps({"users": new_workspace_users}))
    assert response.status_code == 200
    assert response.json[0]['atat_role'] == 'developer'
