'''An agents role is to use their knowledge base and utilize tool to fact check debate statements as 
well as provide live commentary.

Asynchroncity may become an issue with Pythons lack of parallellim, to be observed. I'd also like to qualitatively define some 
of the scoring across the debate to apply quantitative scoring. With this progress perhaps the combination of LLM's and tools 
could come up with some interesting insights'''

import os
import random
from debate_primary import outcomes

#google_cse = os.getenv["GOOGLE_CSE_ID"]
#google_api_key = os.getenv["GOOGLE_API_KEY"]

# Import things that are needed generically
from langchain.agents import AgentType
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent
from langchain.tools import Tool
from langchain.utilities import GoogleSearchAPIWrapper
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder

api_key=os.environ["OPENAI_API_KEY"]
print(api_key)


llm = ChatOpenAI(temperature=0.4, openai_api_key=api_key)
#search = GoogleSearchAPIWrapper(google_api_key="", google_cse_id="")

#Chat based langchain models
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from langchain.agents import AgentExecutor

#LangChain Stuff
agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
tools = load_tools(["google-serper", "llm-math"], llm=llm)
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are very powerful assistant, but bad at calculating lengths of words."),
    ("user", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad"),
])


agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

from langchain.vectorstores.chroma import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains.summarize import load_summarize_chain
from langchain.document_loaders import PyPDFLoader


from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
)
human_message_prompt = HumanMessagePromptTemplate(
        prompt=PromptTemplate(
            template="""What are the congruent and contrasting points of the discussion.
              Questions:{questions}
              Answers: {answers}
              
              Be brutally honest and provide appropirate feedback.
              Based on the format
              Feedback: """,
            input_variables=["questions", "answers"],
        )
    )
human_message_prompt.format([question_history, answers_history])


chat_prompt_template = ChatPromptTemplate.from_messages([human_message_prompt])
chat = ChatOpenAI(temperature=0.5)
chain = LLMChain(llm=chat, prompt=chat_prompt_template)
print(chain.run())

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
agent_executor.invoke("input": f"""critically evaluate this argument with your own perspective"
                                        Question: {questions}
                                        Answer: {answer}""")

    





