import requests
from bs4 import BeautifulSoup as bs

github_user = input("Input github username: ")
url = 'https://github.com/'+ github_user
r = requests.get(url)
soup = bs(r.content, 'html.parser')
profile_picture = soup.find('img', {'class' : 'avatar'}) ['src']
print(profile_picture)