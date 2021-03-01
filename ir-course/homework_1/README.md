# Tokenization & Stemming

# Run the program
* Type
```
python3 main.py --path PATH_TO_CRANFIELD_DIRECOTRY
```
* The only argument is **--path** that accepts the path to the CRANFIELD directory/folder.


## Tokenization
* Remove punctuations ,.!?\\<>
* Remove in-middle spaces
* Remove heading and tailing spaces
* Split sentences into tokens by whitepsace

Given the above algorithm, 
* The program ignores case sensitivity. Hence, "Apples" and "apples" are treated different.
* The program removes punctuations, except hyphen "-" and single-quote "'". Hence, term "middle-class" remains as it is. Similarly, possessive terms "university's" remains as it is.
* Periods are removed from text. Hence, acronyms, e.g. U.N. are converted into concatenated characters, e.g. UN.
* The tokenization is performed based on the followig steps: removing punctuations (except hyphen and single quote), stripping whitespace, and spllitting by whitespace into separate tokens. Then, the token frequency is counted by a dictionary. The number of tokens and the number of unique words are counted based on the dictionary's stats. Then, the dictionary sorted by the word count to compute the number of words occuring only once and to find the 30 most frequent words.

## Stemming
Apply the Porter algorithm to convert words to their stems.

## Data stuctures in-use
Dictionary is mainly used to store the frequency of words and stems in this program. This allows easy and fast lookup. Also, lists are used to store the number of distinct words and stems per document.
