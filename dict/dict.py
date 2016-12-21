#Develop by tuancnttbk93@gmail.com

import requests
import json
import sys

# TODO: replace with your own app_id and app_key
app_id = 'oxford-app-id'
app_key = 'oxford-app-key'

language = 'en'
word_id = sys.argv[1]

try:
    url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_id.lower()
    r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})
    resultStr = 'Key word: ' + word_id + '\n\n'

    results = r.json()['results']
    for result in results:
        lexicalEntries = result['lexicalEntries']
        lexicalEntriesStr = ''

        for lexicalEntrie in lexicalEntries:
            entries = lexicalEntrie['entries']
            lexicalCategoryStr = 'Lexical category: ' + lexicalEntrie['lexicalCategory'] + '\n'
            textStr = 'Text: ' + lexicalEntrie['text'] + '\n'

            lexicalEntrieStr = '--------------------------------------------------------\n'
            lexicalEntrieStr = lexicalEntrieStr + textStr + lexicalCategoryStr + '\n';

            for entry in entries:
                senses = entry['senses']

                for sense in senses:
                    if sense.has_key('definitions'):
                        definitions = sense['definitions']
                        definitionStr = ''
                        for definition in definitions:
                            definitionStr = '* ' + definitionStr + definition + '\n'

                        lexicalEntrieStr = lexicalEntrieStr + definitionStr

                    if sense.has_key('examples'):
                        examples = sense['examples']
                        exampleStr = 'Examples: \n'
                        for example in examples:
                            exampleStr = exampleStr + example['text'] + '\n\n'

                        lexicalEntrieStr = lexicalEntrieStr + exampleStr

            lexicalEntriesStr = lexicalEntriesStr + lexicalEntrieStr + '\n'

        resultStr = resultStr + lexicalEntriesStr


    print(resultStr)
except (KeyboardInterrupt, SystemExit):
    print('Opp! Search progressing is canceled!')
except:
    print('Opp! No results')
