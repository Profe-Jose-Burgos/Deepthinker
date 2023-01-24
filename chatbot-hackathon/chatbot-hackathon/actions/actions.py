# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, ClassVar, Optional
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher



productosdb = {'manzana':'5', 'Guineo': '5', 'Pan': '5'}

usuariosdb = {'2345':'usuario1', '678910':'usuario2', '11121314':'usuario3'}


class GetUserId(Action):
     def name(self) -> Text:
         return "action_verifica_el_usuario"

     def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        actual_id = next(tracker.get_latest_entity_values("usuarios"), None)
            
        usuariosdb = {'2345':'usuario1', '678910':'usuario2', '11121314':'usuario3'}
            
            
        try:
            usuariosdb[actual_id]
            msg1 = f" usuario correcto"
            dispatcher.utter_message(text=msg1)
            print("Finalizar try")

            
        except:
            msg = f"Inserte un usuario correcto"
            dispatcher.utter_message(text=msg)
                



class Getpro(Action):
     def name(self) -> Text:
         return "action_verificap"

     def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        actual_pr = next(tracker.get_latest_entity_values("productos"), None)
        try:
            productosdb[actual_pr]
            print("funciona")

        except:
            print("what")
            msg3 = f"Inserte un producto correcto"
            dispatcher.utter_message(text=msg3)

