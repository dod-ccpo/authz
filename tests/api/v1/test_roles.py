def test_get_roles(client):
    response = client.get('/roles')
    assert response.status_code == 200
    role_names = [role['name'] for role in response.json]
    assert(set(['admin', 'owner', 'developer']).issubset(role_names))
