from flask import Flask
from services import database_service

app = Flask(__name__)

database_service.connect_to_database()

import resources.players

if __name__ == "__main__":
    app.run(debug=True)
