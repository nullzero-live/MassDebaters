''' langchain core'''
import os
import openai
from typing import List, Dict
import logging
import random
from dotenv import load_dotenv
from pydantic import BaseModel
import wandb
wandb.disabled = True

import langchain
from langchain import OpenAI, LLMChain
from langchain.prompts.prompt import PromptTemplate
from langchain.agents import AgentType
from wandb.integration.openai import autolog

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

#Weights and Biases
autolog({"project":"agent-convo"})
wandb.init(project="agent-convo", mode="disabled")
wandb.login(key=os.getenv("WANDB_API_KEY"))


 #Q&A
def outcomes():
    question_history = ["What is the meaning of life?"]
    answers_history = []


def add_to_chat_history(dic_name, idx, metadata):
    dic_name['idx'].append(idx)
    dic_name['metadata'].append(metadata)
    return dic_name


class Results(BaseModel):
    questions: List[str]
    answers: List[str]




class ModelAction:
    def __init__(self):
        pass

    def question_generator(self, topic):
        #Add Output Parser
        llm = OpenAI(model="text-davinci-003")
        return llm.generate([f"give me a 2 sentence question at university level on {topic}"]*15)


class StudyBuddy:
    def __init__(self):
        pass

    def create_speakers(self, name, temperament, opinion, speaker_list=[]):
        self.name = name
        self.temperament = temperament
        if speaker_list == None:
            speaker_list = []
        else:
            speaker_list.append(self.name)
        
        return speaker_list
        
    def choose_speaker(self):
        speakers = [John,Jane,Sarah] #create_speakers()
        id = random.randrange(3)
        speaker = random.choice(speakers)
        return speaker
        
   
    
    def pose_question(self, context:str) -> str:
        question_count = 0
        llm = OpenAI(model="text-davinci-003")
        speaker = self.choose_speaker()
        speak_name = speaker.name
        speak_temp = speaker.temperament
        
        
        
        template = """The 3 participants are to choose a {question} and discuss it. The first question will be chosen at random. It will be at the level of a university student.Role of the {speaker}: When your name is called or your opinion is 'STRONGLY DISAGREE' you will pose a question based on the topic currently discussed
                    your tone, approach and civility will be based on your your {temperament}. 
                    
                    You can offer your question to an individual speaker"
                     
                      You will take into account the {history} provided.
                      
                      The outputs will be Name: ANSWER"""
        prompt_template = PromptTemplate(template=template, input_variables=["history", "temperament", "speaker", "question"])
        final_prompt = prompt_template.format(history=context, temperament=speak_temp, speaker=speak_name, question='what is the meaning of life?')
        output = llm(final_prompt)

        #ADD TO QUESTION CUE
        add_to_chat_history(Records.question_history, question_count, output)
        outcomes.answers_history.extend(output)
        try:
            questions.pop(0)
        except Exception:
            questions = []
        question_count += 1
        
        return output
        
    
    def answer_question(self, for_res) -> str:
        answer_count = 0
        speaker = self.choose_speaker()
        opinion = self.state_opinion(question_history[0], speaker.name)
        llm = OpenAI(model="text-davinci-003")
        speaker = self.choose_speaker()
        speak_name = speaker.name
        speak_temp = speaker.temperament
        
        
        to_respond = [question_history[0] if True else print("No such file")]

        template = """The 3 participants are to make a strong argument in {response} to a stated question. The question will be stated then answered. It will be at the level of a university student.Role of the {speaker}: When your name is called or your opinion is 'STRONGLY DISAGREE' you will pose a question based on the topic currently discussed
                    your tone, approach and civility will be based on your your {temperament}. You will make it clear if you agree or disagree and will have an {opinion}
                    
                    If you feel at all like you must answer you can also pose another question in the form

                    NEW_QUESTION:
                     
                      You will take into account the {history} provided.
                      
                      The outputs will be 
                      
                      Name: ANSWER"""
        
        prompt_template = PromptTemplate(template=template, input_variables=["history", "temperament", "speaker", "response", "opinion"])



        final_prompt = prompt_template.format(history="A brave new world", temperament=speak_temp, speaker=speak_name, response=to_respond, opinion=opinion)
        response = llm(final_prompt)
        
        answers.append(response)
        add_to_chat_history(Records.answer_history, answer_count, response)

        #Add additional questions
        template = """Search for the phrase NEW QUESTION: in {output}
                
                            If it does not exist, ignore the output
                            If it exists summarize the question and return it in the form:
                            
                            Question: """
        
    
        prompt_template = PromptTemplate(template=template, input_variables=["output"])
        final_prompt = prompt_template.format(output=response)
        new_questions = llm(final_prompt)
        
        question_history.append(new_questions)
        
        #ADD TO QUESTION CUE
        answers_history.extend(output)

        return response
        

    
    #Info is a dictionary with person and information
    def state_opinion(self, info:dict, speaker:dict) -> dict:
        a1 = StudyBuddy()
        speaker_raw = a1.choose_speaker().name,
        speaker = speaker_raw.name
        opinions = ["neutral", "positive", "negative", "STRONGLY DISAGREE"],
        opinion = opinions[random.randrange(4)]
        return opinion
       

    def store_dialogue(self,speech):
        dialogue = []
        return dialogue.append(speech)
        


