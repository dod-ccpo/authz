from authz.make_app import make_app, make_config


config = make_config()
app = make_app(config)
app.run()
