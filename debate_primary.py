''' langchain core'''
import os
import openai
from typing import List, Dict

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
class Outcomes:
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
        gen_text = llm.generate([f"give me a 2 sentence question at university level on {topic}"]*15)
        return gen_text.replace("\n", "")

class Speaker:
    def __init__(self, name, temperament, opinion=None):
        self.name = name
        self.temperament = temperament
        self.opinion = opinion
    

class StudyBuddy:
    speaker_list = []
    def __init__(self, speaker_list):
        self.speaker_list = []

    John = create_speakers(John, "Aggressive")
    Jane = create_speakers(Jane, "Balanced")
    Sarah = create_speakers(Sarah, "Meek")
 
    @classmethod
    def create_speakers(cls, names, temperament, opinion=None):
        # Ensure speaker_list is initialized
        if not hasattr(cls, 'speaker_list'):
            cls.speaker_list = []

        for i in group:
            speaker = Speaker(i, temperament, opinion)
            cls.speaker_list.append(speaker)

        return cls.speaker_list
            
    def choose_speaker(self):
        """
        Choose a random speaker from a list of speakers.
        
        Returns:
            str: The name of the chosen speaker.
        """
        # Create a list of speakers
        self.speakers = [John, Jane, Sarah] # create_speakers()
        
        # Choose a random speaker from the list
        self.speaker = random.choice(self.speakers)
        
        # Return the chosen speaker
        return self.speaker
            
    
    
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
        Outcomes.answers_history.extend(output)
        try:
            questions.pop(0)
        except Exception:
            questions = []
        question_count += 1
        
        return output
        
    
    def answer_question(self, for_res:str) -> str:
        answer_count = 0
        speaker = self.choose_speaker()
       
        speak_name = speaker.name
        speak_temp = speaker.temperament
        print(speak_name)
        print(type(speak_name))
        opinion = StudyBuddy.state_opinion(Outcomes.question_history[0], speaker=speak_name)
        print(opinion)
        llm = OpenAI(model="text-davinci-003")
    
        
        
        for_res = [Outcomes.question_history[0] if True else print("No such file")]

        template = """The 3 participants are to make a strong argument in {response} to a stated question. The question will be stated then answered. It will be at the level of a university student.Role of the {speaker}: When your name is called or your opinion is 'STRONGLY DISAGREE' you will pose a question based on the topic currently discussed
                    your tone, approach and civility will be based on your your {temperament}. You will make it clear if you agree or disagree and will have an {opinion}
                    
                    If you feel at all like you must answer you can also pose another question in the form

                    NEW_QUESTION:
                     
                      You will take into account the {history} provided.
                      
                      The outputs will be 
                      
                      Name: ANSWER"""
        
        prompt_template = PromptTemplate(template=template, input_variables=["history", "temperament", "speaker", "response", "opinion"])
        final_prompt = prompt_template.format(history="A brave new world", temperament=speak_temp, speaker=speak_name, response=for_res, opinion=opinion)
        response = llm(final_prompt)
        
        # Add to chat history
        Outcomes.answers.append(response)
        add_to_chat_history(Outcomes.answer_history, answer_count, response)

        #Add additional questions
        template = """Search for the phrase NEW QUESTION: in {output}
                
                            If it does not exist, ignore the output
                            If it exists summarize the question and return it in the form:
                            
                            Question: """
        
    
        prompt_template = PromptTemplate(template=template, input_variables=["output"])
        final_prompt = prompt_template.format(output=response)
        new_questions = llm(final_prompt)
        
        Outcomes.question_history.append(new_questions)
        
        #ADD TO QUESTION CUE
        Outcomes.answers_history.extend(output)

        return response
        

    
    #Info is a dictionary with person and information
    @classmethod
    def state_opinion(self, info:str, speaker:str) -> dict:
        speak_name = speaker
        opinions = ["neutral", "positive", "negative", "STRONGLY DISAGREE"],
        opinion = opinions[random.randrange(len(opinions))]
        speak_name.opinion = opinions
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
    return dic_name

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

#Jane = StudyBuddy(List(questions), List(answers))
#Sarah = StudyBuddy(List(questions), List(answers))

John.create_speakers(name="John", temperament="Aggressive", opinion=None)
Jane.create_speakers(name="Jane", temperament="Passive", opinion=None)
Sarah.create_speakers(name="Sarah", temperament="Rad", opinion=None)

i = StudyBuddy()
j = StudyBuddy()

a = i.answer_question("This is the opening debate")
print(a)




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
