import requests
from lxml import html

word = input("What is the word you want to search?")

definitionURL = ("https://www.dictionary.com/browse/" + word)

page = requests.get(definitionURL)
tree = html.fromstring(page.content)

definition = tree.xpath('/html/body/div/div/div/div[2]/div/main/section/section/div[1]/section[2]/div/div[1]/span/text()')

definitionString = ''.join(definition)

print()
print("Definition:")
print(definitionString)