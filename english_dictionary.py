import json
import time
from difflib import get_close_matches

with open('words.json','r') as f:
    data = json.load(f)

    def give_definition(keyword):
        if keyword in data.keys():
            definition = data[keyword]
        else:
            keyword = close_matches(inp)[0]
            definition = data[keyword]
        for i in definition:
            yield i
    
    def close_matches(inp):
        # source = inp.lower()
        # target = map(lambda x: x.lower(),data.keys())
        matching_word = get_close_matches(inp,data.keys(),1,0.6)
        return matching_word
            
    while(True):
        inp = input('Enter a word: ')
        print()
        try:
            for i in give_definition(inp):
                print(i)
            print()
        except:
            # print(close_matches(inp))
            if (close_matches(inp)):
                print('You might be looking for: {}'.format(close_matches(inp)[0]))
                selection = input('Is the correct? ')
                print()
                if selection.lower() == 'yes' or selection.lower() == 'y':
                    for i in give_definition(close_matches(inp)[0]):
                        print(i)
                else:
                    print('Okay. My bad!')
                print()
            else:
                print('Word not found')
        finally:
            answer = input('Do you want enter again? ')
            if answer.lower() == 'yes' or answer.lower() == 'y':
                continue
            else:
                # print('Thank you!')
                print('Exiting...')
                # time.sleep(1)
                break