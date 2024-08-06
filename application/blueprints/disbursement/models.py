from application.extensions import db


class Disbursement(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref='disbursements', lazy=True)
  