from ._anvil_designer import HomeTemplate
from anvil import *
import anvil.server
from ..About import About
from ..Cart import Cart
from ..Shop import Shop


class Home(HomeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def search_box_2_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    search = self.search_box_2.text
    items = anvil.server.call('procces_words',search)
    self.repeating_panel_1.items = items
    

  def main_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    home = Home()
    open_form(home)

  def home_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    """This method is called when the button is clicked"""
    home = Home()
    open_form(home)
  

  def shop_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    shop = Shop()
    open_form(shop)

  def cart_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    cart = Cart()
    open_form(cart)

  def about_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    about = About()
    open_form(about)

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form(cart)
  
    
    
