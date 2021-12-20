from flask import Flask, render_template, redirect, request, flash
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = 'nitusec'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///king.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= True
db = SQLAlchemy(app)


class King(db.Model):
    __tablename__='king'
    id = db.Column(db.Integer, primary_key=True)
    incident = db.Column(db.String(800),  nullable=False)
    place = db.Column(db.String(80),  nullable=False)
    incident_date = db.Column(db.String(10),  nullable=False)


# this is for assignment section


@app.route('/', methods = ['GET', 'POST'])
def home():
    if request.method=='POST':
        name = request.form['name']
        role = request.form['role']
        if name == "RAM" and role=="KING":
            return redirect ('/form')
        if name=="LAXMAN" and role=="MINISTER":
            return redirect ('/submitted')   
    return render_template ('index.html')

@app.route('/form', methods=['GET','POST'])
def form():
    if request.method=='POST':        
        place = request.form['place']        
        incident = request.form['incident']
        incident_date = request.form['date']
        king = King(place=place, incident=incident,incident_date=incident_date)
        db.session.add(king)
        db.session.commit()     
        return redirect ('/')  

    return render_template ('form.html')

@app.route('/submitted', methods=['GET','POST'])
def submitted():
    king = King.query.all()
    return render_template ('submitted.html', king=king )
 

if __name__=='__main__':
    app.run(debug=True)