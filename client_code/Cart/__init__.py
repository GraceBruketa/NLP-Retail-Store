from ._anvil_designer import CartTemplate
from anvil import *
# from ..Home import Home
from .. import globalVars


class Cart(CartTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.repeating_panel_1.items = globalVars.cartItems

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

  def about_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    from ..About import About
    about = About()
    open_form(about)

  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    print(globalVars.cartItems)

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass
  
