from Bio import Entrez
import regex
id_list = []
max_searches = 0
number_of_emails_wanted =50

keywords = []
count = 0
while count == 0:
    add_term = input("add search term? y/n ")
    if add_term == 'y':
        term = input("Insenrt search term: ")
        keywords.append(term)
    else:
        count = 1

search_term = ''
for a in keywords:
    search_term += str(a)+ '[abstract] AND '
print(search_term)

def search(query):
    Entrez.email = 'mlooke@mit.edu'
    handle = Entrez.esearch(db='pubmed',
                            sort='relevance',#can also be 'date'
                            retmax=str(max_searches),
                            retmode='xml',
                            term=query)
    results = Entrez.read(handle)
    id_list = results['IdList']
    return id_list

new_matches = []
def article_info(pmid):
    global new_matches
    Entrez.email = 'mlooke@mit.edu'
    handle = Entrez.efetch(db='pubmed', id=pmid, retmode='text', rettype='medline')
    paper_info = handle.read()

    matches = regex.findall("\S*@\S*",paper_info )
#    del paper_info
    raw_matches = []
    for a in matches:#this loop removes periods from ends of emails
        if a.endswith('.'):
            raw_matches.append(a[:-1])
        else:
            raw_matches.append(a)
    del matches
    for a in raw_matches: #this loop removes repeated emails
        if a in new_matches:
            continue
        else:
            new_matches.append(a)
    del raw_matches
    #print handle.read()
    #print matches


#make this to a function
for a in range(number_of_emails_wanted,number_of_emails_wanted*4,number_of_emails_wanted*1):
    max_searches= a
    if len(new_matches)<number_of_emails_wanted:
        article_info(search(search_term))
    else:
        break
print('found matches: ', len(new_matches))
print(sorted(new_matches))
