import requests
from bs4 import BeautifulSoup
import operator
from collections import Counter

def start(url):
    
    textlist = []
    source = requests.get(url).text

    soup = BeautifulSoup(source, 'lxml')
    every_texts = soup.find_all('div', class_='single-page')
    for every_text in every_texts:
        content = every_text.text

        texts = content.lower().split()

        for every_text in texts:
            textlist.append(every_text)
        new_textlist(textlist)

# Function to remove unwanted symbols
def new_textlist(textlist):
    
    new_list = []
    for text in textlist:
        symbols = "!@#$%^&*()_-+={[}]|\;:\"<>?/., "

        for i in range(len(symbols)):
            text = text.replace(symbols[i], '')

        if len(text) > 0:
            new_list.append(text)

    create_dictionary(new_list)

# Function creates dict containing each text's
# counts top 20 occuring texts
def create_dictionary(new_list):
    text_count = {}

    for text in new_list:
        if text in text_count:
            text_count[text] += 1
        else:
            text_count[text] = 1

    c = Counter(text_count)

    # return the most occuring texts
    top = c.most_common(20)
    print(top)

# Driver code
if __name__ == '__main__':
    url = "https://www.geeksforgeeks.org/programming-language-choose/"
    # starts crawling and prints output
    start(url)