from schema import Librarian
from dateutil.parser import parse

class LibrarianDAO():

    def create(self, session, data):
        print("\nCreating a new librarian ...")
        print(data)

        librarian = Librarian(first_name = data['first_name'], 
                    last_name = data['last_name'], 
                    email_address = data['email_address'],
                    mobile_number = data['mobile_number'],
                    )

        session.add(librarian)
        session.commit() 

        result = {}  
        result['message'] = 'New Librarian added successfully!'
        inserted_librarian_id = librarian.librarian_id
        result['librarian_id'] = inserted_librarian_id

        return result 

    def find_by_id(self, session, librarian_id):
        print("\nFinding a librarian ...")
        print(librarian_id)

        libr = session.query(Librarian).get(librarian_id) 
        result = {}

        if not libr:

            result['message'] = "Librarian is not enrolled!"
        else:
            d = {}
            d['librarian_id'] = libr.librarian_id
            d['first_name'] = libr.first_name
            d['last_name'] = libr.last_name
            d['email_address'] = libr.email_address

            result['librarian'] = d

        return result

    def find_by_last_name(self, session, last_name): 
        print("\nFinding librarian(s) by last_name ...")
        print(last_name)

        result = {}

        rows = session.query(Librarian) \
               .filter(Librarian.last_name.like(last_name)) \
               .order_by(Librarian.librarian_id).all()   

        if not rows:
            result['message'] = "No librarian with last_name found!" 
        else:
            list_libr = [] 
            for x in rows:
                d = {} 
                d['librarian_id'] = x.librarian_id
                d['first_name'] = x.first_name
                d['last_name'] = x.last_name
                d['email_address'] = x.email_address
                d['mobile_number'] = x.mobile_number
                list_libr.append(d) 
                pass     
                
            result['librarians'] = list_libr
           
        return result 

    def find_all(self, session):
        print("\nFinding all librarians ...")

        result = {}

        rows = session.query(Librarian).all()

        if not rows:
            result['message'] = "No librarians found!"
        else:
            list_libr = [] 
            for x in rows: 
                d = {} 
                d['librarian_id'] = x.librarian_id
                d['first_name'] = x.first_name
                d['last_name'] = x.last_name
                d['email_address'] = x.email_address
                d['mobile_number'] = x.mobile_number
                list_libr.append(d) 
                pass     

            result['librarian'] = list_libr
            
        return result

    def find_ids(self, session):
        print("\nFinding all librarians ids...")

        result = {}
 
        rows = session.query(Librarian).all()

        if not rows:
            result['message'] = "No librarian found!"
        else:
            list_ids = []
            for x in rows:
                list_ids.append(x.librarian_id)
                pass               

            result['librarian_ids'] = list_ids
        
        return result

    def update(self, session, librarian_id, data):
        print("\nUpdating librarian ...")
        print(librarian_id)
        print(data)

        result = {}

        libr = session.query(Librarian).get(librarian_id)

        libr.first_name = data['first_name']
        libr.last_name = data['last_name']
        libr.email_address = data['email_address']
        libr.mobile_number = data['mobile_number']

        session.commit() 

        result['message'] = "Librarian updated!"     

        return result 

    def delete(self, session, librarian_id):
        print("\nDeleting librarian ...")
        print(librarian_id)

        result = {}
   
        libr = session.query(Librarian).get(librarian_id)
        
        session.delete(libr)          
        session.commit()   

        result['message'] = "Librarian deleted"    

        return result  