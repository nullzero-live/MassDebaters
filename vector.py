''' ChromaDB or PineCone still not sure at this stage

Data will either be summaries of or complete informatoin. The agents will have web access as well as other
API's so there is potential for novel discussion


TO DO: ALL THIS CODE WILL NEED TO BE REFACTORED TO WORK WITH THE CODE COLLECTED FROM THE CONVERSATIONS BETWEEN AGENTS.
PROBLEMS: MONITORING AND DECISION MAKING ABOUT CHANGE ALERTS ETC, CONSISTENT FORMATTING.'''

''' RETREIVAL FUNCTIONALITY: Grabbing semantically similar information based on it's stored Vector on the Pinecone servic

NOTES: I'd like to improve my understanding of distance and the ways in which these are implemented by the Vector Store
services for greater granularity and accuracy'''

import os
import csv
import datetime
import pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone

# find API key in console at app.pinecone.io
PINECONE_API_KEY = os.getenv('PINECONE_API_KEY') 
PINECONE_ENVIRONMENT = os.getenv('PINECONE_ENVIRONMENT')

pinecone.init(
    api_key=PINECONE_API_KEY,
    environment=PINECONE_ENVIRONMENT
)

index_name = "study-buddy"

if index_name not in pinecone.list_indexes():
    # we create a new index
    pinecone.create_index(
        name=index_name,
        metric='cosine',
        dimension=1536,  # 1536 dim of text-embedding-ada-002
    )

#Init Index
index = pinecone.GRPCIndex(index_name)
time.sleep(1)
index.describe_index_stats()

# get openai api key from platform.openai.com
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY') or 'OPENAI_API_KEY'

model_name = 'text-embedding-ada-002'

#Vector embedding data set when available
embed = OpenAIEmbeddings(
    model=model_name,
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

#Initialize using langchain helpers
text_field = "text"

# switch back to normal index for langchain
index = pinecone.Index(index_name)

vectorstore = Pinecone(
    index, embed.embed_query, text_field
)


''' RETRIEVAL FUNCTIONALITY'''

from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA


llm = ChatOpenAI(
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    model_name='gpt-3.5-turbo',
    temperature=0.3
)

# Retriever logic (ready for a query on the existing index)
qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vectorstore.as_retriever()
)

#Run a query and store locally
if query is None:
    query = input("What is your query? Please be specific to the topic")

#Data table formatted for csv
data = [
    ["timestamp", "topic", "content"]
]

#New request to vector database: Also, how to best label and utilize the data that is generated?
req = qa.run(query)

'''Need to add the logic so that live conversations are treated in the right way. Applies to MongoDB implementation'''
with open(f'debate-{datetime.now}.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    csvwriter.writerows(req)
