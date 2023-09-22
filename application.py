import requests
import re
import json
from bs4 import BeautifulSoup
url = "https://pubmed.ncbi.nlm.nih.gov/36381921/"
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")  # Parsing the data from the url
    splited = url.split('/')
    pmid = splited[-2]   #split pmid from the url
    title = soup.title.string  #extract title from the url page
    abstract = soup.find("div", id="abstract").text.strip()
    cleaned_text = abstract.replace('\n', '').replace('\r', '')
    abstract = re.sub(' {3,}', ' ', cleaned_text) # cleaned text if abstract which is extracrted from the page 
    class_name = 'docsum-title'
    a_tags = soup.find_all("a",class_=class_name)
    for a_tag in a_tags:
        href = a_tag.get("href")
        full_text_url = "https://pubmed.ncbi.nlm.nih.gov"+ href  # get full text urls 
    find_keywords = abstract.find("Keywords:")
    if find_keywords != -1:
        keywords = abstract[find_keywords:]   #get keyword from the abstract variable becaues of i have extrated everything rlalated to abstract
else:
    print("Failed:", response.status_code)

api_url = "http://127.0.0.1:8000/pageapi/"

def get_data(id = None):
    data = {}
    headers  = {'content-Type ':'application/json'}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    r = requests.get(url = api_url,headers=headers,data=json_data)
    d = r.json()
    print(d)
get_data()

def post_data():
    data = {
        "title": f"{title}",
        "pmid": pmid,
        "abstract": f"{abstract}",
        "full_text_link": f"{full_text_url}",
        "keywords": f"{abstract}"
    }
    headers = {'Content-Type': 'application/json'}
    json_data = json.dumps(data)
    r = requests.post(url=api_url, headers=headers, data=json_data)
    data = r.json()
    print(data)
# post_data()
