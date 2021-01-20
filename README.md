# Vacation2AI
This consists:
* timeline-based AI/ML/DL projects that I have worked on
* Research papers that I have read and found interesting/practical
* Machine Learning Interview Prep

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
    - Contribution: utilized *StanfordNLP and Tensorflow* to develop a Deep Learning model (**LSTM-Attention + MLP**) to extract intents from raw utterances (**75% accuracy in development and 30% in deployment**). Unlike Google Dialogflow using a fixed intent list, our system forms VERB-NOUN intents that it does **not limit iteself by industry domains**
- [Name Entity Recognizer](https://github.com/quocdat32461997/NER) Implemented **BiLSTM-CRF** for **Name Entity Recognition**, built the data pipeline in *Tensorflow/Serving*, and deploy in *Flask*
- [NLP-course final project: Borot](https://github.com/quocdat32461997/borot)
    -	Built **Chatbot Question & Answering** with *Flask, Scikit-learn, Tensorflow, and SQL*.
    - Implemented **Information Retrieval** with **Intent Classifier (SVM), Name-Entity-Recognizer (BiLSTM-CRF) and TF-IDF** to retrieve answers in response to questions. Implemented OOP to collect users’ QA queries for personalization.
  
## Research
- Neural Entrainment to Speech Envelope in response to Perceived Sound Quality
  - Authors: **Dat Quoc Ngo**, Garret Oliver, Gleb Tcheslavski, Chin-Tuan Tan. 
  - Affiliation: Undergraduate Research Assistant at Auditory Perception Engineering Laboratory, UT Dallas
  - Abstract: The extent, to which people listen to and perceive the speech content at different noise levels varies from individual to individual. In past research projects, the speech intelligibility was determined by rating assessment, which suffered from variation of subjects' physical features. The purpose of this study is to investigate electroencephalography (EEG) by implementing multi-variate Temporal Response Function (mTRF) to examine neural responses to speech stimuli at different sound and noise levels. The result of this study shows that the front-central area of the brain clearly shows the envelope entrainment to speech stimuli.
  - Status: [Accepted to IEEE Neural Engineering Conference 2019](https://ieeexplore.ieee.org/abstract/document/8717078/)
- Linear and Nonlinear Reconstruction of Speech Envelope from EEG - @APEL, UT Dallas
  - Authors: **Dat Quoc Ngo**, Garret Oliver, Gleb Tcheslavski, Fei Chen, Chin-Tuan Tan. 
  - Affiliation: Undergraduate Research Assistant at Auditory Perception Engineering Laboratory, UT Dallas
  - Abstract: Electroencephalography (EEG) is a non-invasive method of measuring cortical activities in association to speech communication. Recent studies have shown that EEG at multiple channels across head scalps were colinearly entrained to speech envelope. They were able to reconstruct speech envelope from EEG across scalp by using ridge regression. However, the predicted speech envelopes reconstructed by this linear model approach did not yield a high correlation when compared with the original speech envelopes. The outcome of those studies inspired us to explore a non-linear alternative with Deep Learning in reconstructing speech envelope from EEG. We proposed and developed an Encoder-Decoder model based on Convolutional (CONV) and Long-Short-Term-Memory (LSTM) layers to non-linearly reconstruct speech envelope from EEG. Our finding showed that correlation between the original speech envelope and the predicted speech envelope reconstructed with our model yielded a much higher value than the equivalence reconstructed with a linear model and a single-layer LSTM model. Our Encoder-Decoder model outperformed the regularized linear regression and the single-layer LSTM model with 134% and 21% improvement in correlation.
  - Status: [Preprint](https://quocdat32461997.github.io/assets/linear_and_nonlinear_reconstruction_of_speech_envelope_from_eeg.pdf)
- Exploiting Context for Robust to Label Noise in Depression Diagnosis of Self-reported Statements - @deepkapha.ai
  - Authors: **Dat Quoc Ngo**, Aninda Bhattacharjee, Jie Mei, Tannistha Maiti
  - Affiliation: Visiting AI Researcher at deepkapha.ai
   - Status: [in submission]
