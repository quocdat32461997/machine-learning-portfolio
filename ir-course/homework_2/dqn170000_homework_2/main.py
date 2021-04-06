"""
Author: Dat Quoc Ngo
NET-ID: dqn170000
Date: April. 5, 2021
File: main.py - execution in homework 2
"""

# import dependencies
import os
import re
import sys
import nltk
import time
import argparse
from nltk.stem import WordNetLemmatizer
from collections import defaultdict

nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()

def _compute_m(input):
	"""
	_comput_m - function to compute the measure m of a stem based on the alternate vowel-consonane sequences
	Inputs:
		- input : str
			Words to be stemmed
	Outputs:
		- input : str
			Stemmed words
	"""
	# initialize vowel-consonant matching pattern
	pattern = r'[aeiouy][qwrtpsdfghjklzxcvbnm]'
		
	# count frequency of vowel-consonant sequences
	m = len(re.findall(pattern = pattern, string = input))
	
	return m

def _remove_plural(input):
	"""
	_remove_plural - function to remove plural forms
	Inputs:
		- input : str
	Outputs:
		- input : str
	"""
	# ending w/ 'es'
	if input.endswith('es'):
		return input[:-2]
	# ending w/ ss -> skip
	elif input.endswith('ss'):
		pass
	# ending w/ s only
	elif input.endswith('s'):
		return input[:-1]
	return None

def _remove_ing_n_ed(input):
	"""
	_remove_ing_n_ed - function to remove -ing and -ed forms
	Inputs:
		- input : str
	Outputs:
		- input : str
	"""

	vowel_pattern = r'[aeiouy]'
	cvc_pattern = r'[a-z]*[b-df-hj-np-tv-z][aeiouy][b-df-hj-np-tvz]'

	# (m>0)eed -> ee
	if input.endswith('eed') and _compute_m(input[:-3]) > 0:
		return input[:-1]
	# (*v*)ed -> null 
	elif input.endswith('ed') and re.search(vowel_pattern, input[:-2]):
		input = input[:-2]
	# (*v*)ing -> null
	elif input.endswith('ing') and re.search(vowel_pattern, input[:-3]):
		input = input[:-3]

	# special cases
	# if ends with at or bl or iz
	if input.endswith('at') or input.endswith('bl') or input.endswith('iz'):
		return input + 'e'
	#end with consonant-vowel-consonant sequence
	elif _compute_m(input[:-3]) == 1 and re.search(cvc_pattern, input): 
		return input + 'e'
	# special case of double consonant
	elif len(input) > 2 and input[-1] == input[-2]:
		# if double-consonant is l, s, or z
		return input if re.search(pattern = r'[lsz]', string = input[-1]) else input[:-1]

	return None

def _substitue_y(input):
	"""
	_substitue_y - function to replace y with i
	Inputs:
		- input : str
	Outputs:
		- input : str
	"""
	vowel_pattern = r'[aeiouy]'

	# if ending w/ y and has a vowel in stem
	if input.endswith('y') and re.search(vowel_pattern, input[:-1]):
		return input[:-1] + 'i'

	return input

def _step1(input):
	"""
	_step1 - function to apply step1 rules
	Inputs:
		- input : str
		- m : int
			Measurement m of c.v.c. sequences
	Outputs:
		- input : str
	"""

	# remove plural forms
	temp = _remove_plural(input)
	if temp:
		return temp

	# remove -ed and -ing forms
	temp = _remove_ing_n_ed(input)
	if temp:
		return temp
	
	# substitue y w/ i
	temp = _substitue_y(input)
	if temp:
		return temp
	return input

