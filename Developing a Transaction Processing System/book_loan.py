# student_enrolment_gui.py
# France Cheong
# 22/11/2018

# ########
# Packages
# ########
import tkinter as tk
from tkinter import messagebox

# #################################################
# Import any of your classes defined in other files
# #################################################

# Import all the GUI classes implementing each menu option
# e.g. StudentGUI, TutorGUI, CourseGUI, EnrolmentGUI
# Each GUI class will import the corresponding data access class 
# to communicate with the database
# The GUI classes also import a single Validation class containing 
# all necessary validation methods

# From file xxx.py import class Xxxx
from librarian_gui import LibrarianGUI
from borrower_gui import BorrowerGUI
#from supplier_gui import SupplierGUI # ==> Not implemented
#from purchase_order_gui import PurchaseOrderGUI

# Reports GUI
#from product_report_gui import ProductReportGUI
#from category_report_gui import CategoryReportGUI


# ################
# Global Constants 
# ################


# ####################
# Book loan Class
# ####################

class BookloanGUI():

    def __init__(self):   

        print("Creating Book loan GUI ...")

        self.current_gui = None # Reference to current GUI 

        # Step 1. Create main window of the application
        # 900x500 pixels in the middle of the screen
        # Can minimise to 0x0 pixels
        self.root = tk.Tk()
        self.root.title("Book loan System")
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        width = 900
        height = 600
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        print("Main window coordinates (width, height, x, y) :", 
              width, height, x, y)
        self.root.geometry('%dx%d+%d+%d' % (width, height, x, y))
        self.root.resizable(0, 0)

        # Step 2. Add a menu

        # Create a toplevel menu
        menubar = tk.Menu(self.root)

        # File menu (pulldown)
        # Create a pulldown menu
        filemenu = tk.Menu(menubar, tearoff=0)
        # Add menu items
        filemenu.add_command(label="Open", command="")
        filemenu.add_command(label="Save", command="")
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.root.quit)
        # Add pulldown menu to toplevel menu
        menubar.add_cascade(label="File", menu=filemenu)
       
        # Student menu (pulldown)
        # Create a pulldown menu
        librarian_menu = tk.Menu(menubar, tearoff=0)
        borrower_menu = tk.Menu(menubar, tearoff=0)
        # Add menu items
        # do not use self.create_student_gui()
        librarian_menu.add_command(label="Librarian", 
            command=self.create_librarian_gui) 
        # Add pulldown menu to toplevel menu
        menubar.add_cascade(label="Librarian", menu=librarian_menu)
      
        borrower_menu.add_command(label="Borrower", command=self.create_borrower_gui) 
        menubar.add_cascade(label="Borrower", menu=borrower_menu)

        # Product menu (pulldown)
        # Create a pulldown menu
        # product_menu = tk.Menu(menubar, tearoff=0)
        # Add menu items
        # product_menu.add_command(label="Product", 
        #     command=self.create_product_gui) 
        # Add pulldown menu to toplevel menu
        # menubar.add_cascade(label="Product", menu=product_menu)

        '''
        # Tutor menu (pulldown) ==> Not implemented
        # Create a pulldown menu
        tutor_menu = tk.Menu(menubar, tearoff=0)
        # Add menu items
        tutor_menu.add_command(label="tutor", 
            command=self.create_tutor_gui) 
        # Add pulldown menu to toplevel menu
        menubar.add_cascade(label="Tutor", menu=tutor_menu)
        '''

        # Display the menu
        self.root.config(menu=menubar)

        pass
            
    # Functions to create child frames 
    # when menu options are selected

    def create_librarian_gui(self):
        if self.current_gui:
            self.current_gui.destroy()

        librarian_gui = LibrarianGUI()
        self.current_gui = librarian_gui.create_gui(self.root)
        pass

    def create_borrower_gui(self):
        if self.current_gui:
            self.current_gui.destroy()

        borrower_gui = BorrowerGUI()
        self.current_gui = borrower_gui.create_gui(self.root)
        pass

# ###########
# Main method
# ###########

if __name__ == '__main__':
    """
    The main method is only executed when the file is 'run' 
    (not imported in another file)
    """

    # Instantiate the main application gui 
    # it will create all the necessary GUIs
    gui = BookloanGUI()

    # Run the mainloop 
    # the endless window loop to process user inputs
    gui.root.mainloop()
    pass        