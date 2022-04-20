from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import os
from . import first as k
from . import question as que

class ActionTopicsCheck(Action):
    def name(self) -> Text:
        return "nlu_start"



    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            search_question = tracker.get_slot("getquestion")
            id_of_user = tracker.sender_id
            print(f"user id is ={id_of_user}")
            try:
                doc_path='/Users/rasa_bot_with_nlu_ai'
                k.runstart(doc_path,id_of_user)
                k.doc_clean_and_tfidf(doc_path,id_of_user)


                #question = input("enter your Question:")
                #dispatcher.utter_message(text="enter your Question:\n")
                selected_sentences= que.questions(search_question,id_of_user)
                #print("Answer : {}" .format(selected_sentences[0]))
                a=0
                j=0
                for val in selected_sentences:
                    a = a+1
                print("search_question is: {}".format(search_question))
                dispatcher.utter_message(text="\n\nAnswers :\n" )

                while(j<a):
                    if (j<5):
                        print(selected_sentences[j])
                        dispatcher.utter_message(selected_sentences[j])
                        j= j+1
                    else:
                        break

            except:
                dispatcher.utter_message(text=f"please check your question is that valid one!!!!")

            dispatcher.utter_message(text=f"type: \n 'search' - search topics \n 'ask' - ask questions from the added documents \n 'delete' - delete a specific topic \n 'ok go' - add more topics \n 'clear'- remove all topics you are added")
            return [SlotSet("getquestion", None)]
            