import mysql.connector 

#etablir une connection a la base de donnee
connexion = mysql.connector.connect(
    host = 'localhost',
    user = 'root' ,
    password = '' ,
    database = 'crud_python' 
)

def create_user(nom, email,):
    cursor = connexion.cursor()
    cursor.execute("""
        INSERT INTO utilisateur (nom , email)  
        VALUES (%s, %s)                    
                   """, (nom, email))
    connexion.commit()

    def read_users():
        cursor = connexion.cursor()
        cursor.execute("SELECT * FROM utilisateur")
        for (id, nom, email)in cursor:
            print (f"ID: {id}, Nom: {nom}, Email: {email}")

def update_user(id, email):
        cursor = connexion.cursor
        cursor.execute("""
        UPDATE utilisateur
        SET email = %s
        WHERE id = %s               
                       """, (email, id))
        connexion.commit()

def delete_user(id):
        cursor = connexion.cursor()
        cursor.execute("""
        DELETE FROM utilisateur
        WHERE id = %s               
                       """, (id,))
        connexion.commit()



#create_user("John DOE", "john.doe@example.com")    
        read_users()
        update_user("2", "emicheldev@gmail.com")