def _step2(input):
	"""
	_step2 - function to apply step2 rules
	Inputs:
		- input : str
		- m : int
			Measurement m of c.v.c. sequences
	Outputs:
		- input : str
	"""
	# ational -> ate
	if input.endswith('ational') and _compute_m(input[:-7]) > 0:
		return input[:-1 * len('ational')] + 'ate'
	# tional -> tion
	elif input.endswith('tional') and _compute_m(input[:-6]) > 0:
		return input[:-1*len('tional')] + 'tion'
	# enci -> ence
	elif input.endswith('enci') and _compute_m(input[:-4]) > 0:
		return input[:-1] + 'e'
	# anci -> ance
	elif input.endswith('anci') and _compute_m(input[:-4]) > 0:
		return input[:-1] + 'e'
	# izer -> ize
	elif input.endswith('izer') and _compute_m(input[:-4]) > 0:
		return input[:-1]
	# abli -> able
	elif input.endswith('abli') and _compute_m(input[:-4]) > 0:
		return input[:-1] + 'e'
	# alli -> al
	elif input.endswith('alli') and _compute_m(input[:-4]) > 0:
		return input[:-2]
	# entli -> ent
	elif input.endswith('entli'):
		return input[:-2]
	# eli -> e
	elif input.endswith('eli') and _compute_m(input[:-3]) > 0:
		return input[:-2]
	# ousli -> ous
	elif input.endswith('ousli') and _compute_m(input[:-5]) > 0:
		return input[:-2] + 's'
	# ization -> ize
	elif input.endswith('ization') and _compute_m(input[:-7]) > 0:
		return input[:-5] + 'e'
	# ation -> ate
	elif input.endswith('ation') and _compute_m(input[:-5]) > 0:
		return input[:-3] + 'e'
	# ator -> ate
	elif input.endswith('ator') and _compute_m(input[:-5]) > 0:
		return input[:-2] + 'e'
	# alism -> al
	elif input.endswith('alism') and _compute_m(input[:-5]) > 0:
		return input[:-3]
	# iveness -> ive
	elif input.endswith('iveness') and _compute_m(input[:-7]) > 0:
		return input[:-4]
	# fulness -> ful
	elif input.endswith('fulness') and _compute_m(input[:-7]) > 0:
		return input[:-4]
	# ousness -> ous
	elif input.endswith('ousness') and _compute_m(input[:-7]) > 0:
		return input[:-4]
	# aliti -> ali
	elif input.endswith('aliti') and _compute_m(input[:-5]) > 0:
		return input[:-3]
	# iviti -> ive
	elif input.endswith('iviti') and _compute_m(input[:-5]) > 0:
		return input[:-3] + 'e'
	# biliti -> ble
	elif input.endswith('biliti') and _compute_m(input[:-6]) > 0:
		return input[:-5] + 'le'
	return input

def _step3(input):
	"""
	_step3 - function to apply step2 rules
	Inputs:
		- input : str
	Outputs:
		- input : str
	"""
	# icate -> ic
	if input.endswith('icate') and _compute_m(input[:-5]) > 0:
		return input[:-3]
	# ative -> null
	elif input.endswith('ative') and _compute_m(input[:-5]) > 0:
		return input[:-5]
	# alize -> al
	elif input.endswith('alize') and _compute_m(input[:-5]) > 0:
		return input[:-3]
	# iciti -> ic
	elif input.endswith('iciti') and _compute_m(input[:-5]) > 0:
		return input[:-3]
	# ical -> ic
	elif input.endswith('ical') and _compute_m(input[:-4]) > 0:
		return input[:-2]
	# ful -> null
	elif input.endswith('ful') and _compute_m(input[:-3]) > 0:
		return input[:-3]
	# ness -> null
	elif input.endswith('ness') and _compute_m(input[:-4]) > 0:
		return input[:-4]

	return input

