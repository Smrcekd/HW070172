import re
import yaml

"""
1. load bibtex file
    - bibliography should be curated in Zotero (one can program cleaning procedures into the script, but this is not as reliable);
    - loading bibtex data, keep only those records that have PDFs;
    - some processing might be necessary (like picking one file out of two and more)
2. convert into other formats
    - csv
    - json
    - yml
"""

###########################################################
# VARIABLES ###############################################
###########################################################

settingsFile = "z_config.yml"
#load the settings
settings = yaml.safe_load(open(settingsFile))
#open the loaded yaml file
bibKeys = yaml.safe_load(open("zotero_biblatex_keys.yml"))
#load the keys and open them"
###########################################################
# FUNCTIONS ###############################################
###########################################################

# load bibTex Data into a dictionary
def bibLoad(bibTexFile):
    #define bibLoad
    bibDic = {}
    #create an empty dictionary
    with open(bibTexFile, "r", encoding="utf8") as f1:
        #opens a data file in a write only mode under given encoding as f1:
        records = f1.read().split("\n@")
        #read the content of f1 and splits it at the end of the line and @
        for record in records[1:]:
            #  #creates a loop for each record in records from 1 to last element.
            if ".pdf" in record.lower():
                #If there is ".pdf" in all lower case characters
                record = record.strip().split("\n")[:-1]
                #Removes both leading and the trailing characters from record and  #Splits the each record from first to last at the end of the line
                rType = record[0].split("{")[0].strip()
                rCite = record[0].split("{")[1].strip().replace(",", "")
                #splits the first records of both at {, strips at first letter and in the second case at second letter, replaces it with , and " "
                bibDic[rCite] = {}
                bibDic[rCite]["rCite"] = rCite
                bibDic[rCite]["rType"] = rType
                #opens and empty dictionary for [rCite], writes in rCite and rType
                for r in record[1:]:
                    #creates a loop for each record in records from 1 to last element.
                    key = r.split("=")[0].strip()
                    val = r.split("=")[1].strip()
                     #Sets a value of the key, and val to r, splits it at "=" and strips it at first and second letter
                    val = re.sub("^\{|\},?", "", val)
                    #returns an obtained string and uses regular expression to clear it
                    fixedKey = bibKeys[key]
                    #sets a fixedKey value
                    bibDic[rCite][fixedKey] = val
                    

    print("="*80)
    #prints "=" eighty times
    print("NUMBER OF RECORDS IN BIBLIGORAPHY: %d" % len(bibDic))
    #prints the number of all records in dictionary
    print("="*80)
    return(bibDic)
#returns bibDictionary
# CONVERSION FUNCTIONS

import json
def convertToJSON(bibTexFile):
    #defines converting function
    data = bibLoad(bibTexFile)
    #uploads data
    with open(bibTexFile.replace(".bib", ".json"), 'w', encoding='utf8') as f9:
        #opens a data file in a write only mode under given encoding into file F9
        json.dump(data, f9, sort_keys=True, indent=4, ensure_ascii=False)
        #The script file created is used to store and transfer the data

import yaml
def convertToYAML(bibTexFile):
    #defines yaml conv. function
    data = bibLoad(bibTexFile)
    #uploads the data
    with open(bibTexFile.replace(".bib", ".yaml"), 'w', encoding='utf8') as f9:
        #opens a data file in a write only mode under given encoding into file F9
        yaml.dump(data, f9)
        #The script file created is used to store and transfer the data
# CSV is the trickest because bibTeX is not symmetrical
def convertToCSV(bibTexFile):
    #defines function
    data = bibLoad(bibTexFile)
    #uploads data
    # let's handpick fields that we want to save: citeKey, type, author, title, date
    headerList = ['citeKey', 'type', 'author', 'title', 'date'] 
    #creates the header list
    header = "\t".join(headerList)
    #joins the the header list into string at tab

    dataNew = [header]
    #creates new key "header"
    for k,v in data.items():
        #creates a loop for k v in data returning the list with all dictionary keys with 
        citeKey = k
        #creates the cite key K
        if 'rType' in v:
            rType = v['rType']
        else:
            rType = "NA"

        if 'author' in v:
            author = v['author']
        else:
            author = "NA"

        if 'title' in v:
            title = v['title']
        else:
            title = "NA"

        if 'date' in v:
            date = v['date']
        else:
            date = "NA"
            #Conditioning
        tempVal = "\t".join([citeKey, rType, author, title, date])
        #at tab joing the strings of the keys
        dataNew.append(tempVal)
        #appends the tempValue to new data

    finalData = "\n".join(dataNew)
    #joins strings at new lines
    with open(bibTexFile.replace(".bib", ".csv"), 'w', encoding='utf8') as f9:
        f9.write(finalData)
        #Replaces

###########################################################
# RUN EVERYTHING ##########################################
###########################################################

print(settings["bib_all"])

convertToJSON(settings["bib_all"])
convertToYAML(settings["bib_all"])
convertToCSV(settings["bib_all"])
#prints and converts

print("Done!")