from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import sQLAlchemy

db = sQLAlchemy ()

class User(db. Model) :

    ___tablename___="users"
    id db.Column (db.Integer,primary_key=True)
    username = db.Column (db.String (80), unique=True,nullable=False)
    is_admin = db.Column (db.Boolean,default=False)
    def ___repr___ (self) :
        return '<User %r>' % self.username

    def set_password (self, password) :
        self.password=generate_password_hash (password)
    def check_password (self, password) :
        return check_password_hash (self.password, password)

class Category (db. Model) :
    ___tablename___ = "ideas"
    id = db.Column (db.Integer, primary_key=True)
    name = db.Column (db.String (58), nullable=False)

class Idea (db. Model ):
    ___tablename___ = "ideas"
    id = db.Column (db.Integer, primary_key=True)
    title = db.Column (db.String (80    ), nullable=False)
    description = db.Column (db.String (250) , nullable=False)
    is_public = db.Column (db.Boolean, default=False)
    category_id = db.Column (db.Integer, db.Foreignkey ( 'categories.id' , ondelete="CASCADE"),
        nullable=False)
    category = db.relationship( 'Category', backref=db.backref("ideas", lazy=True ))
    user_id = db.Column (db. Integer, db. ForeignKey ( 'users.id', ondelete='CASCADE'),
        nullable=False)
    user = db.relationship("User", backref=db.backref('ideas', lazy=True))