def _step4(input):
	"""
	_step4 - function to apply step4 rules
	Inputs:
		- input : str
	Outputs:
		- input : str
	"""
	# al -> null
	if input.endswith('al') and _compute_m(input[:-2]) > 0:
		return input[:-2]
	# ance -> null
	elif input.endswith('ance') and _compute_m(input[:-4]) > 0:
		return input[:-4]
	# ence -> null
	elif input.endswith('ence') and _compute_m(input[:-4]) > 0:
		return input[:-4]
	# er -> null
	elif input.endswith('er') and _compute_m(input[:-2]) > 0:
		return input[:-2]
	# ic -> null
	elif input.endswith('ic') and _compute_m(input[:-2]) > 0:
		return input[:-2]
	# able -> null
	elif input.endswith('able') and _compute_m(input[:-4]) > 0:
		return input[:-4]
	# ible -> null
	elif input.endswith('ible') and _compute_m(input[:-4]) > 0:
		return input[:-4]
	# ant -> null
	elif input.endswith('ant') and _compute_m(input[:-3]) > 0:
		return input[:-3]
	# ement -> null
	elif input.endswith('ement') and _compute_m(input[:-5]) > 0:
		return input[:-5]
	# ment -> null
	elif input.endswith('ment') and _compute_m(input[:-4]) > 0:
		return input[:-4]
	# ent -> null
	elif input.endswith('ent') and _compute_m(input[:-3]) > 0:
		return input[:-3]
	# sion/tion -> null
	elif (input.endswith('sion') or input.endswith('tion')) and _compute_m(input[:-4]) > 0:
		return input[:-4]
	# ou -> null
	elif input.endswith('ou') and _compute_m(input[:-2]) > 0:
		return input[:-2]
	# ism -> null
	elif input.endswith('ism') and _compute_m(input[:-3]) > 0:
		return input[:-3]
	# ate -> null
	elif input.endswith('ate') and _compute_m(input[:-3]) > 0:
		return input[:-3]
	# iti -> null
	elif input.endswith('iti') and _compute_m(input[:-3]) > 0:
		return input[:-3]
	# ous -> null
	elif input.endswith('ous') and _compute_m(input[:-3]) > 0:
		return input[:-3]
	# ive -> null
	elif input.endswith('ive') and _compute_m(input[:-3]) > 0:
		return input[:-3]
	# ize -> null
	elif input.endswith('ize') and _compute_m(input[:-3]) > 0:
		return input[:-3]

	return input

def _step5(input):
	"""
	_step5 - function to apply step rules
	Inputs:
		- input : str
	Outputs:
		- input
	"""
	cvc_pattern = r'[a-z]*[b-df-hj-np-tv-z][aeiouy][b-df-hj-np-tvz]'

	# m > 1 and ending w/ 'e'
	if _compute_m(input[:-1]) > 1and input.endswith('e'):
		return input[:-1]
	# m == 1 and not *o
	elif _compute_m(input[:-3]) == 1 and not re.search(cvc_pattern, input):
		return input[:-1]
	# m > 1 and *d and *L -> single-letter
	elif _compute_m(input[:-2]) > 1 and input[-1] == input[-2] and input[-1] == 'l':
		return input[:-1]
	return input

def stem(input):
	"""
	stem - function to stem words to their roots
	Inputs:
		- input : str
			Token
	Outputs:
		- input : str
			Stem
	"""
	# step 1
	input = _step1(input)

	# step 2
	input = _step2(input)

	# step 3
	input = _step3(input)

	# step 4
	input = _step4(input)

	# step 5
	input = _step5(input)

	return input

def tokenize(text):
	"""
	tokenize - function to perform tokenization
	Inputs:
		- text : str 
	Outputs:
		- text : list of tokens
	"""
	# substitue puncutations with whitespace
	text = re.sub(pattern = '[,.!?\\<>]*', repl = '', string = text)

	# strip heading, tailing, and in-middle whitepsace
	text = re.sub(pattern = '\s\s+', repl = ' ', string = text)

	# strip heading and taling whitepsace
	text = text.strip()

	# split text into tokens by whitespace
	text = text.split(' ')
	
	return text

def process(text, pattern = '(<\/?[a-zA-Z]*>)|(\n)'):
	"""
	process - process SGML-styled text into preferred text
	Inputs:
		- text : raw text
		- pattern : matching pattern to remove SGML tags
	Outputs:
		- text : processed text
	"""

	# remove SGML tags
	text = re.sub(pattern = pattern, repl = '', string = text)

	return text

