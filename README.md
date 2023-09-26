# Debate Team Gone Wild and the Pundit Love It 🙌 🙌 🙌
## An experiment in agents with memories and the virtual pundits that judge them.

In this project four agentic athletes will engage in a discussion around a topic that will hopefully be programatically generated by the LLM itself before the debate kicks off. Utilizing the LangChain Library the project will have two parts. A debate without a moderator in which the participants exchange thoughts on a topic until a lexical stop word is reached or a number of rounds of discourse. Pundit analysts will also evaluate the discourse as it progresses through the use of Langchain agents and Tool implementations. I'll use NLTK or perhaps a HF Transformers based text classifier for sentiment analysis or even topic/keyword identification.

It would be nice if I could work out how to add a scoring system that is not completely crippled by being implemented by a deterministic machine rather than the wonderful world of humans. Eg. How do you code for a logical fallacy? How do I handle hallucinations.

Questions and their responses will be stored with tags on MongoDB. Summaries of each will be vectorized and upserted to Pinecone for the exercise. Though I am looking for more interesting things to do with the information generated and collected.

Feature Goals as at September 26 2023:
- 4 agents are generated with allocated temperaments
- They engage in a debate with no moderator etc. Their opinion on a subject is also randomly picked.
- Questions are are added or popped off the stack depending on the state of the game.
- Autogenerate questions for when the arena runs dry
- Build a MongoDB environment for storing question and answer information
- Synchronize high value summarises into Vector Databased (Using either Chroma or Pinecone)
- An event monitor will detect when a questoin is best suited to be answered by a participant and they will engage. The basic behaviour right now is that the speaker is chosen randomly.
- 

Analysis Goals:
- A secondary suite will run which will be composed of Langchain agents that evaluate sentiment, provide criticism and score the debaters as the debate progresses.
- The analysis side will have access to Google etc for fact chacking and other key information.
- Each persona will be inception prompted to have a certain approach to critique etc
- Common topics will be identified by analyzing the database.

Any ideas or contributions are welcome - Nullzero


🤗🤗🤗

