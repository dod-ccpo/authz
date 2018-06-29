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


def test_update_workspace_user_roles_with_invalid_role(client):
    workspace_id = str(uuid4())
    user_id = str(uuid4())

    users = [{"id": user_id, "workspace_role": "invalid_role"}]

    response = client.put(
        "/api/v1/workspaces/{}/users".format(workspace_id),
        content_type="application/json",
        data=dumps({"users": users}),
    )

    assert response.status_code == 404


def test_get_workspace_user(client):
    workspace_id = str(uuid4())
    user_id = str(uuid4())

    users = [{"id": user_id, "workspace_role": "developer"}]

    client.put(
        "/api/v1/workspaces/{}/users".format(workspace_id),
        content_type="application/json",
        data=dumps({"users": users}),
    )

    response = client.get(
        "/api/v1/workspaces/{}/users/{}".format(workspace_id, user_id),
        content_type="application/json",
    )
    assert response.status_code == 200
    assert "view_usage_report" in response.json["permissions"]
    assert "review_and_approve_jedi_workspace" not in response.json["permissions"]


def test_get_nonexistent_workspace_user(client):
    workspace_id = str(uuid4())
    user_id = str(uuid4())

    response = client.get(
        "/api/v1/workspaces/{}/users/{}".format(workspace_id, user_id),
        content_type="application/json",
    )
    assert response.status_code == 404


def test_ccpo_has_workspace_permissions_by_default(client):
    user_id = str(uuid4())
    workspace_id = str(uuid4())

    client.post(
        "/api/v1/users",
        content_type="application/json",
        data=dumps({"id": user_id, "atat_role": "ccpo"}),
    )
    response = client.get(
        "/api/v1/workspaces/{}/users/{}".format(workspace_id, user_id),
        content_type="application/json",
    )
    assert "view_usage_report" in response.json["permissions"]
