from app.database import SessionLocal
from app.models import Question

questions = [
("What is the capital of India?","Mumbai","New Delhi","Kolkata","Chennai","B",1,"India"),
("Which planet is known as the Red Planet?","Earth","Venus","Mars","Jupiter","C",2,"Science"),
("Who wrote the national anthem of India?","Rabindranath Tagore","Bankim Chandra Chattopadhyay","Sarojini Naidu","Premchand","A",3,"India"),
("Which is the largest ocean?","Atlantic","Indian","Arctic","Pacific","D",4,"Geography"),
("What is 12 × 12?","124","144","154","164","B",5,"Math"),
("Which language is mainly used for web page structure?","Python","HTML","SQL","C++","B",6,"Technology"),
("Which gas do plants absorb?","Oxygen","Nitrogen","Carbon dioxide","Hydrogen","C",7,"Science"),
("Who is known as the Missile Man of India?","A. P. J. Abdul Kalam","C. V. Raman","Homi Bhabha","Vikram Sarabhai","A",8,"India"),
("Which database is relational?","MySQL","MongoDB","Redis","Neo4j","A",9,"Technology"),
("What does CPU stand for?","Central Processing Unit","Computer Personal Unit","Central Program Utility","Core Processing User","A",10,"Technology"),
("Which is the longest river in India?","Yamuna","Ganga","Godavari","Narmada","B",11,"Geography"),
("Which company created React?","Google","Microsoft","Meta","Amazon","C",12,"Technology"),
("Which is the smallest prime number?","0","1","2","3","C",13,"Math"),
("What is the currency of Japan?","Won","Yuan","Dollar","Yen","D",14,"General"),
("Which element has chemical symbol O?","Gold","Oxygen","Osmium","Iron","B",15,"Science"),
]

db=SessionLocal()
try:
    if db.query(Question).count()==0:
        for row in questions:
            db.add(Question(question=row[0],option_a=row[1],option_b=row[2],option_c=row[3],option_d=row[4],correct_answer=row[5],prize_level=row[6],category=row[7]))
        db.commit()
        print("15 questions inserted.")
    else:
        print("Questions already exist.")
finally:
    db.close()