class ChainsAgents:
    def __init__(self, questions, answers, prompt=None):
        self.prompt = prompt
        self.questions = questions
        self.answers = answers
    
    @classmethod
    def create_chain(cls, verbose:bool = False) -> LLMChain:
        prompt_template = ("""You are a student at a university in a discussion with two other students. You will have questions to ask.
                           Opinions on topics, and you will take actions""")
        prompt = PromptTemplate(template=prompt_template)

    def create_agent(self,AgentType=None) -> AgentType :
        print(api_key)
        llm=OpenAI(temperature=0.4, openai_api_key=api_key)
        return llm.predict("Am I sentient yet?")
    
    def store_dialogue(self,dialogue:List) -> List:
        return questions.append(dialogue)
    
    
    
class Records:
    question_history = {'idx': [], 'metadata': []}
    answer_history = {'idx': [], 'metadata': []}

def add_to_chat_history(dic_name, idx, metadata):
    dic_name['idx'].append(idx)
    dic_name['metadata'].append(metadata)
    """
    Adds an index and metadata to the chat_history dictionary.
    
    Parameters:
        idx (any): The index to add to the 'idx' key in chat_history.
        metadata (any): The metadata to add to the 'metadata' key in chat_history.  
    """
    
class AgentMonitor:
    def __init__(period, method):
        self.period = period
        self.method = method
    
    def monitor_opinion(speaker, response, opinion):
        pass

class ConversationModerator:
    def __init__(turn, penalise, score):
        pass





#agent1 = ChainsAgents("John is an affable gentlemen")
#print(agent1.create_agent())

John = StudyBuddy()
Jane = StudyBuddy()
Sarah = StudyBuddy()
#Jane = StudyBuddy(List(questions), List(answers))
#Sarah = StudyBuddy(List(questions), List(answers))

John.create_speakers(name="John", temperament="Aggressive", opinion=None)
Jane.create_speakers(name="Jane", temperament="Passive", opinion=None)
Sarah.create_speakers(name="Sarah", temperament="Rad", opinion=None)

i = StudyBuddy()
j = StudyBuddy()

print(a = i.pose_question("This is the opening debate"))
print(b = j.answer_question(a))

'''class DataProceeing:
    define 
    dataset = {}



def main():
    if len(questions) == 0:
        #print("you will need input")
        pass
    
    config= config = {"lr": 0.0001, "bs": 16, "epochs": 5}'''


#Disable wandb autolog
wandb.finish()
autolog.disable()
