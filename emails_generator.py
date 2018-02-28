import random
import json
random_words = json.load(open('words.json'))
random_domains = json.load(open('domains.json'))
n = int(input('Enter number of emails to generate'))
name_of_file = input('Enter the name of file you want to save your emails to')
f = open(name_of_file,'w')
for i in range(n):
    f.write(random_words[random.randint(0,len(random_words) - 1)] + '@' + random_domains[random.randint(0,len(random_domains) - 1)] + '\n')
f.close()
