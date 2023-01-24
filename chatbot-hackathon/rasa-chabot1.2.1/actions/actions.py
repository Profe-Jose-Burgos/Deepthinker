from typing import Any, Text, Dict, List, ClassVar, Optional
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from rasa_sdk.events import EventType



ALLOWED_PIZZA_SIZES = ["libras","kilos","litros","gramos","mililitros","kg","mg","lt","ltr","g",
"1","2","3","4","5","6","7","8","9","10","libra","kilo","litro","gramos","un","dos",
"tres","cuatro","cinco","seis","siete","ocho","nueve","diez"
]
prodb = ["manzana", "guineo", "pan", "pizza", "queso", "pollo","leche","cafe","huevos","ketchup"]

class ActionRememberPr(Action):
    def name(self) -> Text:
        return "action_obtiene_producto"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        current_product = next(tracker.get_latest_entity_values("product"))
        print("Current product es:", current_product)
        return [SlotSet("productos", current_product)]

class ActionComprobarPr(Action):
    def name(self) -> Text:
        return "action_verifica_el_producto"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        producto = tracker.get_slot("productos")
        print("El producto es: ",producto)
        if producto in prodb:
            msg = f"Hola bb"
            dispatcher.utter_message(text=msg)
            print("Yahoo nenecito bebelin")
        
        return []