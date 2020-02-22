import requests, webbrowser
from bs4 import BeautifulSoup

# dictionary containing the subject codes and their corresponding names
subject_dict = {'7707': 'Accounting (7707)', '5038': 'Agriculture (5038)', '3180': 'Arabic (3180)', '6010': 'Art (6010)', '6090': 'Art and Design (6090)', '7094': 'Bangladesh Studies (7094)', '3204': 'Bengali (3204)', '5090': 'Biology (5090)', '7115': 'Business Studies (7115)', '7048': 'CDT Design and Communication (7048)', '5070': 'Chemistry (5070)', '7100': 'Commerce (7100)', '7101': 'Commercial Studies (7101)', ' 221': 'Computer Science - 2210', '7010': 'Computer Studies (7010)', '6043': 'Design and Technology(6043)', '2281': 'Economics (2281)', '1123': 'English Language (1123)', '5014': 'Environmental Management (5014)', ' 605': 'Fashion and Fabrics - 6050', ' 613': 'Fashion and Textiles - 6130', '6065': 'Food and Nutrition (6065)', '3015': 'French (3015)', '2217': 'Geography (2217)', '3025': 'German (3025)', 'one ': 'Global Perspectives 2069 Only for Zone 4', '3195': 'Hindi (3195)', '2055': 'Hinduism (2055)', ' 213': 'History (Modern World Affairs) - 2134', ' 214': 'History 2147', '2158': 'History World Affairs, 1917-1991 (2158)', '5096': 'Human and Social Biology (5096)', '-206': 'Islamic-Studies-2068', '2056': 'Islamic Religion and Culture (2056)', '2058': 'Islamiyat (2058)', '2010': 'Literature in English (2010)', ' 518': 'Marine Science- 5180', '4037': 'Mathematics - Additional (4037)', '4024': 'Mathematics D (Calculator Version) (4024)', '3202': 'Nepali (3202)', '2059': 'Pakistan Studies (2059)', '5054': 'Physics (5054)', '7110': 'Principles of Accounts (7110)', '2048': 'Religious Studies (2048)', '5129': 'Science - Combined (5129)', '3158': 'Setswana (3158)', '3205': 'Sinhala (3205)', '2251': 'Sociology (2251)', '3035': 'Spanish (3035)', '4040': 'Statistics (4040)', '3162': 'Swahili (3162)', '3206': 'Tamil (3206)', '7096': 'Travel and Tourism (7096)', '3247': 'Urdu - First Language (3247)', '3248': 'Urdu - Second Language (3248)'}

# user enters their desired subject code
subject_code = input('enter your subject code > ')

# looks for coresponding name in dictionary
subject_name = subject_dict.get(subject_code, '')       

# creates the link using gceguide website
main_link = 'https://papers.gceguide.com/O%20Levels/' + subject_name

# getting html data
main_html = requests.get(main_link).text

# feeding html into bs4
main_soup = BeautifulSoup(main_html, 'lxml')
        
        
# creating list by finding the appropriate link from html
paper_list=[main_link+'/'+i["href"] for i in main_soup.find_all('a', class_='name')]


for i in paper_list:
    print(i)
    
    inp = input()
    
    if inp != '':
        webbrowser.open(i)
