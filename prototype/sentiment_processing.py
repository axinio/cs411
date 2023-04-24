import json
import os
from dotenv import load_dotenv
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 \
    import Features, SentimentOptions

load_dotenv() 
SECRET_KEY = os.environ.get("WATSON_API")

def description_analyzer(desc):
    if desc:
        authenticator = IAMAuthenticator(SECRET_KEY)
        natural_language_understanding = NaturalLanguageUnderstandingV1(
            version='2022-04-07',
            authenticator=authenticator
        )

        natural_language_understanding.set_service_url('https://api.us-east.natural-language-understanding.watson.cloud.ibm.com/instances/9c7df39a-d218-4da5-87ef-c974a0960c60')

        response = natural_language_understanding.analyze(
            text=desc,
            features=Features(sentiment=SentimentOptions(document= True))).get_result()
        
        print(json.dumps(response, indent=2))
    else:
        return "neutral"
    return response["sentiment"]["document"]["label"]