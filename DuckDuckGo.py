# DuckDuckGo.py - Library written in Python3 for querying DuckDuckGo API.
# Tested wiht Python 3.5.2 
#
# Copyright (c) 2016 Abhishek Poonia <abhishekpoonia22@gmail.com>
# Github: https://github.com/knight-shade
#
# See LICENSE for terms of usage, modification and redistribution.
#
# See https://duckduckgo.com/api for more details about return fields.
#
# *CAUTION: As this library uses an instant answer API, most deep queries (non topic names) will be blank.



# The required libraries.
import sys
import json
import http
import webbrowser
import urllib.request
import urllib.error
import urllib.parse



def get_topics(json):
    '''
    Returns the list of all the topics associated with search query.
    '''
    
    tmp = []
    for res in json['RelatedTopics']:
            if 'Topics' in res:
                for i in res['Topics']:
                    tmp.append(Topic(i))
            else:
                tmp.append(Topic(res))
    return tmp




def output(i):
    '''
    A helper function to print the data
    '''
    
    print("{}\n{}".format(i.first_url, i.text))
    print("-" * 50)


    
    
def search(query, web = False, useragent = "DuckDuckGo Python3 Api", skip_disambig = True, pretty = True, **kwargs):
    '''
    Searching the DuckDuckGo search engine and returning a Result object.
    
    Keyworld Arguments:
    
    query          : Straightforward, the search string.
    web            : If true, opens the web browser and skips and command line. Default: False
    useragent      : Useragent to use while searching. Default: "DuckDuckGo Python3 Api". Can be overridden.
    skip_disambig  : Used to skip disambiguation. Default: 1 (True)
    pretty         : To make JSON look pretty. Default: 1 (True)
    **kwargs       : Any other parameters passed. As of writing this API no other parameters exists, helpful for future scaling.
    '''
    
    parameters = {'q': query, 'format': 'json', 'pretty': pretty, 'no_redirect': 1, 'no_html': 1, 'skip_disambig': skip_disambig}
                   
    encoded_parameters = urllib.parse.urlencode(parameters) 
    url = 'http://api.duckduckgo.com/?' + encoded_parameters
    
    # Performs the Web browser search instead of instant answer API.
    if web:
        url = 'http://duckduckgo.com/?ia=web&' + urllib.parse.urlencode({'q': query})
        webbrowser.open(url)
        return
        
        
    request = urllib.request.Request(url, headers = {'User-Agent': useragent})
    
    try:
        response = urllib.request.urlopen(request)
    except urllib.error.HTTPError as e:
        print("The server couldn't fulfill the request.")
        print("Error code: {}, Response: {}.".format(e.code, http.HTTPStatus(e.code)))
    except urllib.error.URLError as e:
        print("We failed to reach the server.")
        print("Reason: {}", e.reason)
        
    else:
        response = response.read().decode()
        response = json.loads(response)
        return Result(response)
        
    
        

# Below are the return fields as class objects.
class Result:
    def __init__(self, json):
        self.abstract = Abstract(json)
        self.definition = Definition(json)
        self.answer = Answer(json)
        self.related_topics = get_topics(json)
        self.results = [Topic(res) for res in json['Results']]
        self.type = {'A': 'Article', 'D': 'Disambiguation', 'C': 'Category', 'N': 'Name', 'E': 'Exclusive'}.get(json['Type'], 'Nothing')
        self.redirect = json['Redirect']
               
               
    def display(self, limit = 5):
        '''
        Any easy way to dispaly top <limit> results.
        This function is called when API is accessed via command line.
        '''    
        for i in self.related_topics[:limit]:
            output(i)
        for i in self.results[:limit]:
            output(i)
            
        
        
class Abstract:
    def __init__(self, json):
        self.abstract = json['Abstract']
        self.abstract_text = json['AbstractText']
        self.abstract_source = json['AbstractSource']
        self.abstract_url = json['AbstractURL']
        self.image = json['Image']
        self.heading = json['Heading']
        
        
        
class Definition:
    def __init__(self, json):
        self.definition = json['Definition']
        self.definition_source = json['DefinitionSource']
        self.definition_url = json['DefinitionURL']
        
     
        
class Answer:
    def __init__(self, json):
        self.answer = json['Answer']
        self.answer_type = json['AnswerType']
        
        
                
class Topic:
    def  __init__(self, json):
        
        self.result = json['Result']
        self.first_url = json['FirstURL'] 
        self.icon = Icon(json['Icon'])
        self.text = json['Text']
        
        
        
class Icon:
    def __init__(self, json):
        self.url = json['URL']
        self.height = json['Height']
        self.width = json['Width']
        
        
        
if __name__ == "__main__":
    import sys
          
    if len(sys.argv) > 1:
        for i in range(1, len(sys.argv)):
            res = search(sys.argv[i])
            res.display()                   # Displaying the results. Default: Top 5 form internal and external links.
    else:
        print("Usage:   {} [-w] 'search term in quotes'...".format(sys.argv[0]))
        print("Example: {} [-w] 'Hellow world' 'wikipedia' 'India'".format(sys.argv[0]))
        print("Example: {} [-w] 'Latest NBA Rankings'".format(sys.argv[0]))
        print("Option -w opens search in web browser. Should be included before all search terms.")
        

        
 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
