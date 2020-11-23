
import re
import yaml 
import os
import shutil
#from z_2_conversion_simple import bibLoad
#####Variables#####################################################################
settingsFile = "MW.yml"
settings = yaml.safe_load(open(settingsFile))
bibKeys = yaml.safe_load(open("MyLibrary.yaml"))
#####Functions#####################################################################
def bibLoad(bibTexFile):
    bibDic = {}
    with open(bibTexFile, "r", encoding="utf8") as f1:
        records = f1.read().split("\n@")
        for record in records[1:]:
            # let process ONLY those records that have PDFs
            if ".pdf" in record.lower():
                completeRecord = "\n@" + record
# adding the complete record
                record = record.strip().split("\n")[:-1]
                rType = record[0].split("{")[0].strip()
                rCite = record[0].split("{")[1].strip().replace(",", "")
                bibDic[rCite] = {}
                bibDic[rCite]["rCite"] = rCite
                bibDic[rCite]["rType"] = rType
                bibDic[rCite]["completeR"] = completeRecord
                for r in record[1:]:
                    key = r.split("=")[0].strip()
                    val = r.split("=")[1].strip()
                    val = re.sub("^\{|\},?", "", val)
                    fixedKey = bibKeys[key]
                    if fixedKey == "file":
                        if ";" in val:
                            temp = val.split(";")
                            for i in temp:
                                if i.endswith(".pdf"):
                                    val = i
                                    break
                    bibDic[rCite][fixedKey] = val
    print("="*80)
    print("NUMBER OF RECORDS IN BIBLIGORAPHY: %d" % len(bibDic))
    print("="*80)
    print(bibDic)    
    return(bibDic)# end of function
dictionary = bibLoad(settings["bib_all"]) # saving the results into a variable
def folderMaker(rCite):
    temppath= os.path.join(settings["memex_path"], rCite[0], rCite[:2], rCite)
    if not os.path.exists(temppath):
        os.makedirs(temppath)   
    print(temppath)
    return temppath    

def copySafe(metaData):
    for k, v in metaData.items():
        pubPath= folderMaker(k)   
        tempFile = open(pubPath + "\\" + k + ".bib", "w", encoding="utf8")        
        print(v["completeR"], file= tempFile)
        pdfPath = v["file"]     
        pdfPath = pdfPath.replace("\\\\", "\\")
        pdfPath = pdfPath.replace("\\:", ":")
        

        if not os.path.isfile(pubPath):
            shutil.copyfile(pdfPath, pubPath+ "\\" + k + ".pdf")
copySafe(dictionary)

