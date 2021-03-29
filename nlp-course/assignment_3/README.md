# Assignment 3
To run the program, given the **.txt** file in the same directory with **main.py**, type
```
python3 main.py
```

## Part 1
Sampel output:
```
POS for the folowing text "Brainpower has the power ."
The final probability for the POS-Tag sequene is 3.8612161014384054e-11
Word Brainpower - Tag NNP
Word has - Tag VBZ
Word the - Tag DT
Word power - Tag NN
Word . - Tag .

POS for the folowing text "Janet will back the bill ."
Suggested post-tags (excluding out-of-vocab) are <s> MD RB DT NN . </s>
The final probabillity for the POS-Tag sequene is 0.0. Hence, the post-tags for the input text could not be determined

POS for the folowing text "I lost power yesterday ."
The final probability for the POS-Tag sequene is 1.9131130571030934e-14
Word I - Tag PRP
Word lost - Tag VBD
Word power - Tag NN
Word yesterday - Tag NN
Word . - Tag .
```

## Part 2
Sample output:
```
POS Tags for "Janet will back the bill"
Word Janet - Tag NNP - Prob 8.8544e-06
Word will - Tag MD - Prob 3.00406859104e-07
Word back - Tag VB - Prob 1.6085273254449313e-10
Word the - Tag DT - Prob 1.8161992521340702e-11
Word bill - Tag NN - Prob 2.0135707102213856e-14

POS Tags for "will Janet back the bill"
Word will - Tag MD - Prob 0.00018505859999999998
Word Janet - Tag NNP - Prob 4.73750016e-12
Word back - Tag RB - Prob 4.4539134004224e-16
Word the - Tag DT - Prob 1.0797240155413401e-17
Word bill - Tag NN - Prob 1.1970606475374611e-20

POS Tags for "back the bill Janet will"
Word back - Tag RB - Prob 0.000532746
Word the - Tag DT - Prob 1.2914904235206597e-05
Word bill - Tag NN - Prob 1.4318403040178357e-08
Word Janet - Tag NNP - Prob 4.398613413942791e-15
Word will - Tag MD - Prob 1.4923356072633679e-16
```
