'''Using NLP tools to examine elements of the discourse between candidates'''
import nltk
import gensim
from transformers install pipeline
nltk.download("maxent_ne_chunker")
nltk.download("words")
from nltk.stem.porter import *
from nltk.stem import WordNetLemmatizer
import gensim
import gensim.parsing.preprocessing

#NLTK

class NLTKAnalysis:

    def __init__(self, text)
         self.text = text
    
    def extract_ne(self.text):
        ''' Named Entity Recognition is an NLP technique which highlights entities in text. Entities
        can vary depending on how the model was trained but include ideas like people PER, Places, Organizations.
        This will serve as another means of finding meaningful information from the debates and analysis'''
        
        words = word_tokenize(quote, language=language)
        tags = nltk.pos_tag(words)
        tree = nltk.ne_chunk(tags, binary=True)
        ne_out = set(" ".join(i[0] for i in t)
        for t in tree:
            if hasattr(t, "label") and t.label() == "NE":)
        
        return ne_out
    
   

    def topic_modelling(self, text):
         ''' 
         LDA extracts the main topics from a piece of text based on the words used and
         does a form of topic modelling. I hope to use it on the raw debates to find core topics that come up again
         and to evaluate if the LLM's are quite repetitive'''
        
         #Lemmatize
         stemmer = PorterStemmer()
         lemm = stemmer.stem(WordNetLemmatizer().lemmatize(text, pos='v'))
         proc_docs=[]
         for token in gensim.utils.simple_preprocess(lemm):

            if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 3:
                proc_docs.append(lemmatize_stemming(token))
        
                
        
        dictionary = gensim.corpora.Dictionary(proc_docs)

        bow_corpus = [dictionary.doc2bow(doc) for doc in proc_docs]
    
        lda_model =  gensim.models.LdaMulticore(bow_corpus, 
                                   num_topics = 8, 
                                   id2word = dictionary,                                    
                                   passes = 10,
                                   workers = 2)
        return lda_model
        
        

    
    def sentiment_analysis(self, text):
        sentiment_analysis = pipeline("sentiment-analysis")
        sentiment = pipeline(text)
        return sentiment 


#TRANSFORMERS

