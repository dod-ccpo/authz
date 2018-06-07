from uuid import uuid4


def test_get_roles(client):
    response = client.get('/roles')
    assert response.status_code == 200
    role_names = [role['name'] for role in response.json]
    assert(set(['admin', 'owner', 'developer']).issubset(role_names))


def test_get_workspace_user_roles(client):
    workspace_id = uuid4()
    response = client.get('/workspaces/{}/users'.format(workspace_id))
    assert response.status_code == 200
