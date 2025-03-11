import anvil.stripe
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime
import stripe
import en_core_web_sm

import anvil.email

nlp = en_core_web_sm.load()
@anvil.server.callable
def add_message(name, email, message):
  app_tables.contact.add_row(name=name, email=email, message=message, date=datetime.now())
  anvil.email.send(from_name="Contact Form", 
                   subject="New Web Contact",
                   text=f"New web contact from {name} ({email})\nMessage: {message}")
  
@anvil.server.callable
def add_subscriber(email):
  app_tables.subscribers.add_row(email=email)
  
@anvil.server.callable
def add_order(charge_id, cart_items):
  app_tables.orders.add_row(charge_id=charge_id, order=cart_items)

@anvil.server.callable
def procces_words(text):
  # Process whole documents
  
  doc = nlp(text)

  noun_phrases = [chunk.text for chunk in doc.noun_chunks]
  promtVerbs = [token.lemma_.lower() for token in doc if token.pos_ == "VERB"]
  promtAdjectives = [token.text.lower() for token in doc if token.pos_ == "ADJ"]        # Surface form
  # adjectives_lemmas = [token.lemma_ for token in doc if token.pos_ == "ADJ"]  # Lemmatized form

  column_values = [{"id": row["id"], "Description": row["Description"],"points":0} for row in app_tables.items.search()]
  
  for val in column_values:
    doc = nlp(val['Description'])
    verbs = [token.lemma_.lower() for token in doc if token.pos_ == "VERB"]
    adjectives = [token.text.lower() for token in doc if token.pos_ == "ADJ"]
    verbPoint = len(set(promtVerbs) & set(verbs))
    abjectivePoint = len( set(adjectives) & set(promtAdjectives))
    val['points'] = abjectivePoint + verbPoint
    # ad point for noun phrases and nouns , andphares give more points
    
    
  sorted_column_values = sorted(column_values, key=lambda x: x['points'], reverse=True)
  print(sorted_column_values)
  print(noun_phrases)
  return sorted_column_values
  
  # print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])
  # # extract adjectives
  # print("Adjectives:", [token.text for token in doc if token.pos_ == "ADJ"])  # Surface form
  # # OR for lemmas (like verbs):
  # print("Adjectives (lemmas):", [token.lemma_ for token in doc if token.pos_ == "ADJ"])
  
  

  
