import requests
import json
if __name__=='__main__':
    url = 'https://pokeapi.co/api/v2/pokemon?limit=8&offset='
    response = requests.get(url)


    if response.status_code == 200:
        response_json= response.json()
        results= response_json['results']
        print(results[2])

        response_json= json.loads(response.text)
        names= response_json['results']
        names[2]
        print(names)
    
 
    
