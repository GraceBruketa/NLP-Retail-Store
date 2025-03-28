from ._anvil_designer import RowTemplate1Template
from anvil import *
import anvil.server
import stripe.checkout
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class RowTemplate1(RowTemplate1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def add_qty_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call(
    'insert_item',
    self.quantity.text,
    get_open_form().raise_event('x-refresh')
    )

  def quantity_show(self, **event_args):
    """This method is called when the Label is shown on the screen"""
    quantity = self.quantity.text
    anvil.server.call('increase_quantity',quantity)

