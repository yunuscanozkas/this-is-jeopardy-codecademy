import pandas as pd
pd.set_option('display.max_colwidth', -1)

#2: Loading the data
jeopardy = pd.read_csv("jeopardy.csv")
print(jeopardy.columns)
#After you figure out the problem with the column names, you may want to rename them to make your life easier the rest of the project.
jeopardy = jeopardy.rename(columns = lambda x: x.strip())
print(jeopardy.columns)

#3 & 4: Write a function that filters the dataset for questions that contains all of the words in a list of words.Edit your function so it is more robust. For example, think about capitalization
def filter(data,words):
  filter = lambda x:all(word.lower() in x.lower() for word in words)
  return data.loc[data["Question"].apply(filter)]
#Testing the function
filtered = filter(jeopardy, ["King", "England"])
print(filtered["Question"])

#5: Convert the " Value" column to floats. If you’d like to, you can create a new column with the float values 
jeopardy["Float Value"] = jeopardy["Value"].apply(lambda x: float(x[1:].replace(',','')) if x != "None" else 0)
#... For example, what is the average value of questions that contain the word "King"?
filtered_king = filter(jeopardy, ["King"])
print(filtered_king["Float Value"].mean())

#6:Write a function that returns the count of the unique answers to all of the questions in a dataset. 
def get_answer_counts(data):
    return data["Answer"].value_counts()

print(get_answer_counts(filtered))
