import os, yaml

###########################################################
# VARIABLES ###############################################
###########################################################

settingsFile = "ml.yml"
vars = yaml.safe_load(open(settingsFile))
#assigning the file we are using as a source and loading it to the python.

###########################################################
# FUNCTIONS ###############################################
###########################################################

# analyze bibTeX data; identify what needs to be fixed

def bibAnalyze(bibTexFile):
    #defining function of analyzing the BibTexFile
    tempDic = {}
    #creating an empty dictioanary

    with open(bibTexFile, "r", encoding="utf8") as f1:
        #opens a data file in a read only mode under given encoding into file F1
        records = f1.read()
        #reads the content of f1
        records = records.split("\n@")
        #splits the records
        for record in records[1:]:
            # let process ONLY those records that have PDFs
            #creates a loop for each record in records from 1 to last element.
            if ".pdf" in record.lower():
                #If there is ".pdf" in all lower case characters
                record = record.strip()
                #Removes both leading and the trailing characters from record
                record = record.split("\n")[:-1]
                #Splits the each record from first to last at the end of the line
                for r in record[1:]:
                    #creates a loop for every r in records from first to last
                    r = r.split("=")[0].strip()
                    #splits r on "=" symbol and every first symbol
                    if r in tempDic:
                        #creates a condition - if r in the dictionary
                        tempDic[r] += 1
                        #assigns +1
                    else:
                        tempDic[r] = 1
                        #if not, starts as 1
    results = []
    #creates an empty list called "results"
    for k,v in tempDic.items():
        #creates a loop for each k, v in dictionary returning the list with all dictionary keys with values
        result = "%010d\t%s" % (v, k)
        #the v and k are reduced through regular expressions and returns rest
        results.append(result)
        #results are appended to the end of the list
    results = sorted(results, reverse=True)
    #Sorts the results in descending order
    results = "\n".join(results)
    # results are divided by new line, joining all items in the "results" into one string
    with open("bibtex_analysis.txt", "w", encoding="utf8") as f9:
        #opens a data file in a write only mode under given encoding into file f9
        f9.write(results)
        #writes the results in the 

bibAnalyze(vars['bib_all'])
#returns the "bib_all" attribute of the given object


