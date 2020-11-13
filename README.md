# Vacation2AI
Collections of :
* Machine Learning Interview Prep
* Interesting research papers
* My Machine Learning and Deep Learning implementations

Modules:
* Computer Vision
* Natural Language Processing/Understanding
* Other

---
## Machine Learning Interview Prep
[Link](./ml_interview_prep.md)

---

## Computer Vision
### Image Classification
#### Chest Disease Classification upon X-Rays
	- Fine-tune of VGG16 for Chest Disease Classification
	- Link: https://github.com/quocdat32461997/HealthCareAI_2019/blob/master/code-lab-3-chestxray8-vgg16.ipynb

### Object Detection
#### - Mask-RCNN
	- Implementation of Mask-RCNN in Tensorflow 2.0 for Object Detection
	- Link: https://github.com/quocdat32461997/Mask_RCNN

#### Pulications
	- [End-to-End Hierarchical Relation Extraction for Generic Form Understanding]()
	- [Mask-RCNN](https://arxiv.org/abs/1703.06870#:~:text=The%20method%2C%20called%20Mask%20R,CNN%2C%20running%20at%205%20fps.)
		* Includes Region Proposal Network (simple CNN) and ROIAlign layer (Non-Max-Suppression) that both shares hidden features from CNN backbone (ResNet or VGG)
		* Limits: Object Classification using Fully-Connect-Network (prone to overfitting and large computation cost).
	- [You Look Only Once](https://arxiv.org/abs/1506.02640)
		* A unified Object Detection model consisting of DarkNet (a Deep CNN) and Non-Max-Suppresion at output branches. 
		* Pros: simple and less computation than Mask-RCNN that object classification is produced by ConvNet layers.
	- [Single Image Super Resolution based on a Modified U-net with Mixed Gradient Loss](https://arxiv.org/pdf/1911.09428.pdf)
		* Introduction to loss functions (MGE and MixGE) for Super-Image-Super-Resolution problems using U-Net
		* MSE, a common loss function is limited to learn errors based on pixel values, not the object curve (aka gradient error).
		* To solve gradient error introduced by Super-Resolution, Mean-Gradient-Error (MGE) utilizes Sobel oeprator to shapren curves of objects in predicted and true images which are then computed into difference-square. 
---

## Natural Language Processing/Understanding

### Sequence Tagging
#### - BiLSTM-CRF
	- Implementatino of BiLSTM-CRF for Name-Entity-Recognition tasks. Accuracy: 95% for training
	- Full training and inference functions
	- Link: https://github.com/quocdat32461997/BiLSTM-CRF
	- Reference:
		* [Bidirectional LSTM-CRF Models for Sequence Tagging](https://arxiv.org/pdf/1508.01991v1.pdf)

### Intent Detection
#### - Intent Classifier
	- Implementation of SVM and GradientBoosting for TF-IDF text features for Intent-Classification tasks. Accuracy: 97% for training and 80% validation.
	- Link: https://github.com/quocdat32461997/intent_classifier
	- Reference:
		* [Stefan Larson, Anish Mahendran, Joseph J. Peper, Christopher Clarke, Andrew Lee, Parker Hill, Jonathan K. Kummerfeld, Kevin Leach, Michael A. Laurenzano, Lingjia Tang, and Jason Mars. 2019. An evaluation dataset for intent classification and out-of-scope prediction. In Proceedings of EMNLP-IJCNLP](https://archive.ics.uci.edu/ml/datasets/CLINC150)
	
### Chatbot
#### - Borot
	- A Chatbot using Intent-Classifier and NER models to parse users' requests and lookup answers from internal database or Google Search API.
	- Link: https://github.com/quocdat32461997/borot
	
### Publications
	- [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/abs/1810.04805)
		* State-of-art NLU technique utilizing Encoder-Decoder architecture of Multi-head Attention layers
		* Multi-head Attention is a stack of multiple Transformers (Scale-dot productions). Default BERT has 12-head attentions that means 12 Transformer layers (6 for Encoder and Decoder)
	- [XLNet: Generalized Autoregressive Pretraining for Language Understanding](https://arxiv.org/abs/1906.08237)
		* As BERT is pretraiend on MASK task, BERT ignores dependency between MASK tokens. 
		* Hence, XLNet (Autogressive Language Modeling) implements [Permutation Language Modeling](https://jmlr.org/papers/volume17/16-272/16-272.pdf) to generate permutation of token positions. This allows XLNet to learn dependency between a token and tokens before it only which represent for Autogressive Language Modeling (remember RNN and LSTM?).

---

## Others
#### - Tensorflow
[Link](https://github.com/quocdat32461997/Vacation2AI/blob/master/tensorflow/Tensorflow_Digit_Classifier.ipynb)
#### - PyTorch
[Link](https://github.com/quocdat32461997/Vacation2AI/tree/master/pytorch)
#### - Titanic Survival Prediction
	- Implementations and validations of multiple ML algorithms (SVM, Random Forest, Decision Tree, Logistic Regression) on Titanic dataset
	- Link: https://github.com/quocdat32461997/Vacation2AI/blob/master/others/titanic_survival_rate_prediction.pdf
### - Intro-to-nlp
	- [UTDallas - Human Language Technologies](https://github.com/quocdat32461997/intro-to-nlp)
