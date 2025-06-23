from app import app
from models import db, Message

with app.app_context():
    print("Clearing old data...")
    Message.query.delete()

    print("Seeding messages...")
    message = Message(body="Hello world!", username="tester")
    db.session.add(message)
    db.session.commit()

    print("Seeding complete.")
