# full_text_search
Full Text Search implemented in python

Searches through an XML of abstracts from wikipedia articles. An index of the data is built before searching the index for the search terms. **Tokenization** is done in order to build relevance of the individual terms that occur in the anstracts, while ignoring the very common words (*stopwords* corpus) occuring in the english language. 

Term frequency is maintained to ran the unordered list of documents and this is generated while creating the index of articles and abstracts. 

We'd also maintain an inverse document frequency in order to determine which of the documents have more relevance with respect to the search term; the more often the term occurs in the abstract the less it is relevant about the term.