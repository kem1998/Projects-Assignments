from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dateutil.parser import parse

from borrower_dao import BorrowerDAO

DATABASE_URI = 'sqlite:///app.db'

def get_db_session():
    engine = create_engine(DATABASE_URI, echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session 

def test_create():
    session = get_db_session()
    bor = BorrowerDAO()
    data = {
        'first_name': "Kaneki",
        'last_name': "Kun",
        'date_of_birth': "18-10-1998",
        'email_address': "kaneki@gmail.com",
        'mobile_number': "(04) 0119 0509",
        'street_address': "34, Bik Lane",
        'suburb': "Fitzroy North",
        'state': "VIC",
        'postcode': "3068"
    }
    result = bor.create(session, data)
    print(result)
    session.close()

def test_find_by_id():
    session = get_db_session()
    bor = BorrowerDAO()
    borrower_id = 1
    result = bor.find_by_id(session, borrower_id)
    print(result)
    session.close()

def test_find_all():
    session = get_db_session()
    bor = BorrowerDAO()
    result = bor.find_all(session)
    print(result)
    session.close()    

def test_find_by_last_name():
    session = get_db_session()
    bor = BorrowerDAO()
    last_name = "Kaneki" 
    result = bor.find_by_last_name(session, last_name)
    print(result)
    session.close()  

def test_find_ids():
    session = get_db_session()
    bor = BorrowerDAO()
    result = bor.find_ids(session)
    print(result)
    session.close()    

def test_update():
    session = get_db_session()
    bor = BorrowerDAO()
    borrower_id = 1

    data = {}
    data['first_name'] = "Kaneki"
    data['last_name'] = "Kun"
    data['date_of_birth'] = "18-10-1998"
    data['email_address'] = "kaneki@gmail.com"
    data['mobile_number'] = "(04) 0119 0509"
    data['street_address'] = "34, Bik Lane"
    data["suburb"] = "Fitzroy North"
    data["state"] = "VIC"
    data["postcode"] = "3068"

    result = bor.update(session, borrower_id, data)
    print(result)
    session.close()    

def test_delete():
    session = get_db_session()
    bor = BorrowerDAO()
    borrower_id = 1
    result = bor.delete(session, borrower_id)
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