from ._anvil_designer import ShopTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
# from ..Home import Home


class Shop(ShopTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def main_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    from ..Home import Home
    home = Home()
    open_form(home)
  
  def home_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    from ..Home import Home
    home = Home()
    open_form(home)
  
  
  def cart_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    from ..Cart import Cart
    cart = Cart()
    open_form(cart)

  def about_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    from ..About import About
    about = About()
    open_form(about)

  def search_box_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    search = self.search_box.text
    item_list = anvil.server.call('procces_words',search)
    self.re
  