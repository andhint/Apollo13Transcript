import pandas as pd

# Read in data. Will create a dataframe with a row for each line in text file
data = pd.read_table('apollo13transcript.txt', header = None)
# Trim extra information at top of document
data = data.iloc[138:]

# split up even and odd rows to seperate message from text and time/speaker information
timeSpeaker = data.iloc[::2]
text = data.iloc[1::2]

# split time/speaker information and put into seperate columns of a dataframe
timeSpeaker = timeSpeaker[0].apply(lambda x: pd.Series(x.split(' ')))

# create variable to be concatenated to final dataframe, reset index so indexs are the same
time = timeSpeaker[0].reset_index(drop=True)
speaker = timeSpeaker[1].reset_index(drop=True)
text = text[0].reset_index(drop=True)

# concatenate the three series into one dataframe, rename columns
cleanedData = pd.concat([time, speaker, text], axis = 1)
cleanedData.columns = ['time', 'speaker', 'text']

# write new tsv file
cleanedData.to_csv('cleanedData.txt', sep = '\t', index = False)
