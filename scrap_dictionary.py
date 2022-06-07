import requests
from bs4 import BeautifulSoup
import csv

from views.view import View


def extract_definition(text):
    """ Allow to skip characters before ') ' """

    for i, letter in enumerate(text):
        if letter == ')':
            return text[(i + 1):]


def parse_one_letter(letter, delimiter):

    # Scrap
    vgm_url = f'https://www.mso.anu.edu.au/~ralph/OPTED/v003/wb1913_{letter}.html'
    html_text = requests.get(vgm_url).text
    soup = BeautifulSoup(html_text, 'html.parser')

    # Extract
    words = []
    for line in soup.find_all('p'):
        word = line.find('b').text
        type = line.find('i').text
        definition = extract_definition(line.text)

        if len(word) > 1:
            # Regroup same words in one line
            if len(words) < 2 or not (words[-1][0] == word and words[-1][1] == type):
                words.append([word, type, definition])
            else:
                words[-1].append(definition)

    # Create csv file
    with open(f'./files/{letter}.csv', 'w', newline='') as f:
        writer = csv.writer(f, delimiter=delimiter)
        writer.writerows(words)


# −−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−
bodies = list()
bodies.append('https://www.mso.anu.edu.au/~ralph/OPTED/')
bodies.append("One file per letter, csv file with '_' as delimiter.")
bodies.append("One line per words with the type (multiple definitions are regrouped on the same line \n"
              "and separated by the delimiter).")
my_view = View(header='Scraping', bodies=bodies)
my_view.start_loading()

# --
letters = 'abcdefghijklmnopqrstuvwxyz'
for i, letter in enumerate(letters):
    my_view.update_loading_text(f'In progress : {letter.upper()}')
    my_view.update_loading(i * 100 / len(letters))
    parse_one_letter(letter, '_')

# --
my_view.stop_loading()
bodies.append('Done.')
my_view.show()
