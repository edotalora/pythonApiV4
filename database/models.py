from .db import db

class Client(db.Document):
    doc_id = db.StringField(required=True, unique=True)
    name = db.StringField(required=True)
    last_name = db.StringField(required=True)
    preexistence = db.ListField(db.StringField(), required=True)
    
class Documento(db.Document):
    doc_id = db.StringField(required=True, unique=True)
    name = db.StringField(required=True)
    tarifa = db.StringField(required=True)
    userDoc = db.StringField(required=True)
    tipoDoc = db.StringField(required=True)