def lem(text):
    """
    Lemmatize text
    """

    return lemmatizer.lemmatize(text)

class DocNode(object):
    """
    DocNode - a unidirected linked list
    """
    def __init__(self,
            count:int = 1,
            doc_idx: int = -1,
            prev:'DocNode' = None,
            nxt:'DocNode' = None):
        self._count = count
        self._doc_idx = doc_idx
        self._prev = prev
        self._next = nxt

    def update(self, prev:'DocNode' = None, nxt:'DocNode' = None):
        self._prev = prev or self._prev
        self._next = nxt or self._next

class Index(object):
    def __init__(self):
        self._postings = defaultdict(list)
        self._doc_count = defaultdict(int)

    def build(self, docs):
        """
        Args:
            docs : list of Document(s)
        Returns: None
        """

        # loop over possting
        for doc_idx, doc in docs._dict.items():
            # loop over tookens
            for token in doc._dict.keys():
                self._postings[token].append(doc_idx)
                self._doc_count[token] += 1

    def invert(self):
        # sort keys alphabetical ordering
        temp_dict = sorted(self._postings.items(), key = lambda x:x[0])
        temp_doc_count = sorted(self._doc_count.items(), key = lambda x:x[0])
        self._postings = defaultdict(list)
        self._doc_count = defaultdict(int)
        for idx in range(len(temp_dict)):
            # get token
            token = temp_dict[idx][0]

            # save dict
            self._postings[token] = temp_dict[idx][-1]

            # save doc count
            self._doc_count[token] = temp_doc_count[idx][-1] 

        # split into dictionary and posting list
        postings = Posting(self._postings.copy())
        dictionary = Dictionary(self._doc_count.copy())

        return postings, dictionary

class Posting(object):
    def __init__(self, postings):
        self._postings = list(postings.values())

    def _gamma(self,inp):
        # to binary
        binary = str(bin(inp))[2:] # discard 0b at front

        # get offset
        offset = binary[1:]

        # get length
        offset_len = len(offset)
        unary = ''.join(['1'] * offset_len) + '0'

        # concat to gamma
        gamma = unary + offset

        return gamma

    def _delta(self, inp):
        # to binary
        binary = str(bin(inp))[2:]

        # get offset
        offset = binary[1:]

        # binary length
        bin_len = len(binary)

        # gamma of binary length
        gamma = self._gamma(bin_len)

        # concat to delta
        delta = gamma + offset

        return delta

    def compress(self, method):
        # initialize compressed postings
        self._compressed_postings = []
        self._postings.copy()

        # get encoding function
        encode_fn = self._gamma if method == 'gamma' else self._delta

        for i in range(len(self._postings)):
            prev = 0
            self._compressed_postings.append([])
            # compute gap and encode into gamma
            for j in range(len(self._postings[i])):
                # get gap
                id = self._postings[i][j]

                # encode
                self._compressed_postings[-1].append(encode_fn(id - prev))

                # update previous gap
                prev = id

class Dictionary(object):
    def __init__(self, doc_count):
        # indexing by 0
        self._doc_count = doc_count
        self._postings = {tok:v for tok, v in zip(doc_count.keys(), range(len(doc_count)))}
        self._dict_str = None
        self._dict = list(doc_count.keys())

    def compress(self, k, method):
        if method == 'blocking':
            pointers = [0]
            idx = 0
            self._dict_str = '' 
            while idx < len(self._dict):
                # get terms and update idx
                terms = self._dict[idx : min(idx + k, len(self._dict))]
                idx += 4

                # update dict_str
                self._dict_str += ''.join([str(len(term)) + term for term in terms])
                pointers.append(len(self._dict_str))
            # update term pointer
            self._dict = pointers[:-1]
        elif method == 'front-coding':
            pointers = [0]
            idx = 0
            self._dict_str = ''
            while idx < len(self._dict):
                # get common prefix
                prefix = self._dict[idx][:k]

                # get first term
                if k > len(prefix):
                    self._dict_str += str(len(prefix) - 1) + prefix[:-1] + '*' +  prefix[-1]
                else:
                    self._dict_str += str(k + 1) + prefix + '*' + self._dict[idx][k:]
                # update index
                idx += 1

                # add suffixes
                while idx < len(self._dict) and self._dict[idx].startswith(prefix):
                    suffix = self._dict[idx][len(prefix):]
                    self._dict_str += str(len(suffix)) + '^' + suffix
                    idx += 1

                # update pointer
                pointers.append(len(self._dict_str))
            # update term pointer
            self._dict = pointers[:-1]


