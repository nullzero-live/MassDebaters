''' Analysis tasks to evaluate the debate and provide feeback using LLM's and external tools
1. Sentiment analysis on each participats opinion on various topics.
2. Grouping of topics that come up through the random generation of new questions
3. Who knows?

'''
import os
from dotenv import load_dotenv, find_dotenv`
import nltk
import pymongo
from datetime import datetime

class DebateMonitor:
    def __init__(self,db_uri, db_name):
        pass

    def record_questions(self, question_id, speaker, text, position):
        self.question_data = {
            "text": text,

        }
    
    def record_answers():
        answer_data:VectorStore,
