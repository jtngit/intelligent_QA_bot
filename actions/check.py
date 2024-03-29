from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, AllSlotsReset
import os

class ActionTopicsCheck(Action):
    def name(self) -> Text:
        return "topic_search_topic_check"



    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


            id_of_user = tracker.sender_id
            print(f"user id is ={id_of_user}")
            

            try:
                fo = open(f"{id_of_user}.topicsname", "r+")
                line = fo.read()
                fo.close()
            except:
                with open(f"{id_of_user}.topicsname","w") as file:
                    file.write('')
                    file.close()
                    fo = open(f"{id_of_user}.topicsname", "r+")
                    line = fo.read()
                    fo.close()

            print (line)
            search_topic= set(())
            for a in line.split(','):
                if a != '' :
                    search_topic.add(a)
            print("$$$$$$$$$$$$$$$")
            if line == '':
                dispatcher.utter_message(text="Hey!  searching from wiki? type - 'ok go'")
            else:
                dispatcher.utter_message(text="your topics :")
                for item in search_topic:
                    dispatcher.utter_message(item+ ',')
                dispatcher.utter_message(text="type: \n 'search' - search topics \n 'ask' - ask questions from the added documents \n 'delete' - delete a specific topic \n 'ok go' - add more topics \n 'clear'- remove all topics you are added")

            return []
            