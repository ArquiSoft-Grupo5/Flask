from app import create_app
from app.migrate import init_db

app = create_app()
@app.route("/")
def index() :
    return"Hola mundo"

@app.route("/database")
def database():
    init_db()
    return "base de datos creada correctamente."