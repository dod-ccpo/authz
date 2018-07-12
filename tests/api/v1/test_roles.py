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

