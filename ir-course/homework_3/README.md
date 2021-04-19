# Index Construction

## Run the program
* Type
```
# install nltk
pip3 install nltk

# execute program
python3 main.py --path PATH_TO_CRANFIELD_DIRECOTRY
```
* The only argument is **--path** that accepts the path to the CRANFIELD directory/folder.

## Code flow
* Each text file is processed by either lemmatizer or stemmer
* Stop-word are removed and not stored in dictionary. However, the stop-word occurences are counted to document length
* Each text file is then parsed into a **Document** object that holds document length, maximum frequency, and document id, and word frequency dictionary
* All **Document** objects are then merged together into a single **Index** object for either "lemma" or "stem"
* Then **Index** objects are inverted (alphebetically sorted). The returns of "invert" is 2 objects: **Posting** and **Dictionary** for the correponding posting list and dictionary
* Then **Posting** and ** Dictionary** objects are compressed based on the given requirements. The results of compression are stored into separate variables within the objects. This is done purposely because the retrieval mechanisms for compressed posting lists and dictionarys are not implemented yet.
* Finally, the program display results as requested below

## Results
- Time for building the version-1 and version-2 indics
```
Time for building index-1 with compressing is 3.0236922859999993
Time for building index-2 with compressing is 3.4592588490000002
```
* Comparison of version-1 and version-2 indices before and after compression
```
- version-1 index
Size of the index version-1 uncompressed is 437776 bytes
Size of the index version-1 compressed is 280168 bytes

- version-2 index
Size of the index version-2 uncompressed is 416016 bytes
Size of the index version-2 compressed is 231624 bytes
```
- Number of postings in  version-1 and version-2 indcies
```
Number of postings in the version-1 index is 27354
Number of postigns in the version-1 index is 25994
```
- Test results
	-- "Rynolds" has no result because the test word is not found in dictionary. This is due to differences in text-processing steps
```
Test in lemma Rynolds: Document frequency = 0 Term-frequency in documents = [] Inverted length = 0 byte
s
```
	-- "flow" has the following results
