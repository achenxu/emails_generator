import random
import json
f = open('email_list','w')
random_words = json.load(open('words.json'))
random_domains = json.load(open('domains.json'))
for i in range(5000):
    f.write(random_words[random.randint(0,len(random_words) - 1)] + '@' + random_domains[random.randint(0,len(random_domains) - 1)] + '\n')
f.close()