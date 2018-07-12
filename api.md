# authz API

## Roles

### Get roles

Get a list of all existing roles.

#### Request
```
GET /api/v1/roles
```

#### Response
```json
[
  {
    "description": "",
    "id": "10e7a1c5-7f48-46ea-90d9-6bf7181c8cfc",
    "name": "billing_auditor",
    "permissions": [
      "view_usage_report",
      "view_usage_dollars",
      "federate_into_csp",
      "view_application_in_workspace",
      "view_environment_in_application"
    ]
  },
  {
    "description": "",
    "id": "67674f2a-b647-4a57-909b-6d0fe06a2444",
    "name": "security_auditor",
    "permissions": [
      "view_assigned_atat_role_configurations",
      "view_assigned_csp_role_configurations",
      "federate_into_csp",
      "view_atat_permissions",
      "view_application_in_workspace",
      "view_environment_in_application"
    ]
  },
  {
    "description": null,
    "id": "37c9ac51-3d00-4c5f-ad9b-35ddffc2f027",
    "name": "default",
    "permissions": []
  }
]
```

### Get role

Get a role by name.

#### Request
```
GET /api/v1/role/developer
```

#### Response

```json
{
    "description": "",
    "id": "a380fdcd-ca5f-407f-9b9b-d54d2ef6a5be",
    "name": "developer",
    "permissions": [
        "view_usage_report",
        "view_usage_dollars",
        "federate_into_csp",
        "view_application_in_workspace",
        "view_environment_in_application"
    ]
}
```

## Users

### Create a new user

Creates a new atat user with the given role.

#### Request

```
POST /users/
{
    id: <user id>,
    atat_role: <name of an atat role>
}
```

#### Response

```
{
    "atat_role": "developer",
    "id": "4069cdec-6750-44d4-97d7-126658019040",
    "username": null,
    "workspace_roles": []
}
```

### Update a user

Update a given user with a new atat role.

#### Request

```json
PUT /users/<user id>
{
    atat_role: <name of an atat role>
}
```

#### Response

```json
{
    "atat_role": "developer",
    "id": "4069cdec-6750-44d4-97d7-126658019040",
    "username": null,
    "workspace_roles": []
}
```

## Workspaces

### Get workspace users

#### Request

```
GET /workspaces/<workspace id>/users/<user id>
```

### Update workspace users

#### Request

```json
PUT /workspaces/<workspace id>/users
{
    "users": [
        {"id": "", "workspace_role": "developer"}
    ]
}
```

#### Response

```json
{
  "atat_role":"developer",
  "id":"42627d7d-f58f-4217-baa6-1c5346186e26",
  "permissions": [
    "view_application_in_workspace",
    "view_environment_in_application",
    "view_usage_report",
    "view_usage_dollars"
  ],
  "username": None,
  "workspace_roles": ["577eeddd-2bc2-4b74-8163-79f5d91d02ba"]
}
```
