from Shop import app
from Shop import db
from Shop import manager
from Shop import migrate


if __name__ == "__main__":
    app.run(debug=True)
    manager.run()