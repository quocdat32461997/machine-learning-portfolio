"""
Author: Dat Quoc Ngo
NET-ID: dqn170000
Date: Feb. 19, 2021
File: main.py - execution in homework 1
"""

# import dependencies
import os
import re
import argparse
from collections import defaultdict

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
    return text

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
        self._posting = defaultdict()
        self._heads = defaultdict()        

    def merge_index(self, postings):
        """
        Args:
            postings : list of Posting(s)
        Returns: None
        """
        def _merge(token, doc):
            if not token in self._posting:
                self._posting[token] = doc
                return None

            head = self._posting[token]
            while(head._next):
                head = head._next
            head._next = doc
            return None

        # loop over possting
        for post in postings:
            # loop over tookens
            for token, doc in post._posting.items():
                # merge posting
                _merge(token, doc)

        # sort keys alphabetical ordering
        temp_posting = sorted(self._posting.items(), key = lambda x:x[0])
        self._posting = defaultdict()
        for k,v in temp_posting:
            self._posting[k] = v
        # testing
        #print(self._posting['while']._doc_idx, self._posting['while']._next._doc_idx)

class Posting(Index):
    """
    Posting - an implementation of Poting list in Infomration Retrieval system
    """
    def __init__(self, doc_idx):
        super().__init__() # inherit from Index class
        self._max_freq = 0
        self._doclen = 0
        self._doc_idx = doc_idx
    
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
        block = defaultdict(int)
        for token in text:
            # apply text_proc
            token = proc_fn(token)
            
            # remove stopwords
            if token in stop_words:
                continue
            
            # count valid word frequenccy
            block[token] += 1

            # find frequency of the most frequnt term/stem in doc
            self._max_freq = block[token] if block[token] > self._max_freq\
                    else self._max_freq
        
        # generate posting block
        for k,v in block.items():
           self._posting[k] = DocNode(count = v, doc_idx = self._doc_idx) 
        del block

def main(args):
    """
    Implement Single-Pass In-Memory Indexing
    """
    # retrieve list of text files
    files = os.listdir(args.path)
    files = [os.path.join(args.path, x) for x in files]

    # get stop words
    stop_words = []

    # build index with lemmas
    postings = []
    for file, f_idx in zip(files, range(1, len(files) + 1)):
        # read text
        with open(file) as f:
            text = f.read()

        # parse
        postings.append(Posting(doc_idx = f_idx))
        postings[-1].parse(text, stop_words, proc_fn = lem)
    ## merge into big index
    lem_index = Index().merge_index(postings)
    del postings

    # build index with stems
    postings = []
    for file, f_idx in zip(files, range(1, len(files) + 1)):
        # read text
        with open(file) as f:
            text = f.read()

        # parse
        postings.append(Posting(doc_idx = f_idx))
        postings[-1].parse(text, stop_words, proc_fn = stem)

    ## merge to a big index
    stem_index = Index().merge_index(postings)
    del postings

if __name__ == '__main__':
    # initialize argument parser
    parser = argparse.ArgumentParser(description = 'Argument parser for homework 1')

    # add arguments
    parser.add_argument('--path', default = './Cranfield', type = str)

    # execute main
    main(parser.parse_args())
