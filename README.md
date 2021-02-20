# machine-learning-portfolio
This consists:
* [My timeline-based AI/ML/DL projects that I have worked on](#Projects)
* [My publications](#Publications)
* [Research papers that I have read and found interesting/practical (comments included)](#Papers that I have read and found useful (comments included))
* [My blogs/presentations/repos](#My blogs/presentations/repos)
* [Interview prep]()
* [What I have learnt](#What I have learnt)
---

## Projects
### - 2018
- [Intro to Machine Learning final project: Titanic Survival Prediction](https://github.com/quocdat32461997/Vacation2AI/blob/master/others/titanic_survival_rate_prediction.pdf) Trained and validated multiple ML algorithms using *Scikit-learn* (**SVM, Random Forest, Decision Tree, Logistic Regression**) on Titatnic dataset to predict the survival rate of Titatnic passengers

- [TCReepy](https://github.com/NCBI-Hackathons/TCRecePy)
  - Implemented **K-Nearest-Neighbor** to learn informative positions of proteins in amino acids to distinguish two types of T cell receptor hypervariable CDR3 sequences.
  - Achived: Best Desk to Best Bedside Award at 2018 Med U-Hack at UT Southwestern
  
### - 2019
- Neural Engineering research projects (2018 - 2019) advised by Prof. Tan Chin-Tuan at the Auditory Perception Engineering Laboratory, UT Dallas
- [Chest X-Ray Abnormal Detection](https://github.com/quocdat32461997/HealthCareAI_2019)
  - Applied multiple Transfer Learning models and hyper-parameter tuning to detect abnormalities in chest x-rays with 88% accuracy.
  - Achived: 1st Prize at the HealthCare AI 2019 Hackathon at Uni. of Texas at Dallas

### - 2020
- [MoCV](https://pypi.org/project/MoCV/)
  - An open-source Python package implementing **Computer Vision and Image Processing algorithms**.
 - [Senior Co-op Project: Interaction Tunning Tool](https://quocdat32461997.github.io/2020/05/05/interaction-tuning-tool-the-end_to_end-deep-learning_system-for-intent-detection.html)
    - Led a team of 6 engineers to build and deploy **an end-to-end Intent Extraction system** to **reduce the manual intent labeling tasks** (no coding and domain knowledge required) for Chatbot data preparation.
    - Contribution: utilized *StanfordNLP and Tensorflow* to develop a Deep Learning model (**LSTM-Attention + MLP**) to extract intents from raw utterances (**75% accuracy in development and 20% in deployment**). Unlike Google Dialogflow using a fixed intent list, our system forms VERB-NOUN intents that it does **not limit iteself by industry domains**
- [Name Entity Recognizer](https://github.com/quocdat32461997/NER) Implemented **BiLSTM-CRF** for **Name Entity Recognition**, built the data pipeline in *Tensorflow*, and deploy in *Flask*
- [Intent Classifier](https://github.com/quocdat32461997/intent_classifier)
    - Trained **Suport-Vector-Machine (SVM) and GradientBoosting** on text features extracted by **TF-IDF** for Intent-Classification tasks. Accuracy: 97% for training and 80% validation
- [CS6320: NLP final project - Borot](https://github.com/quocdat32461997/borot)
    -	Built **Chatbot Question & Answering** with *Flask, Scikit-learn, Tensorflow, and SQL*.
    - Implemented **Information Retrieval** with **Intent Classifier (SVM), Name-Entity-Recognizer (BiLSTM-CRF) and TF-IDF** to retrieve answers in response to questions. Implemented OOP to collect users’ QA queries for personalization.
- [Mask-RCNN](https://github.com/quocdat32461997/Mask_RCNN) - Implementation of Mask-RCNN in Tensorflow >= 2.0.0

### - 2021
- [Emorecom, ICDAR2021 Competition – Multimodal Emotion Recognition on Comic scenes](https://github.com/aisutd/emorecom)
    - Developed a multimodal Deep Learning model composed of CNN (ResNet, FaceNet) for visual features and RNN/BERT for textual features to detect emotion on comic scenes. Current AOU-RUC at 80%.
    - Utilized Tensorflow Data/string/image and OpenCV to build image/text augmentation pipeline and the TFRecord data pipeline.

---
  
## Publications
- [Neural Entrainment to Speech Envelope in response to Perceived Sound Quality](https://ieeexplore.ieee.org/abstract/document/8717078/)
  - Authors: **Dat Quoc Ngo**, Garret Oliver, Gleb Tcheslavski, Chin-Tuan Tan. 
  - Affiliation: Undergraduate Research Assistant at Auditory Perception Engineering Laboratory, UT Dallas
  - Abstract: The extent, to which people listen to and perceive the speech content at different noise levels varies from individual to individual. In past research projects, the speech intelligibility was determined by rating assessment, which suffered from variation of subjects' physical features. The purpose of this study is to investigate electroencephalography (EEG) by implementing multi-variate Temporal Response Function (mTRF) to examine neural responses to speech stimuli at different sound and noise levels. The result of this study shows that the front-central area of the brain clearly shows the envelope entrainment to speech stimuli.
  - Status: [Accepted to IEEE Neural Engineering Conference 2019](https://ieeexplore.ieee.org/abstract/document/8717078/)
- [Linear and Nonlinear Reconstruction of Speech Envelope from EEG](https://quocdat32461997.github.io/assets/linear_and_nonlinear_reconstruction_of_speech_envelope_from_eeg.pdf)
  - Authors: **Dat Quoc Ngo**, Garret Oliver, Gleb Tcheslavski, Fei Chen, Chin-Tuan Tan. 
  - Affiliation: Undergraduate Research Assistant at Auditory Perception Engineering Laboratory, UT Dallas
  - Abstract: Electroencephalography (EEG) is a non-invasive method of measuring cortical activities in association to speech communication. Recent studies have shown that EEG at multiple channels across head scalps were colinearly entrained to speech envelope. They were able to reconstruct speech envelope from EEG across scalp by using ridge regression. However, the predicted speech envelopes reconstructed by this linear model approach did not yield a high correlation when compared with the original speech envelopes. The outcome of those studies inspired us to explore a non-linear alternative with Deep Learning in reconstructing speech envelope from EEG. We proposed and developed an Encoder-Decoder model based on Convolutional (CONV) and Long-Short-Term-Memory (LSTM) layers to non-linearly reconstruct speech envelope from EEG. Our finding showed that correlation between the original speech envelope and the predicted speech envelope reconstructed with our model yielded a much higher value than the equivalence reconstructed with a linear model and a single-layer LSTM model. Our Encoder-Decoder model outperformed the regularized linear regression and the single-layer LSTM model with 134% and 21% improvement in correlation.
  - Status: [Preprint](https://quocdat32461997.github.io/assets/linear_and_nonlinear_reconstruction_of_speech_envelope_from_eeg.pdf)
- [Depression Detection: Text Augmentation for Robustness to Label Noise in Self-reprots](https://github.com/quocdat32461997/quocdat32461997.github.io/blob/master/assets/ACL_IJCNLP_2021___Final.pdf)
  - Authors: **Dat Quoc Ngo**, Aninda Bhattacharjee, Tannistha Maiti, Tarry Singh, Jie Mei
  - Affiliation: Visiting AI Researcher at deepkapha.ai
  - Abstract: With a high prevalence in both high and low-middle-income countries, depression is re- garded as one of the most common mental disorders around the globe, placing heavy burdens at a societal level. Depression severely impairs the daily functioning and quality of life of individuals of different ages, and may eventually lead to self-harm and suicide. In recent years, advancements have emerged in the fields of deep learning and natural language understanding, leading to improved detection and assessment of depression using methods including convolutional neural networks (CNNs) and bidirectional encoder representation from transformers (BERT). Nevertheless, previous work focused on data ac- quired through brain functional magnetic resonance imaging (fMRI), clinical screening or interviews, thus required labeling by domain experts. Therefore, in this study, we used the Reddit Self-reported Depression Diagnosis dataset, an uncurated text-based dataset, to enable detection of depression using easily accessible data. To reduce the negative impact of label noise on the performance of transformers-based classification, we proposed two data augmentation approaches, i.e., Negative Embedding and Empathy for BERT and DistilBERT, to exploit the usage of pronouns and affective, depression-related words in the dataset. As a result, the use of Negative Embedding improves the accuracy of the model by 31% compared with a baseline BERT and a DistilBERT, whereas Empathy underperforms baseline methods by 21%. Taken together, we argue that the detection of depression can be performed with high accuracy on datasets with label noise using various augmentation approaches and BERT.
  - Status: [in submission](https://github.com/quocdat32461997/quocdat32461997.github.io/blob/master/assets/ACL_IJCNLP_2021___Final.pdf)

---

## Papers that I have read and found useful (comments included)
### - Computer Vision
- [You Look Only ONce](https://arxiv.org/abs/1506.02640)
    - A unified Object Detection model consisting of DarkNet (Deep CNN) and Non-Max-Suppression at the output layer to group multiple bounding-boxes for the final object. Multi losses (object loss, class loss, and position loss) were computed.
- [Mask RCNN](https://arxiv.org/pdf/1703.06870.pdf)
    - An instance segmentation model composed of backbone (ResNet or Feature Pyramid Network), Region Proposal Network (simple CNN), and ROIAlign layer (Non-Max-Suppression) that both share hidden feature from the backbone.
    - Prone to overfitting since using Fully Connected layer for prediction.
- [Single Image Super Resolution based on a Modified U-NET with Mixed Gradient Loss](https://arxiv.org/pdf/1911.09428.pdf)
    - Introduction to loss functions (MGE and MixGE) for Super-Image-Super-Resolution problems using U-NET.
    - MSE, a common loss function is limited to learn errors based on pixel values, not the object curve (aka gradient error)
    - To solve gradient error introduced by Super-Resolution, Mean-Gradient-Error (MGE) utilizes Sobel operator to shapren curves of objects in predicted and true images which are then computed into difference-square
### - Natural Language Processing
- [Bidirectional LSTM-CRF Models for Sequence Tagging](https://arxiv.org/pdf/1508.01991v1.pdf)
    - Implementation of BiLSTM-CRF for Sequence Tagging tasks.
- [Attention is all you need](https://papers.nips.cc/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf)
    - Attention-based Seq-2seq model for state-of-the-art Neural Machine Translation
- [BERT: Pretraining of Deep Bidirectional Transformers for Langauge Understanding](https://arxiv.org/pdf/1810.04805.pdf)
    - A Deep Transformer-based Encoder pretrained on Wikipedia and BookCorpus allows easiy fine-tuning for downstream tasks.
    - Make text-based Transfer Learning feasible
    - Pros: effectively extract context
    - Cons: due to unsupervised pretraining tasks (i.e. random input masks) and individually attention-weight computing of each token across text, BERT ignores the sequential dependency of tokens (aka autogressive learning). Hence, BERT is not suitable for several text generation tasks such as Machine Translation.
- [XLNet: Generalized Autoregressive Pretraining for Language Understanding](https://arxiv.org/abs/1906.08237)
    -  XLNet (Autogressive Language Modeling) implements [Permutation Language Modeling](https://jmlr.org/papers/volume17/16-272/16-272.pdf) to generate permutation of token positions. This allows XLNet to learn dependency between a token and tokens before it only which represent for Autogressive Language Modeling (remember RNN and LSTM?).
- [Conditional BERT Contextual Augmentation](https://arxiv.org/pdf/1812.06705.pdf)
    - Proposed Conditional Mask Language Modeling (Conditional MSM) and a novel text data augmentation for labeled sntences to train Conditinoal BERT.
    - Idea : replace Segmentation Embedding with vocabulary-indexed labels when pretraining. 
    - Result : Conditional BERT is applicable for contextual data augmentation that improves BERT in several NLP tasks. Also, Conditional BERT could be used for text style transfer (replacing words w/o changing context).
- [DistilBERT, a distilled version of BERT: smaller, faster, cheaper, and lighter](https://arxiv.org/abs/1910.01108v1)
    - A smaller version of BERT with equivalent performance but less number of layers (6 in Distil BERT and 12 in BERT)
    - More practical for real-time inference
- [COMET: Commonsense Transformers for Automatic Knowledge Graph Construction](https://arxiv.org/pdf/1906.05317.pdf)
    - A Transformer-based model to generate/complete knowledge graphs.
    - Input encoding:
      - Consists of a 3-element tuple {subject, relation, object}
      - Unlike BERT w/ 3 embedings, COMET has 2 embeddings: tokens and positions
    - Architecture is similar to BERT, except the output layer of Transformer
- [Unsupervised Commonsense Question Answering with Self-Talk](https://arxiv.org/pdf/2004.05483.pdf)
    - To be added
- [Visual Question Answering To-read-list](https://github.com/zixuwang1996/VQA-reading-list)
    - Collection of to-read publications regarding Visual Question Answering
### - Others
#### Label Noise
- [Label Noise Types and Their Effects on Deep
Learning](https://arxiv.org/pdf/2003.10471.pdf)
    - Investigate the effects of label noise types to Deep Learning
    - Label noise is common in large-scale datasets or in active learning when samples are labeled by non-experts
- [Exploiting Context for Robustness to Label Noise in Active Learning](https://arxiv.org/pdf/2010.09066.pdf)
    - Proposed to exploit graphical context to improve CNN's performance in classification tasks.
---

## My blogs/presentations/contributions
- [Install Tensorflow on AMD GPUs](https://medium.com/analytics-vidhya/install-tensorflow-2-for-amd-gpus-87e8d7aeb812)
- [Blogs on Deep Learning](https://datngo-79115.medium.com/)
- [explore ml @DSC-UTD](https://github.com/DSC-UTDallas/explore-ml) - workshops over fundamental machine learning algorithms
- [Introduction to Python](https://github.com/pekkalacd/Introduction-to-Python)


## My machine-learning-engineer interview prep
- [ML Engineer Notes](https://docs.google.com/document/d/1mo1edEotJDpvT4fxL8-_VFBwS0e4OHqLnxd5I0yy-ps/edit?usp=sharing)

## What I have learnt
- [Natural Language Processing](./nlp-course)
- [Machine Learning](./ml-course)
- [Information Retrieval](./ir-course)
