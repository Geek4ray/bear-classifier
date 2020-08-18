from my_app import app
app.run()
# or for custom commands
with app.app_context():
    do_command()