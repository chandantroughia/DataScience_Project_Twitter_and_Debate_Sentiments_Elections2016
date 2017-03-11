# DataScience_Project_Twitter_and_Debate_Sentiments_Elections2016
(US Presidential Elections 2016)

Team: Max Llewellyn, Yi Liu, Charlie You, Kyle Francis, Chandan Singh Troughia, Aaron Sedlacek

It was a team project and the purpose of the project was to figure out two different things:
1. Whether the sentiments of the both the presidential candidates are same or not.
2. Whether the twitter sentiments of both the presidential candidates match their sentiments in presidential debates during that time.

Data Sources: 
DataSet1: Twitter handles of Hillary Clinton and Donald Trump
DataSet2: 
a. Debate 1: http://www.presidency.ucsb.edu/ws/index.php?pid=118971
b. Debate 2: http://www.presidency.ucsb.edu/ws/index.php?pid=119038
c. Debate 3: http://www.presidency.ucsb.edu/ws/index.php?pid=119039


I collected the data for DataSet 2 in textual format, cleaned it and converted it to json format for our analysis.

Other Scripts Used:
preprocess.py: Preprocesses all data with using methods described above.
train.py: Creates features from training data and trains the classifier.
classify.py: Uses the trained models to classify the debate transcripts and
candiate tweets
visualize.py: Creates the required visualizations to demonstrate our findings.

In Case of pickled data, you can read it with the following script:
