# authz API

## Roles

### Get roles

Get a list of all existing roles.

#### Request
```
GET /api/v1/roles
```

#### Response
```
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
```
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
