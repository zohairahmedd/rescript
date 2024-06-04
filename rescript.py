import pandas as pd
import re

df = pd.read_csv('EBR_Videos_Listed.csv') # dataframe

categories = { # maps category names to a list of specific keywords
    'Unusable': ['Unusable', 'really', 'bad', 'positioning', 'blurry', 'too', 'hidden', 'Too'],
    'Can Be Used': ['minute', 'last', 'first', 'half', 'little', 'dark', 'harder', 'maybe', 'might', 'usable', 'few', 'some', 'frames'],
    'Perfect Video': ['Clear', 'visible'],
} # notice how its in order of unusable to perfect, this is mandatory

pattern = r'[a-zA-Z]+' # matches sequences of entire alphabet
totalCounter = 0
unusableCounter = 0
potentialCounter = 0
perfectCounter = 0

for index, row in df.iterrows(): # iterates over each row in dataframe or excel sheet

    value = row['Name (.mp4)'] # extracts video name
    annotation = row['Brief Description'] # extracts annotations
    
    if re.search(pattern, value): # if text is found in a row within video name, continue
        totalCounter += 1
        for category, keywords in categories.items(): # iterate through CATEGORIES, keywords temporarily holds the list of keywords associated with the current category
            if any(keyword.lower() in annotation.lower() for keyword in keywords): # compares lowercased keyword to lowercased version of annotated text, loops for all keywords in category
                print(f"Categorizing '{value}' under '{category}'") # prints only if a match is found
                if category == 'Unusable':
                    unusableCounter += 1
                if category == 'Can Be Used':
                    potentialCounter += 1
                if category == 'Perfect Video':
                    perfectCounter += 1
                break # break so that each video is only categorized once

print(f"Total Rows: {totalCounter}")
print(f"Unusable Videos: {unusableCounter}")
print(f"Potential Videos: {potentialCounter}")
print(f"Perfect Videos: {perfectCounter}")
