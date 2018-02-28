import random
import json
random_words = json.load(open('words.json'))
random_domains = json.load(open('domains.json'))
#generate 5 000 emails
f = open('email_list_5000','w')
for i in range(5000):
    f.write(random_words[random.randint(0,len(random_words) - 1)] + '@' + random_domains[random.randint(0,len(random_domains) - 1)] + '\n')
f.close()
#generate 100 000 emails
f = open('email_list_100000','w')
for i in range(100000):
    f.write(random_words[random.randint(0,len(random_words) - 1)] + '@' + random_domains[random.randint(0,len(random_domains) - 1)] + '\n')
f.close()