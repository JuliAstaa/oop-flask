from . import db

# setiap class adalah table di database
class Contact(db.Model):
    id: int = db.Column(db.Integer, primary_key = True)
    name: str = db.Column(db.String(80), nullable=False)
    no_hp: str = db.Column(db.String(15), nullable=False, unique=True)
    email: str = db.Column(db.String(30), nullable=False)

    # representasi string dari objek, bagus buat debug
    def __repr__(self):
        return f"<Contact {self.name}>"