```
Test in lemma flow: Document frequency = 660 Term-frequency in documents = [1, 2, 2, 2, 2, 1, 3, 2, 1, 
1, 1, 2, 6, 3, 1, 1, 3, 1, 1, 3, 1, 3, 1, 3, 1, 4, 2, 2, 4, 2, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 2, 7
, 1, 1, 3, 1, 1, 1, 2, 2, 4, 3, 1, 4, 1, 3, 5, 2, 3, 4, 1, 3, 4, 3, 4, 4, 4, 3, 1, 1, 1, 1, 1, 4, 2, 2,
 5, 1, 1, 1, 2, 1, 5, 1, 2, 1, 2, 1, 1, 3, 1, 3, 2, 3, 1, 4, 3, 2, 1, 7, 1, 1, 2, 3, 2, 3, 1, 6, 3, 3, 
2, 2, 3, 3, 3, 3, 4, 1, 2, 5, 4, 1, 4, 1, 1, 2, 3, 3, 1, 4, 1, 2, 6, 3, 3, 6, 2, 2, 2, 2, 2, 3, 3, 5, 1
, 2, 1, 6, 2, 6, 5, 1, 2, 2, 1, 1, 1, 2, 2, 7, 1, 1, 7, 3, 3, 1, 6, 1, 1, 1, 2, 2, 2, 2, 1, 1, 4, 2, 2,
 1, 2, 6, 1, 2, 1, 6, 6, 2, 2, 4, 1, 4, 1, 4, 2, 1, 8, 2, 1, 2, 3, 2, 2, 2, 1, 2, 3, 5, 1, 1, 1, 3, 4, 
4, 2, 1, 5, 1, 2, 2, 1, 5, 1, 4, 1, 2, 1, 1, 2, 1, 5, 4, 3, 4, 1, 1, 3, 2, 1, 2, 3, 2, 1, 1, 1, 2, 4, 2
, 2, 1, 1, 7, 1, 1, 3, 2, 4, 1, 1, 2, 1, 2, 2, 3, 1, 1, 3, 1, 2, 2, 2, 1, 4, 4, 4, 3, 5, 4, 3, 8, 2, 1,
 3, 5, 7, 2, 2, 4, 2, 2, 1, 3, 2, 1, 1, 2, 1, 2, 2, 6, 1, 3, 3, 1, 1, 3, 1, 1, 1, 1, 8, 1, 2, 2, 6, 3, 
1, 2, 1, 4, 1, 1, 1, 2, 5, 7, 1, 3, 2, 1, 2, 1, 1, 2, 3, 4, 8, 1, 1, 3, 2, 1, 3, 1, 5, 2, 7, 1, 3, 4, 2
, 1, 11, 3, 6, 2, 3, 1, 3, 4, 2, 1, 1, 1, 1, 3, 2, 1, 2, 1, 2, 4, 3, 1, 1, 2, 3, 2, 2, 1, 2, 1, 3, 5, 1
, 1, 2, 3, 1, 2, 4, 2, 4, 4, 1, 3, 2, 2, 5, 1, 2, 2, 1, 4, 3, 1, 4, 2, 5, 1, 2, 4, 2, 3, 4, 2, 5, 3, 10
, 3, 4, 1, 1, 3, 1, 1, 6, 1, 3, 4, 1, 1, 1, 3, 1, 6, 3, 1, 2, 1, 1, 1, 1, 4, 2, 2, 1, 4, 2, 3, 2, 1, 7,
 3, 3, 1, 1, 1, 2, 4, 1, 3, 1, 1, 2, 1, 6, 1, 1, 1, 1, 1, 2, 4, 3, 4, 3, 2, 2, 4, 2, 6, 1, 5, 1, 1, 3, 
2, 3, 1, 5, 1, 2, 3, 1, 2, 9, 3, 2, 1, 1, 2, 1, 1, 2, 2, 2, 2, 4, 3, 2, 1, 1, 4, 1, 1, 2, 1, 2, 1, 1, 7
, 6, 3, 1, 2, 1, 4, 3, 1, 1, 4, 2, 6, 4, 4, 2, 4, 1, 3, 2, 4, 3, 1, 2, 3, 1, 2, 6, 2, 2, 3, 2, 3, 2, 5,
 1, 6, 3, 3, 1, 1, 1, 1, 5, 1, 7, 1, 2, 6, 3, 6, 1, 1, 3, 1, 1, 4, 2, 2, 4, 1, 2, 3, 3, 1, 2, 2, 2, 3, 
1, 2, 3, 1, 1, 2, 1, 2, 2, 1, 1, 1, 3, 1, 2, 1, 5, 1, 2, 1, 2, 1, 1, 1, 8, 2, 4, 2, 2, 2, 1, 2, 1, 1, 1
, 2, 2, 3, 3, 4, 1, 2, 2, 3, 2, 1, 2, 1, 3, 1, 4, 1, 6, 5, 1, 1, 1, 1, 1, 5, 2, 6, 3, 2, 4, 1, 1, 4] Inverted length = 5488 bytes
```
- The first 3 entries in the lemmand and stem posting lists has
```
In lemma posting list, the entry 1 has doc_length = 86 and max_tf = 5
In lemma posting list, the entry 2 has doc_length = 59 and max_tf = 3
In lemma posting list, the entry 3 has doc_length = 57 and max_tf = 2
In stem posting list, the entry 1 has doc_length = 86 and max_tf = 6
In stem posting list, the entry 2 has doc_length = 59 and max_tf = 3
In stem posting list, the entry 3 has doc_length = 57 and max_tf = 2
```
- From index 2, the stem with the largest document frequency and the dictionary term with the lowest ocument frequency 
```
Stem 'i' has the largest document frequency 1114 from index 2
Dictionary term 'density has the lowest document frequency 1 from index 2

```
- Document with the largest term frequency and document length
```
Document '695' has the largest max_tf 31 from index 2
Document '1163' has the largest doclen 617 from index 2
```
