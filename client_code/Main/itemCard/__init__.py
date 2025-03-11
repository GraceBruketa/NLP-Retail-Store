from ._anvil_designer import itemCardTemplate
from anvil import *
import anvil.server
import anvil.image
import stripe.checkout
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class itemCard(itemCardTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    

    # Any code you write here will run before the form opens.
    print(f"self.item = {self.item}")
    image_media = URLMedia('https://images.dog.ceo/breeds/mastiff-english/2.jpg')
    # Media()
     self.image_1.source(image_media)
    
