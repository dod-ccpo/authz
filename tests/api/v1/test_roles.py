from uuid import uuid4
from json import dumps


def test_get_roles(client):
    response = client.get('/roles')
    assert response.status_code == 200
    role_names = [role['name'] for role in response.json]
    assert(set(['admin', 'owner', 'developer']).issubset(role_names))


def test_get_existing_role(client):
    response = client.get('/roles/developer')
    assert response.status_code == 200
    assert response.json['name'] == 'developer'
    assert 'permissions' in response.json


def test_get_nonexistent_role(client):
    response = client.get('/roles/puppy')
    assert response.status_code == 404



def test_get_workspace_user_roles(client):
    workspace_id = uuid4()
    response = client.get('/workspaces/{}/users'.format(workspace_id))
    assert response.status_code == 200


def test_update_workspace_user_roles(client):
    workspace_id = uuid4()
    owner_id = str(uuid4())
    admin_id = str(uuid4())

    new_workspace_users = {
        owner_id: {
            'roles': ['owner']
        },
        admin_id: {
            'roles': ['admin']
        }
    }

    response = client.put(
        '/workspaces/{}/users'.format(workspace_id),
        content_type='application/json',
        data=dumps(new_workspace_users))
    assert('owner' in response.json[owner_id]['roles'])
