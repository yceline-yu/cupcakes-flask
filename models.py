from flask_sqlalchemy import SQLAlchemy 
db = SQLAlchemy()

DEFAULT_IMAGE = "https://tinyurl.com/demo-cupcake"

"""Models for Cupcake app."""

class Cupcake(db.Model):
    """ Cupcake. """

    __tablename__ = "cupcakes"

    id= db.Column(db.Integer, 
                    primary_key=True,
                    autoincrement=True)

    flavor= db.Column(db.Text,
                        nullable=False)

    size= db.Column(db.Text,
                        nullable=False)

    rating= db.Column(db.Integer,
                        nullable=False)

    image= db.Column(db.Text,
                        nullable=False,
                        default=DEFAULT_IMAGE)

    def __repr__(self):
        c = self
        return f'<ID={c.id}, FLAV={c.flavor}, SIZ={c.size}' 

    def serialize(self):
        """serialize to dict."""
        return {
            "id": self.id,
            "flavor": self.flavor,
            "size": self.size,
            "rating": self.rating,
            "image": self.image
        }                   

def connect_db(app):
    """Connect to database."""
    db.app = app
    db.init_app(app)