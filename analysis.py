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
from debate_primary import Outcomes

class DebateMonitor:
    def __init__(self,db_uri, db_name):
        pass
    # recording of questions for long term storage will be in mongoDB
    def record_questions(self, question_id, speaker, text, position):
        self.question_data = {
            "id": question_id
            "text": text}

    def record_answers():
        return answer_data:VectorStore


class ArgumentAssessment:
    def __init__(self, debate_id, questions, answers):
        self.debate_id = debate_id
        self.debate_id = "???????"
        self.questions = Outcomes.question_history
        self.answers = Outcomes.answers_history
    
    def summary_analysis(self):
        def __init__(self):
            pass

    def logical_coherence(self):
        def __init__(self):
            pass
    
    def factcheck(self):
        def __init__(self):
            pass

class MetricsData:
    def __init__(self):
        pass
