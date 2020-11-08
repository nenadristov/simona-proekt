import sqlite3
konekcija= sqlite3.connect("Biblioteka.db")
c=konekcija.cursor()
try:
   c.execute("""CREATE TABLE Biblioteka
   (idKniga UNIQUE  PRIMARY KEY,
   Naslov VARCHAR(30),
   Avtor VARCHAR(30),
   Zanr VARCHAR(30),
   BrojNaKnigi INTEGER,
   BrojDostapniKnigi INTEGER
   )
 
   """)
 
   c.execute("""CREATE TABLE Clen
   (idKniga UNIQUE  PRIMARY KEY,
   Ime VARCHAR(30),
   Prezime VARCHAR(30),
   DataNaRagjanje VARCHAR(30),
   MaticenBroj VARCHAR(30),
   UlicaNaZiveenje VARCHAR(30),
   MestoNaZiveenje VARCHAR(30),
   TelefonskiBroj INTEGER,
   ZemenoKniga INTEGER
   )
 
   """)
   konekcija.commit()
   print("Tabelite se kreirani")
except sqlite3.OperationalError:
   print("Tabelite se kreirani")
try:
   c.execute("""INSERT INTO Biblioteka VALUES ('1','Hari Poter','J.K.Rouling ','Misterija','10','4')""")
 
   c.execute("""INSERT INTO Biblioteka VALUES ('2','Asistola','Marija Janevska ','Ljubovna','10','2')""")
 
   c.execute("""INSERT INTO Biblioteka VALUES ('3','Drakula','Bram Stoker ','Triler','10','6')""")
 
   c.execute("""INSERT INTO Biblioteka VALUES ('4','Inferno','Den Braun ','Misterija','10','2')""")
 
   c.execute("""INSERT INTO Biblioteka VALUES ('5','Origin','Den Braun ','Misterija','10','8')""")
except sqlite3.IntegrityError:
   print("Podatokot vekje postoi")
 
try:
   c.execute("""INSERT INTO Clen VALUES ('1','Simona','Petrushevska','14.12.1997','1412997455002','Cucevska','Skopje','075210928','1')""")
 
   c.execute("""INSERT INTO Clen VALUES ('2','Gordana','Petrushevska','20.09.1970','2009997055002','Cucevska','Skopje','075210928','0')""")
 
   c.execute("""INSERT INTO Clen VALUES ('3','Saso','Petrushevski','14.12.1997','1412997455002','Cucevska','Skopje','075210928','1')""")
 
   c.execute("""INSERT INTO Clen VALUES ('4','Irina','Nikovska','14.12.1997','1412997455002','Cucevska','Skopje','075210928','0')""")
 
   c.execute("""INSERT INTO Clen VALUES ('5','Martin','Grozdanovski','14.12.1997','1412997455002','Cucevska','Skopje','075210928','1')""")
 
except sqlite3.IntegrityError:
   print("Podatokot vekje postoi")
 
    
c.execute("""SELECT * FROM Clen""")
clen=c.fetchall()
#print(clen)
 
c.execute(""" SELECT * FROM Biblioteka""")
biblioteka=c.fetchall()
#print(biblioteka)
 
for i in clen:
    print(i[1])
    print(i[2])
    print(i[5])
 
ime=input("Vnesi ime na klient")
prezime=input("Vnesi prezime na klient")
ulica=input("Vnesi ulica na ziveenje")
 
for i in clen:
    if (ime==i[1] and prezime==i[2] and i[8]==0):
       print("moze da podigne kniga")
 
       imenakniga=input("vnesi koja kniga saka da ja zeme")
    
       for i in biblioteka:
           if imenakniga == i[1] and i[5] != 0:
                print("moze da ja podigne knigata")
                dostapnost = int(i[4])
                dostapnost -= 1
                
           elif imenakniga == i[1] and i[5] == 0:
                print("knigata ne e dostapna")
               
                
 
   
 
for i in clen:
    if (ime==i[1] and prezime==i[2] and i[8]==1):
       print("Klientot ima podignato kniga")
       break


 
#konekcija.commit()