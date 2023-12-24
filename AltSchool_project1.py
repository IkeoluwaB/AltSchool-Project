import uuid 
from datetime import datetime,timezone


class Expense:
    def __init__(self,id, title ,amount):
        """
        This initializes the expense atrributes 
        """
        self.id = (str(uuid.uuid4()))
        self.title = title
        self.amount = amount 
        self.created_at = datetime.utcnow()
        self.upated_at= datetime.utcnow()
        

    def update(self, title = None, amount = None):
        """
        This method updates the expense details
        """
        if title is not None:
            self.title = title
        if amount is not None:
            self.amount = amount
        self.updated_at = datetime.utcnow()
        
    def to_dict(self):
        """
        This method returns the expense instance in representation of a dictionary
        """
        return{
            "id":self.id,
            "title": self.title,
            "amount":self.amount,
            "created_at": self.created_at,
            "updated_at": self.upated_at
        }
    



class ExpenseDatabase:
    def __init__(self): 
        """
        This intializes the Expense Database instance
        """
        self.database = []

    def add_expense(self, expense):
        """
        This method adds an expense to the database
        """
        self.database.append(expense)
        return f"{expense} has been added successfully"

    def remove_expense(self,id):
        """
        This method removes an expense to the database
        """
        
        self.database = [expense for expense in self.database if expense.id != id]
        print(f"Expense with id{id} has been removed!")

    def get_expense_by_id(self, id):
        """
        This method gets an Expense by id 
        """
        return[expense for expense in self.database if expense.id == id]
        
    
    def get_expense_by_title(self, title):
         """
        This method gets an Expense by title
        """
         return[expense for expense in self.database if expense.title == title]


    def to_dict(self):
        """
        This method returns the expenses in the database in a list of dictionaries
        """
        return[expense.to_dict() for expense in self.database]
    