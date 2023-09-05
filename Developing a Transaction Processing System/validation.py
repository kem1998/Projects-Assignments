# validation.py
# France Cheong
# 22/11/2018

# ########
# Packages
# ########
import re # regular expression

# ################
# Validation Class
# ################

class Validation():

    def is_numeric(self, val):
        val = str(val) # only str have the isnumeric() method
        if val.isnumeric():
            print("Numeric")
            return True
        else:
            print("Not numeric")
            return False  

    def is_alphabetic(self, val):
        val = str(val)
        if val.isalpha():
            print("Alphabetic")
            return True
        else:
            print("Not alphabetic")
            return False  

    def is_alphanumeric(self, val):
        val = str(val)
        if val.isalnum():
            print("Alphanumeric")
            return True
        else:
            print("Not alphanumeric")
            return False  

    def is_mobile_number(self, val):
        val = str(val)
        if re.search(r'^(\d{10})(?:\s|$)', val):
            print("Valid mobile number")
            return True
        else:
            print("Invalid mobile number")
            return False  

    def is_email_address(self, val):
        val = str(val)
        # Check that it has exactly one @ sign, 
        # and at least one . in the part after the @
        if re.match(r'^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$', val):

            print("Valid email_address")
            return True
        else:
            print("Invalid email_address")
            return False  
    
        
    pass

# ###########
# Main method
# ###########

# The main method is only executed when the file is 'run' (not imported in another file)

if __name__ == '__main__':
    # Instead of writing separate test scripts, could write them here
    # The test scripts would not be executed when the file is imported into another one
    pass        