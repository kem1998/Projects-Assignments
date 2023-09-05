from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from librarian_dao import LibrarianDAO

DATABASE_URI = 'sqlite:///app.db'

def get_db_session():
    engine = create_engine(DATABASE_URI, echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session 

def test_create():
    session = get_db_session()
    libr = LibrarianDAO()
    data = {
        'first_name': "Kemith",
        'last_name': "Nanayakkara",
        'email_address': "kemithsan@gmail.com",
        'mobile_number': "(04) 0119 0432",
    }
    result = libr.create(session, data)
    print(result)
    session.close()

def test_find_by_id():
    session = get_db_session()
    libr = LibrarianDAO()
    librarian_id = 1
    result = libr.find_by_id(session, librarian_id)
    print(result)
    session.close()

def test_find_all():
    session = get_db_session()
    libr = LibrarianDAO()
    result = libr.find_all(session)
    print(result)
    session.close()    

def test_find_by_last_name():
    session = get_db_session()
    libr = LibrarianDAO()
    last_name = "Kemith" 
    result = libr.find_by_last_name(session, last_name)
    print(result)
    session.close()  

def test_find_ids():
    session = get_db_session()
    libr = LibrarianDAO()
    result = libr.find_ids(session)
    print(result)
    session.close()    

def test_update():
    session = get_db_session()
    libr = LibrarianDAO()
    librarian_id = 1

    data = {}
    data['first_name'] = "Kemith"
    data['last_name'] = "Nanayakkara"
    data['email_address'] = "kemithsan@gmail.com"
    data['mobile_number'] = "(04) 0119 0432"

    result = libr.update(session, librarian_id, data)
    print(result)
    session.close()    

def test_delete():
    session = get_db_session()
    libr = LibrarianDAO()
    librarian_id = 1
    result = libr.delete(session, librarian_id)
    print(result)
    session.close()          

if __name__ == "__main__":

    print("\nTesting ...")

    test_create()
    test_find_by_id()
    test_find_all()
    test_find_by_last_name()
    test_find_ids()
    test_update()
    test_delete()