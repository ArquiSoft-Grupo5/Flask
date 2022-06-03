from .database import *   
def create_db() :
    """Método de creación de la base de datos. """ 
    db.drop_all ()
    db.create_all()
def init_db()
    """Método de inicialización de nuestra base de datos."""
    create_db()
    #User admin apP
    admin = User(
        username="SuperAdmin",
        is_admin=True,
    )
    admin. set_passMord ("123Admin")
db.session.add (admin)
db.session.commit ()