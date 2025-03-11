from ._anvil_designer import MainTemplate
from anvil import *
import stripe.checkout
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Home import Home
from ..Shop import Shop
from ..Contact import Contact
from ..About import About
from ..Cart import Cart


class Main(MainTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # self.navigate(self.home_link, Home())
    self.cart_items = []
    # self.repeating_items_panel_ = app_tables.clothes()
    
    for link in [self.home_link_copy, self.shop_link_copy, self.about_link_copy, self.contact_link_copy, self.insta_link_copy, self.link_1_copy, self.cart_link_copy]:
      link.role = ['spaced-title', 'display-responsive']
    
    for link in [self.home_link, self.shop_link, self.about_link,  self.cart_link]:
      link.role = ['spaced-title', 'display-none-responsive']
    
  def add_to_cart(self, product, quantity):
    #if item is already in cart, just update the quantity
    for i in self.cart_items:
      if i['product'] == product:
        i['quantity'] += quantity
        break
    else:
      self.cart_items.append({'product': product, 'quantity': quantity})
    
  def navigate(self, active_link, form):
    for i in [self.home_link, self.shop_link, self.about_link, self.contact_link, self.cart_link]:
      i.foreground = 'theme:Primary 700'
    active_link.foreground = 'theme:Secondary 500'
    self.column_panel_1.clear()
    self.column_panel_1.add_component(form, full_width_row=True)

  def home_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    home = Home()
    open_form(home)


  def shop_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    shop = Shop()
    open_form(shop)

  def about_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    about = About()
    open_form(about)
    
  def contact_link_click(self, **event_args):
    """This method is called when the Link is shown on the screen"""
    contact = Contact()
    open_form(contact)

  def cart_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    cart = Cart()
    open_form(cart)

  def subscribe_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    email = self.subscribe_textbox.text
    if email:
      anvil.server.call('add_subscriber', email)
      self.subscribe_textbox.text = None
      Notification("Thanks for subscribing!").show()

  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    pass

  def searchInput_change(self, **event_args):
    """This method is called when the text in this text area is edited"""
    pass

  def searchBut_click(self, **event_args):
    """This method is called when the button is clicked"""
    
    search = self.searchInput.text
    alert(search)

  def searchInput_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    alert(event_args['sender'].text)
    
   
    anvil.server.call('procces_words',search)
    

 








