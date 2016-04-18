#returns a list of dictionaries{'url': ___, 'title': ___} of one site 
choices={'bbc_technology.json':'BBC Technology', 'bbc_health.json':'BBC Health','bbc_us_and_canada.json':'BBC US/Canada','bbc_world.json':'BBC World','foxbusiness_markets.json':'Fox Markets','foxbusiness_politics.json': 'Fox Politics','foxbusiness_technology.json':'Fox Technology','independent_americas.json': 'Independent Americas', 'independent_business.json': 'Independent Business', 'independent_gadgets-and-tech.json':'Independent Technology', 'independent_politics.json': 'Independent Politics', 'independent_world.json':'Independent World','theguardian_technology.json':'The Guardian Technology', 'theguardian_us-elections-2016.json':'The Guardian US Politics', 'theguardian_us-news.json':'The Guardian US news','theguardian_world.json':'The Guardian World' }	

def make_dict(sites):
    posts = []
    for site in sites:
	f = open(site)
	
	while True:
	    line = f.readline()	
	    line2 = f.readline()
	    if not line2: 
		break
	    temp = {}
	    temp['title'] = str(line[11:].split('"')[0])
	    temp['url'] = str(line2[8:].split('"')[0])
	    temp['source'] = str(choices[site])
	    
	    posts.append(temp)
	f.close()

    return posts

#test = ['independent_business.json']
#make_dict(test)

def search_word(site, word):
    word = str(word).lower() # make the word lower case
    title_list = make_dict(site)
    searched_list = [] # will hold the titles with the word that was searched for
    """for titles in title_list:
	title = titles['title'].split() #list of a ll the words in one title
	for x in title:
	    if((str(x).lower())==word): #if there is a word in the title that matches the searched word
		searched_list.append(titles)
		break # go onto next title if a word is found"""
    
    for titles in title_list:
	title = titles['title']
	temp = str(title)
	temp = temp.lower()
	if word in temp:
	    searched_list.append(titles)
    return searched_list


#search for candidates..should have really used my search for words function..
#Make candidate names upper case
def pres_candidates():
    #all_sites = ['bbc_technology.json', 'bbc_health.json','bbc_us_and_canada.json','bbc_world.json','foxbusiness_markets.json','foxbusiness_politics.json', 'foxbusiness_technology.json'] 
    bbc_sites = ['bbc_technology.json', 'bbc_health.json','bbc_us_and_canada.json','bbc_world.json']
    fox_sites = ['foxbusiness_markets.json','foxbusiness_politics.json', 'foxbusiness_technology.json']
    bbc_list = make_dict(bbc_sites)
    fox_list = make_dict(fox_sites)
    candidates = {'sanders':{'bbc':{'num_sited':0,'ref':[]},'fox':{'num_sited':0,'ref':[]}},'clinton':{'bbc':{'num_sited':0,'ref':[]},'fox':{'num_sited':0,'ref':[]}},'trump':{'bbc':{'num_sited':0,'ref':[]},'fox':{'num_sited':0,'ref':[]}},'cruz':{'bbc':{'num_sited':0,'ref':[]},'fox':{'num_sited':0,'ref':[]}}}
    #republicans = {'trump':{'bbc':0,'fox':0},'cruz':{'bbc':0,'fox':0}}
   
    #print democrats
    #print republicans

    #f = open("bbc_technology.json")
    for site in bbc_list:
	temp = site['title'].lower()
	if "sanders" in temp:
	    candidates['sanders']['bbc']['num_sited'] = candidates.get('sanders').get('bbc').get('num_sited') + 1
	    candidates['sanders']['bbc']['ref'].append(site)
	elif "bernie" in temp:
	    candidates['sanders']['bbc']['num_sited'] = candidates.get('sanders').get('bbc').get('num_sited') + 1
	    candidates['sanders']['bbc']['ref'].append(site)
	if "clinton" in temp:
	    candidates['clinton']['bbc']['num_sited'] = candidates.get('clinton').get('bbc').get('num_sited') + 1
	    candidates['clinton']['bbc']['ref'].append(site)
	elif "hillary" in temp:
	    candidates['clinton']['bbc']['num_sited'] = candidates.get('clinton').get('bbc').get('num_sited') + 1
	    candidates['clinton']['bbc']['ref'].append(site)
	if "trump" in temp:
	    candidates['trump']['bbc']['num_sited'] = candidates.get('trump').get('bbc').get('num_sited') + 1
	    candidates['trump']['bbc']['ref'].append(site)
	elif "donald" in temp:
	    candidates['trump']['bbc']['num_sited'] = candidates.get('trump').get('bbc').get('num_sited') + 1
	    candidates['trump']['bbc']['ref'].append(site)
	if "cruz" in temp:
	    candidates['cruz']['bbc']['num_sited'] = candidates.get('cruz').get('bbc').get('num_sited') + 1
	    candidates['cruz']['bbc']['ref'].append(site)
	elif "ted" in temp:
	    candidates['cruz']['bbc']['num_sited'] = candidates.get('cruz').get('bbc').get('num_sited') + 1
	    candidates['cruz']['bbc']['ref'].append(site)

    for site in fox_list:
	temp = site['title'].lower()
	if "sanders" in temp:
	    candidates['sanders']['fox']['num_sited'] = candidates.get('sanders').get('fox').get('num_sited') + 1
	    candidates['sanders']['fox']['ref'].append(site)
	elif "bernie" in temp:
	    candidates['sanders']['fox']['num_sited'] = candidates.get('sanders').get('fox').get('num_sited') + 1
	    candidates['sanders']['fox']['ref'].append(site)
	if "clinton" in temp:
	    candidates['clinton']['fox']['num_sited'] = candidates.get('clinton').get('fox').get('num_sited') + 1
	    candidates['clinton']['fox']['ref'].append(site)
	elif "hillary" in temp:
	    candidates['clinton']['fox']['num_sited'] = candidates.get('clinton').get('fox').get('num_sited') + 1
	    candidates['clinton']['fox']['ref'].append(site)
	if "trump" in temp:
	    candidates['trump']['fox']['num_sited'] = candidates.get('trump').get('fox').get('num_sited') + 1
	    candidates['trump']['fox']['ref'].append(site)
	elif "donald" in temp:
	    candidates['trump']['fox']['num_sited'] = candidates.get('trump').get('fox').get('num_sited') + 1
	    candidates['trump']['fox']['ref'].append(site)
	if "cruz" in temp:
	    candidates['cruz']['fox']['num_sited'] = candidates.get('cruz').get('fox').get('num_sited') + 1
	    candidates['cruz']['fox']['ref'].append(site)
	elif "ted" in temp:
	    candidates['cruz']['fox']['num_sited'] = candidates.get('cruz').get('fox').get('num_sited') + 1
	    candidates['cruz']['fox']['ref'].append(site)
	
     
    #print bbc_list
    #print fox_list
    return candidates

#pres_candidates()    
		
    

