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


def test_get_workspace_user_roles(client):
    workspace_id = uuid4()
    response = client.get('/api/v1/workspaces/{}/users'.format(workspace_id))
    assert response.status_code == 200


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
    print(response.json)
    assert('owner' in response.json[1]['roles'])
