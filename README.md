# Amazon Review Sentiment Analysis using RoBERTa.

### Goal

The task of this project is to determine a review sentiment using Big Data. 

### Dataset
 
A few million Amazon reviews in fastText format are taken from Kaggle:  https://www.kaggle.com/bittlingmayer/amazonreviews.

Description from Kaggle:
> In this case, the classes are __label__1 and __label__2, and there is only one class per row.
__label__1 corresponds to 1- and 2-star reviews, and __label__2 corresponds to 4- and 5-star reviews.
(3-star reviews i.e. reviews with neutral sentiment were not included in the original),
Most of the reviews are in English, but there are a few in other languages, like Spanish.


### Model

The pre-trained **RobertaForSequenceClassification ("roberta-base")** ​network is used as a model. The model was trained for 2 epochs on 1 million reviews. It is impossible to include a larger number of reviews, due to the limited capabilities of GPU. The result model was trained more than six hours and saved in file **model_bert.pth**. Loss function in RoBERTa is Cross-Entropy. 

##### Please note that this file weighs more than 400 MB - it is larger than the allowed size on github, so to check the model, you need to download it from the link: https://drive.google.com/file/d/1e88lx2AMlgiXJjyt2IJex0-6QPAysfE_/view?usp=sharing

**Accuracy** is used as a metric (classes are balanced).

The training results are located in the file Jupyter Notebook **Final_project.ipynb**, **accuracy** is 0.97.
If you want to test the training of the model, you need to download the data set from kaggle.

### Technologies

* Flask server: RestAPI to get a review sentiment. Due to work with Big Data and that the model is taken from a result file the communication is built synchronously.
* Docker / Docker-Compose: to build and start a flask server

### Instructions for application:

* clone the repository: https://github.com/KseniyaLem/final_project_lsml2.git
* download the pre-trained model file: https://drive.google.com/file/d/1e88lx2AMlgiXJjyt2IJex0-6QPAysfE_/view?usp=sharing`
* to start the server use docker-compose 
```
 docker-compose up
```
or run commands manually 
```
 docker build . -t deploy_flask
 docker run -p 5000:5000 -t -i deploy_flask:latest
```
* open a page in a web browser ***http://127.0.0.1:5000/***
* input and submit any review in English into the text area
```
Examples:
    I love this project.
    It could work faster.
```
* get the result in the form "Positive review" or "Negative review"
