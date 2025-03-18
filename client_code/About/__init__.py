from ._anvil_designer import AboutTemplate
from anvil import *
# from ..Home import Home


class About(AboutTemplate):
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
  
  def shop_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    from ..Shop import Shop
    shop = Shop()
    open_form(shop)

  def cart_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    from ..Cart import Cart
    cart = Cart()
    open_form(cart)

