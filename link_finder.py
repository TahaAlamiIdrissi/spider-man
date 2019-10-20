from html.parser import HTMLParser
from urllib import parse

""" Parsing an html file and gather all the links using html parser """

# create a class linkfinder and inherit from HTMLParser


class LinkFinder(HTMLParser):
    def __init__(self):
        super().__init__()

    # method coming from HTMLParser (in the contract of inheritance :/)
    def error(self, message):
        pass
    
    #handling starting tags(HTMLParser)
    def handle_starttag(self,tag, attrs):
        if tag == 'a':
            for (attribute,value) in attrs:
                if attribute == 'href':
                    