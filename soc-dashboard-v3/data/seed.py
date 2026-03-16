from app import db, User, Incident

db.create_all()

admin = User(username="admin", password="soc123")

db.session.add(admin)

db.session.add(Incident(type="Malware Alert",severity="High",status="Investigating",time="10:15"))
db.session.add(Incident(type="Unauthorized Login",severity="Medium",status="Resolved",time="09:40"))
db.session.add(Incident(type="Phishing Email",severity="Low",status="Monitoring",time="08:30"))

db.session.commit()

print("Database Created Successfully")