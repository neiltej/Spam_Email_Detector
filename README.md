# Spam_Email_Detector

Spam emails such as phishing and advertisements cost businesses and individuals millions of dollars annually.

There are several techniques to automatically detect spam emails, although none of them have showed 100% predictive accuracy. One of the earliest examples of a successful spam classification model was the Naive Bayes classification model. However, nowadays, this model lags behind more sophisticated counterparts within machine learning and deep learning models, particularly those better suited for Natural Language Processing. Among all proposed models, machine learning and deep learning algorithms have achieved better accuracy.

We have used Natural Language Processing techniques including stopwords removal, stemming, and ASCII character removal to create a more robust and non-repetitive corpus to train our vocabulary on. After these preprocessing steps, the training data is used to train several different models, including: logistic regression, naive bayes, support vector classifier, artificial neural network, and a long-short-term memory model (LSTM).

The results demonstrated excellent classification results for most of the models, however, overfitting is a major issue for NLP models. Upon training of all models, overfitting analysis was conducted by using K-fold cross-validation on the machine learning models (LR, NB, SVC) and implementing early stopping and dropout layers in training for the deep learning models (ANN, LSTM). These models were tested again to determine their efficacy. It was found that LSTM performed very well, and this model was later deployed to Streamlit to create a useable web application.

The final web application can be viewed and tested here: https://neiltej-spam-email-detector-predictor-bhyv2q.streamlit.app/
The python script used for the project is: final_script_riya.ipynb
