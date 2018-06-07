from authz.models.role import Role


def seed_db(app, db):
    roles = [
        Role(
            name='admin',
            description='',
            permissions=['assign_atat_role', 'remove_atat_role']
        ),
        Role(
            name='owner',
            description='',
            permissions=['']
        ),
        Role(
            name='developer',
            description='',
            permissions=['']
        ),
        Role(
            name='ccpo',
            description='',
            permissions=['']
        ),
    ]

    with app.app_context():
        if Role.query.count() == 0:
            db.session.add_all(roles)
            db.session.commit()
