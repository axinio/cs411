import requests
from itertools import combinations
from med_parser import wrap_trace
from sentiment_processing import description_analyzer
from firedb import *
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

def repopulate_list(data):
    keys = list(data.keys())
    for x in keys:
        new_list.append(x)
    for i in range(len(keys)):
        if type(data[keys[i]]) == dict:
            new_keys =  data[keys[i]].keys()
            for y in new_keys:
                if y not in new_list:
                    new_list.append(y)
    return newChecker()
    


def request_process_path(user,data):
        if userFinder(user) == True:
            if "id" in data:
                print(new_list)
                i = data["id"]
                print(i)
                addMain(i)
                new_d = newChecker()
                replaceData(user,new_d)
        elif userFinder(user) == False:    
            if "id" in data:
                i = data["id"]
                print(i)
                addMain(i)
                new_d = newChecker()
                addData(user,new_d)
        return new_d

def clear_curr_list():
    new_list.clear()


#Different Version of newChecker
# def newChecker():
#     n = len(new_list)
    
#     if n < 2:
#         return None

#     result = {}
#     base_url = 'https://rxnav.nlm.nih.gov/REST/interaction/list.json?rxcuis='

#     for x, y in combinations(new_list, 2):
#         url = f"{base_url}{x}+{y}"
#         try:
#             response = requests.get(url)
#             response.raise_for_status()
#         except requests.exceptions.RequestException as e:
#             print(f"Error: {e}")
#             continue

#         wrapped_response = wrap_trace(response)

#         if x not in result:
#             result[x] = {y: wrapped_response}
#         else:
#             result[x][y] = wrapped_response

#     return result
