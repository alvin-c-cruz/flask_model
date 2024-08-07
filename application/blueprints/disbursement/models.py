from application.extensions import db
import  json


class Disbursement(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    record_date = db.Column(db.Date())
    
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref='disbursements', lazy=True)
    
    def __str__(self) -> str:
        _dict = {
            "id": self.id,
            "record_date": str(self.record_date),
            "user_id": self.user_id,
            "details": [] 
        }
        
        for detail in self.disbursement_details:
            _dict["details"].append({
                "id": detail.id,
                "disbursement_id": detail.disbursement_id,
                "description": detail.description,
                "amount": detail.amount
            })
        return json.dumps(_dict, indent=4)
  

class DisbursementDetail(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    
    disbursement_id = db.Column(db.Integer, db.ForeignKey('disbursement.id'), nullable=False)
    dusbursement = db.relationship('Disbursement', backref='disbursement_details', lazy=True)

    description = db.Column(db.String())
    amount = db.Column(db.Float())
