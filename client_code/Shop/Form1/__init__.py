from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import stripe.checkout
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ... import globalVars
# from ... import Module1

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def BUY_button__click(self, **event_args):
    """This method is called when the button is clicked"""
    globalVars.addItems(self.item)
    alert( self.item['productDisplayName'] + " added to cart!") 
    
    
