import sys
import json
import http
import urllib.request
import urllib.error
import urllib.parse


def get_topics(json):
    tmp = []
    for res in json['RelatedTopics']:
            if 'Topics' in res:
                for i in res['Topics']:
                    tmp.append(Topic(i))
            else:
                tmp.append(Topic(res))
    return tmp



def output(i):
    print("{}\n{}".format(i.first_url, i.text))
    print("-" * 50)
    
    
def search(query, useragent = "DuckDuckGo PythonV3 Api", skip_disambig = True, pretty = True, **kwargs):
   
    parameters = {'q': query, 'format': 'json', 'pretty' : pretty, 
                   'no_redirect': 1, 'no_html': 1,
                   'skip_disambig': skip_disambig}
                   
    encoded_parameters = urllib.parse.urlencode(parameters) 
    url = 'http://api.duckduckgo.com/?' + encoded_parameters
    print("URS is {}".format(url))
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
        
        
        
class Result:
    def __init__(self, json):
        self.abstract = Abstract(json)
        self.definition = Definition(json)
        self.answer = Answer(json)
        self.related_topics = get_topics(json)
        self.results = [Topic(res) for res in json['Results']]
        self.type = {'A': 'Article', 'D': 'Disambiguation', 'C': 'Category', 'N': 'Name', 'E': 'Exclusive'}.get(json['Type'], 'Nothing')
        self.redirect = json['Redirect']
               
    def display(self):
        for i in self.related_topics[:5]:
            output(i)
            
        for i in self.results[:5]:
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
            res.display()
    else:
        print("Usage:   {} 'search term in quotes'...".format(sys.argv[0]))
        print("Example: {} 'Hellow world' 'wikipedia' 'India'".format(sys.argv[0]))
        print("Example: {} 'Latest NBA Rankings'".format(sys.argv[0]))
        
        

        
 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
