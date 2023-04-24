import requests
from med_parser import wrap_trace
from sentiment_processing import description_analyzer
new_list = []

#Adds new medications to list for current user
def addMain(medNum):
    if len(new_list) == 0:
        new_list.append(medNum)
    elif medNum not in new_list:
        new_list.append(medNum)

#Processes API request to check for drug interactions
def newChecker():
    n = len(new_list)
    result = {}
    for x in range(n):
         for j in range(x,n):
              base_url = 'https://rxnav.nlm.nih.gov/REST/interaction/list.json?rxcuis='
              if len(new_list) > 1:
                if new_list[x] != new_list[j]:
                    base_url = base_url + (str(new_list[x])+'+'+str(new_list[j]))
                    get_resp = requests.get(base_url)
                    if new_list[x] not in result:
                        a = wrap_trace(get_resp)
                        result[new_list[x]] = {new_list[j]: a }
                    else: 
                        a = wrap_trace(get_resp)
                        result[new_list[x]][new_list[j]] =  a
              else:
                  return None
    return result