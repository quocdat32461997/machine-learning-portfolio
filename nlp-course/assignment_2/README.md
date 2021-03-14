# README
The program is done to demonstrate how to compute the bigram probability with various smoothing methods: none, add-one-smoothing, and good-turing

## Running the program
Type
```
python3 main.py --type smoothing_type
```
that:
* **--type** specifies the *smoothing type: no-smoothing, add-one-smoothing, good-turing*, 

## Output example
```
python3 bigram.py --type no-smoothing

#Total word 68737, total vocabulary 7602, total bigram 66517
#Computing probability of test test
#test not in corpus
#no-smoothing: 0.00010183743835197929 * 0.0 = 0.0 
```

---

```
python3 bigram.py --type add-one-smoothing

#Total word 68737, total vocabulary 7602, total bigram 66517
#Computing probability of test test
#add-one-smoothing: 0.00010183743835197929 * 0.0001314233144959916 = 1.338381368799833e-08
```

---

```
python3 bigram.py --type good-turing

#Total word 68737, total vocabulary 7602, total bigram 66517
#Computing probability of test test
#good-turing: 0.00010183743835197929 * 0.2483575627283251 = 2.5292097983593635e-05 
```
