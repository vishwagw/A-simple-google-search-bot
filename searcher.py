import requests
import string
from lxml import html
from googlesearch import search
from bs4 import BeautifulSoup

#creating the function to perform the searh engine result. 
#this is the main python code in the back end program for the search bot.
#example- print(cbot_query('what is an AI'))

def cbot_query(query, index=0):
    fallback = 'Sorry, I can not think of a reply for this request.'
    result = ''

    try:
        search_result_list = list(search(query, tld='co,.in', num=19, stop=3, puased =1))
        page = requests.get(search_result_list[index])
        tree = html.fromstring(page.content)
        soup = BeautifulSoup(page.content, features='lxml')
        
        article_text = ''
        arcticle = soup.findAll('p')
        for element in arcticle:
            article_text += '\n' + ''.join(element.findALL(text=True))
        article_text = article_text.replace('\n', '')
        first_sentence =article_text.split('.')
        first_sentence = first_sentence[0].split('?')[0]

        chars_without_whitespace = first_sentence.translate(
            { ord(c): None for c in string.whitespace}
        )

        if len(chars_without_whitespace) > 0:
            result = first_sentence
        else: 
            result = fallback
        
        return result
    except:
        if len(result) == 0: result = fallback
        
        return result 
    
