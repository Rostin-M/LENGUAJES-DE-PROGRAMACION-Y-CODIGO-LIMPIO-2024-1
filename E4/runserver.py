from os import environ
from MVC_HIPOTECA_INVERSA_4 import app

if __name__ == '__main__':
    
    from MVC_HIPOTECA_INVERSA_4.model.database_manager import DatabaseManager
    
    db = DatabaseManager()    
    db.create_tables()

    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)