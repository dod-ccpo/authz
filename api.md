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

### Retrieve a user

#### Request

```
GET /api/v1/users/<user id>
```

#### Response

```json
{
    "atat_permissions": [
        "view_usage_report",
        "view_usage_dollars",
        "view_application_in_workspace",
        "view_environment_in_application"
    ],
    "atat_role": "developer",
    "id": "164497f6-c1ea-4f42-a5ef-101da278c012",
    "username": null,
    "workspace_roles": []
}
```

### Create a new user

Creates a new atat user with the given role.

#### Request

```
POST /api/v1/users/
{
    id: <user id>,
    atat_role: <name of an atat role>
}
```

#### Response

```json
{
    "atat_permissions": [
        "view_usage_report",
        "view_usage_dollars",
        "view_application_in_workspace",
        "view_environment_in_application"
    ],
    "atat_role": "developer",
    "id": "164497f6-c1ea-4f42-a5ef-101da278c012",
    "username": null,
    "workspace_roles": []
}
```

Returns a 201 if a new user was created, and a 200 if the user already exists.

### Update a user

Update a given user with a new atat role.

#### Request

```json
PUT /api/v1/users/<user id>
{
    atat_role: <name of an atat role>
}
```

#### Response

```json
{
    "atat_permissions": [
        "view_usage_report",
        "view_usage_dollars",
        "view_application_in_workspace",
        "view_environment_in_application"
    ],
    "atat_role": "developer",
    "id": "164497f6-c1ea-4f42-a5ef-101da278c012",
    "username": null,
    "workspace_roles": []
}
```

## Workspaces

### Get workspace users

#### Request

```
GET /api/v1/workspaces/<workspace id>/users/<user id>
```

#### Response

```json
{
  "permissions": [
    "view_environment_in_application",
    "view_application_in_workspace",
    "view_usage_dollars",
    "view_usage_report"
  ],
  "user": {
    "atat_role": "developer",
    "id": "99b161eb-ed10-40af-90b2-331a271c4ee7",
    "username": "fake_user",
    "workspace_roles": ["69d245a6-d859-4cb2-b0b8-015c103aae20"]
  },
  "workspace_id": "bf1b7d0a-99a2-435f-a285-c353332b0f27"
}
```

### Update workspace users

#### Request

```json
PUT /api/v1/workspaces/<workspace id>/users
{
  "users": [
    {"id": "78b274ab-62e7-4132-8a0c-8fb4d94e449b", "workspace_role": "developer"},
    {"id" :"3c13b296-8aa9-4112-81d8-a16c3570f515", "workspace_role": "owner"}
  ]
}
```

#### Response

```json
[
    {
        "permissions": [
            "view_usage_report",
            "view_environment_in_application",
            "view_usage_dollars",
            "view_application_in_workspace"
        ],
        "user": {
            "atat_role": "developer",
            "id": "78b274ab-62e7-4132-8a0c-8fb4d94e449b",
            "username": "fake_user1",
            "workspace_roles": [
                "998af241-d9ce-419c-b8d1-2d4672909998"
            ]
        },
        "workspace_id": "4069cdec-6750-44d4-97d7-126658019040"
    },
    {
        "permissions": [
            "view_environment_in_application",
            "view_usage_report",
            "view_usage_dollars",
            "view_assigned_atat_role_configurations",
            "add_and_assign_csp_roles",
            "remove_csp_roles",
            "rename_application_in_workspace",
            "delete_application_in_workspace",
            "request_jedi_workspace",
            "view_application_in_workspace",
            "view_atat_permissions",
            "assign_and_unassign_atat_role",
            "view_original_jedi_request",
            "view_assigned_csp_role_configurations",
            "add_environment_in_application",
            "deactivate_environment_in_application",
            "deactivate_application_in_workspace",
            "delete_environment_in_application",
            "add_application_in_workspace",
            "request_new_csp_role",
            "rename_environment_in_application",
            "deactivate_workspace"
        ],
        "user": {
            "atat_role": "developer",
            "id": "3c13b296-8aa9-4112-81d8-a16c3570f515",
            "username": "fake_user2",
            "workspace_roles": [
                "fc4b8163-1fd1-4dc0-ab34-afe560dbcd83"
            ]
        },
        "workspace_id": "4069cdec-6750-44d4-97d7-126658019040"
    }
]
```
