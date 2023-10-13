dict1.get('key1', 'N/A')

# If the key is not in the dictionary, .get() will return 'N/A'.

for key in dict1:
    print(key, [dict1.get('subkey1', 'N/A') for item in dict1[key]])  

dict1
{'key1': [{'subkey1': 'Blue','subkey2': None}, {'subkey1': 'Gray', 'subkey2': 'Perfect'}],
 'key2': [{'subkey1': 'Red','subkey2': 'Great'}, {'subkey1': 'Green', 'subkey2': '...'}]
}
