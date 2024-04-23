from app import db

from datetime import date, timedelta, datetime


class HistorialDominio(db.Model):
    __tablename__ = "dominiosi"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    nombre = db.Column(db.String(20), nullable=False)
   