class Documents(object):
    """
    Postings - class to map doc index to word frequency
    """
    def __init__(self):
        self._dict = defaultdict()
    def update(self, doc):
        self._dict[doc._doc_idx] = doc

class Document(object):
    """
    Document - an implementation of Poting list in Infomration Retrieval system
    """
    def __init__(self, doc_idx):
        super().__init__() # inherit from Index class
        self._max_freq = 0
        self._doclen = 0
        self._doc_idx = doc_idx
        self._dict = defaultdict(int)
    
    def parse(self,
            text,
            stop_words,
            proc_fn = None):
        """
        Parse and generate posting list
        Args:
            text : raw text
            stop_words : list
                List of stopwords
            proc_fn : callable function
                text-proc functions such as None, lemmatize, or stem
        Returns: None
        """

        # proceess text
        text = process(text)

        # tokenize
        text = tokenize(text)

        # get doclen
        self._doclen = len(text)

        # justify proc_fn
        proc_fn = proc_fn if proc_fn else lambda inp: inp
        
        # compute word frequency
        for token in text:
            # apply text_proc
            token = proc_fn(token)
            
            # remove stopwords
            if token in stop_words:
                continue
            
            # count valid word frequenccy
            self._dict[token] += 1

            # find frequency of the most frequnt term/stem in doc
            self._max_freq = self._dict[token] if self._dict[token] > self._max_freq\
                    else self._max_freq
        
