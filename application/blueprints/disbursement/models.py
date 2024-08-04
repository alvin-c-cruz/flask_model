from application.extensions import db


class Disbursement(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    record_date = db.Column(db.Date())
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref='disbursements', lazy=True)
  

class DisbursementDetail(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    
    disbursement_id = db.Column(db.Integer, db.ForeignKey('disbursement.id'), nullable=False)
    dusbursement = db.relationship('Disbursement', backref='disbursement_details', lazy=True)

    description = db.Column(db.String())
    amount = db.Column(db.Float())
