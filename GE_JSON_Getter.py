import requests
import time

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


for let in letters:
    for num in range(1,50):
        payload = {'category':1, 'alpha': let, 'page':num}
        r = requests.get('http://services.runescape.com/m=itemdb_oldschool/api/catalogue/items.json?' ,params=payload)

        r_dict = r.json()
        
        if r_dict['items'] == []:
            break
        else:
            time.sleep(5)
            for item in r_dict['items']:
                name = item["name"]
                current = item["current"]["price"]

                print(name + ' ' + str(current))

                


