from schema import Borrower
from dateutil.parser import parse

class BorrowerDAO():

    def create(self, session, data):
        print("\nCreating a new borrower ...")
        print(data)

        borrower = Borrower(first_name = data['first_name'], 
                    last_name = data['last_name'], 
                    date_of_birth = data['date_of_birth'], 
                    email_address = data['email_address'],
                    mobile_number = data['mobile_number'],
                    street_address = data['street_address'],
                    suburb = data['suburb'],
                    state = data['state'],
                    postcode = data['postcode']
                    )

        session.add(borrower)
        session.commit() 

        result = {}  
        result['message'] = 'New Borrower added successfully!'
        inserted_borrower_id = borrower.borrower_id
        result['borrower_id'] = inserted_borrower_id

        return result 

    def find_by_id(self, session, borrower_id):
        print("\nFinding a borrower ...")
        print(borrower_id)

        bor = session.query(Borrower).get(borrower_id)
        result = {}

        if not bor:

            result['message'] = "Borrower is not enrolled!"
        else:
            d = {}
            d['borrower_id'] = bor.borrower_id
            d['first_name'] = bor.first_name
            d['last_name'] = bor.last_name
            d['date_of_birth'] = bor.date_of_birth
            d['email_address'] = bor.email_address
            d['mobile_number'] = bor.mobile_number
            d['street_address'] = bor.street_address
            d['suburb'] = bor.suburb
            d['postcode'] = bor.postcode

            result['borrower'] = d

        return result

    def find_by_last_name(self, session, last_name): 
        print("\nFinding borrower(s) by last_name ...")
        print(last_name)

        result = {}

        rows = session.query(Borrower) \
               .filter(Borrower.last_name.like(last_name)) \
               .order_by(Borrower.borrower_id).all()   

        if not rows:
            result['message'] = "No borrower with last_name found!" 
        else:
            list_bor = [] 
            for x in rows:
                d = {} 
                d['borrower_id'] = x.borrower_id
                d['first_name'] = x.first_name
                d['last_name'] = x.last_name
                d['date_of_birth'] = x.date_of_birth
                d['email_address'] = x.email_address
                d['mobile_number'] = x.mobile_number
                d['street_address'] = x.street_address
                d['suburb'] = x.suburb
                d['postcode'] = x.postcode
                list_bor.append(d) 
                pass     
                
            result['borrowers'] = list_bor
           
        return result 

    def find_all(self, session):
        print("\nFinding all borrowers ...")

        result = {}

        rows = session.query(Borrower).all()

        if not rows:
            result['message'] = "No borrowers found!"
        else:
            list_bor = [] 
            for x in rows: 
                d = {} 
                d['borrower_id'] = x.borrower_id
                d['first_name'] = x.first_name
                d['last_name'] = x.last_name
                d['date_of_birth'] = x.date_of_birth
                d['email_address'] = x.email_address
                d['mobile_number'] = x.mobile_number
                d['street_address'] = x.street_address
                d['suburb'] = x.suburb
                d['postcode'] = x.postcode
                list_bor.append(d) 
                pass     

            result['borrower'] = list_bor
            
        return result

    def find_ids(self, session):
        print("\nFinding all borrowers ids...")

        result = {}
 
        rows = session.query(Borrower).all()

        if not rows:
            result['message'] = "No borrower found!"
        else:
            list_ids = []
            for x in rows:
                list_ids.append(x.borrower_id)
                pass               

            result['borrower_ids'] = list_ids
        
        return result

    def update(self, session, borrower_id, data):
        print("\nUpdating borrower ...")
        print(borrower_id)
        print(data)

        result = {}

        bor = session.query(Borrower).get(borrower_id)

        bor.first_name = data['first_name']
        bor.last_name = data['last_name']
        bor.date_of_birth = data['date_of_birth']
        bor.email_address = data['email_address']
        bor.mobile_number = data['mobile_number']
        bor.street_address = data['street_address']
        bor.suburb = data['suburb']
        bor.postcode = data['postcode']

        session.commit() 

        result['message'] = "Borrower updated!"     

        return result 

    def delete(self, session, borrower_id):
        print("\nDeleting borrower ...")
        print(borrower_id)

        result = {}
   
        bor = session.query(Borrower).get(borrower_id)
        session.delete(bor)          
        session.commit()   

        result['message'] = "Borrower deleted"    

        return result  