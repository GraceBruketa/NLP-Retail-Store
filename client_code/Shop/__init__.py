from ._anvil_designer import ShopTemplate
from anvil import *
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
  