from booky import create_app, db
from booky.auth.models import User

flask_app = create_app('prod')

if __name__ == '__main__':

    with flask_app.app_context():
        db.create_all()

    flask_app.run()