def main(args):
    """
    Implement Single-Pass In-Memory Indexing
    """

    # retrieve list of text files
    files = os.listdir(args.path)
    files = [os.path.join(args.path, x) for x in files]

    # get stop words
    with open('./stop_words.txt') as file:
        stop_words = file.read().split()

    # construct index
    print('Index Construction')

    # start timing for building index-1
    tic = time.perf_counter()
    # build index with lemmas
    lem_docs = Documents()
    for file, f_idx in zip(files, range(1, len(files) + 1)):
        # read text
        with open(file) as f:
            text = f.read()

        # parse
        doc = Document(doc_idx = f_idx)
        doc.parse(text, stop_words, proc_fn = lem)
        lem_docs.update(doc)

    ## merge into big index
    lem_index = Index()
    lem_index.build(lem_docs)
    lem_posting, lem_dict = lem_index.invert()

    # end timeing
    toc = time.perf_counter()
    print("Time for building index-1 with compressing is {}".format(toc - tic))

    # size of index-1 uncompressed
    print("Size of the index version-1 uncompressed is {} bytes".format(
        sys.getsizeof(lem_posting._postings) + sys.getsizeof(lem_dict._dict)))

    # compressd dictionary
    lem_dict.compress(k = 4, method = 'blocking')

    # compress posting list
    lem_posting.compress(method = 'gamma')

    # size of index-1 compressed
    print("Size of the index version-1 compressed is {} bytes".format(
        sys.getsizeof(lem_posting._compressed_postings) + sys.getsizeof(lem_dict._dict)))

    # number of postings
    print("Number of postings in the version-1 index is {}".format(
        len(lem_posting._postings)))

    #**************************

    # start timeing for building index-2
    tic = time.perf_counter()

    # build index with stems
    stem_docs = Documents()
    for file, f_idx in zip(files, range(1, len(files) + 1)):
        # read text
        with open(file) as f:
            text = f.read()

        # parse
        doc = Document(doc_idx = f_idx)
        doc.parse(text, stop_words, proc_fn = stem)
        stem_docs.update(doc)

    ## merge to a big index
    stem_index = Index()
    stem_index.build(stem_docs)
    stem_posting, stem_dict = stem_index.invert()

    # size of the index-2 uncompressed
    print("Size of the index version-2 uncompressed is {} bytes".format(
        sys.getsizeof(stem_posting._postings) + sys.getsizeof(stem_dict._dict)))

    # end timing
    toc = time.perf_counter()
    print("Time for building index-2 with compressing is {}".format(toc - tic))

    # compress dictionary
    stem_dict.compress(k = 4, method = 'front-coding')

    # compress posting
    stem_posting.compress(method = 'delta')

    # size of the index-2 compressed
    print("Size of the index version-2 compressed is {} bytes".format(
        sys.getsizeof(stem_posting._compressed_postings) + sys.getsizeof(stem_dict._dict)))

    # number of postings
    print("Number of postigns in the version-1 index is {}".format(
        len(stem_posting._postings)))

    #********************
    # testing
    tests = ['Rynolds', 'NASA', 'Prandtl', 'flow', 'pressure', 'boundary', 'shock']
    # lemma
    for test in tests:
        # process text
        _test = lem(test)

        # display result
        print("Test in lemma {}: Document frequency = {} Term-frequency in documents = {} Inverted length = {} bytes"\
                .format(_test,
                    lem_index._doc_count[_test],
                    [lem_docs._dict[x]._dict[_test] for x in lem_index._postings[_test]],
                    0 if not _test in lem_dict._postings else sys.getsizeof(lem_posting._postings[lem_dict._postings[_test]])))

        # process text
        _test = stem(test)
        # display result
        print("Test in stem {}: Document frequency = {} Term-frequency in documents = {} Inverted len    gth = {} bytes"\
                .format(_test,
                    stem_index._doc_count[_test],
                    [stem_docs._dict[x]._dict[_test] for x in stem_index._postings[_test]],
                    0 if not _test in stem_dict._postings else sys.getsizeof(stem_posting._postings[stem_dict._postings[_test]])))

    # doclen and max_tf for the first 3 entries
    for id, doc in list(lem_docs._dict.items())[:3]:
        print("In lemma posting list, the entry {} has doc_length = {} and max_tf = {}".format(id, doc._doclen, doc._max_freq))

    for id, doc in list(stem_docs._dict.items())[:3]:
        print("In stem posting list, the entry {} has doc_length = {} and max_tf = {}".format(id, doc._doclen, doc._max_freq))

    # stem with largest df from stem 2 and dictionary term with lowest df
    _stem = sorted(stem_dict._doc_count.items(), key = lambda x:x[-1], reverse = True)[0]
    print("Stem '{}' has the largest document frequency {} from index 2".format(_stem[0], _stem[-1]))
    _dict_term = sorted(stem_dict._doc_count.items(), key = lambda x:x[-1])[0]
    print("Dictionary term {} has the lowest document frequency {} from index 2".format(_dict_term[0], _dict_term[-1]))

    # document with largest max_tf and doc length
    _doc = sorted([(id, doc._max_freq) for id, doc in stem_docs._dict.items()],
            key = lambda x:x[-1], reverse = True)[0]
    print("Document '{}' has the largest max_tf {} from index 2".format(_doc[0], _doc[-1]))
    _doc = sorted([(id, doc._doclen) for id, doc in stem_docs._dict.items()],
            key = lambda x:x[-1], reverse = True)[0]
    print("Document '{}' has the largest doclen {} from index 2".format(_doc[0], _doc[-1]))

if __name__ == '__main__':
    # initialize argument parser
    parser = argparse.ArgumentParser(description = 'Argument parser for homework 1')

    # add arguments
    parser.add_argument('--path', default = './Cranfield', type = str)

    # execute main
    main(parser.parse_args())
