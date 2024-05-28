import pandas as pd
import re

df = pd.read_excel('EBR_Videos_Excel.xlsx') # dataframe

categories = { # maps category names to a list of specific keywords
    'Unusable': ['Unusable', "can't", 'really', 'bad', 'positioning', 'blurry', 'too', 'hidden', 'Too'],
    'Can Be Used': ['minute', 'first', 'half' ],
    'Might Work': ['little', 'dark', 'harder', 'maybe', 'might'],
    'Perfect Video': ['Clear', 'visible'],
} # notice how its in order of unusable to perfect, this is mandatory

pattern = r'[a-zA-Z]+' # matches sequences of entire alphabet

for index, row in df.iterrows(): # iterates over each row in dataframe or excel sheet

    value = row['Name (.mp4)'] # extracts video name
    annotation = row['Brief Description'] # extracts annotations
    
    if re.search(pattern, value): # if text is found in a row within video name, continue
        for category, keywords in categories.items(): # iterate through CATEGORIES, keywords temporarily holds the list of keywords associated with the current category
            if any(keyword.lower() in annotation.lower() for keyword in keywords): # compares lowercased keyword to lowercased version of annotated text, loops for all keywords in category
                print(f"Categorizing '{value}' under '{category}'") # prints only if a match is found
                break # break so that each video is only categorized once