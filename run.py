from app import create_app
from app.db import db

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        from app import models
        db.create_all()
    app.run(debug="True")