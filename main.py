import json
import requests
from bs4 import BeautifulSoup


class Beer:
    def __init__(self, name):
        self.name = name
        self.og_min = None
        self.og_max = None
        self.fg_min = None
        self.fg_max = None
        self.ibu_min = None
        self.ibu_max = None
        self.srm_min = None
        self.srm_max = None
        self.abv_min = None
        self.abv_max = None
        self.sections = []
        self.fetch()

    def fetch(self):
        contents = fetch_beer(self.name)
        parse_beer(self, contents)


def parse_beer(beer, contents):
    header = contents.split('}}')[0].replace('{{', '').replace('%', '').replace('–', '-')

    try:
        for param in header.split('|')[1:]:
            param_name = param.split('=')[0].strip()
            param_range = param.split('=')[1]
            param_min_value = float(param_range.split('-')[0].strip())
            param_max_value = float(param_range.split('-')[1].strip())

            if param_name == 'OG':
                beer.og_min = param_min_value
                beer.og_max = param_max_value
            if param_name == 'FG':
                beer.fg_min = param_min_value
                beer.fg_max = param_max_value
            if param_name == 'IBU':
                beer.ibu_min = param_min_value
                beer.ibu_max = param_max_value
            if param_name == 'SRM':
                beer.srm_min = param_min_value
                beer.srm_max = param_max_value
            if param_name == 'ABV':
                beer.abv_min = param_min_value
                beer.abv_max = param_max_value
    except:
        pass

    sections = []
    for section in contents.split('\n\n'):
        section = section.strip()
        if len(section) < 1:
            continue
        label = section.splitlines()[0].replace('=', '')
        data = '\n'.join(section.splitlines()[1:])
        if len(data) > 0 and label[0] != "{":
            sections.append({
                'label': label.strip(),
                'value': data.replace('[[Kategoria:BJCP]]', '').strip()
            })
    beer.sections = sections


def fetch_beer(url):
    url = url.replace('https://wiki.piwo.org/', '')
    page = requests.get(f'https://wiki.piwo.org/index.php?title={url}&action=edit')
    soup = BeautifulSoup(page.content.decode('utf-8'), 'html.parser')
    textarea = soup.find('textarea')
    return textarea.contents[0]


beers = [
    Beer('Lite American Lager'),
    Beer('Standard American Lager'),
    Beer('Premium American Lager'),
    Beer('Munich Helles'),
    Beer('Dortmunder Export'),
    Beer('German Pilsner (Pils)'),
    Beer('Bohemian Pilsener'),
    Beer('Classic American Pilsner'),
    Beer('Vienna Lager'),
    Beer('Oktoberfest'),
    Beer('Dark American Lager'),
    Beer('Munich Dunkel'),
    Beer('Schwarzbier'),
    Beer('Maibock/Helles Bock'),
    Beer('Traditional Bock'),
    Beer('Doppelbock'),
    Beer('Eisbock'),
    Beer('Cream Ale'),
    Beer('Blonde Ale'),
    Beer('Kölsch'),
    Beer('American Wheat or Rye Beer'),
    Beer('North German Altbier'),
    Beer('California Common Beer'),
    Beer('Düsseldorf Altbier'),
    Beer('Standard/Ordinary Bitter'),
    Beer('Special/Best/Premium Bitter'),
    Beer('Extra Special/Strong Bitter (English Pale Ale)'),
    Beer('Scottish Light 60/-'),
    Beer('Scottish Heavy 70/-'),
    Beer('Scottish Export 80/-'),
    Beer('Irish Red Ale'),
    Beer('Strong Scotch Ale'),
    Beer('American Pale Ale'),
    Beer('American Amber Ale'),
    Beer('American Brown Ale'),
    Beer('Mild'),
    Beer('Southern English Brown'),
    Beer('Northern English Brown'),
    Beer('Brown Porter'),
    Beer('Robust Porter'),
    Beer('Baltic Porter'),
    Beer('Dry Stout'),
    Beer('Sweet Stout'),
    Beer('Oatmeal Stout'),
    Beer('Foreign Extra Stout'),
    Beer('American Stout'),
    Beer('Russian Imperial Stout'),
    Beer('English IPA'),
    Beer('American IPA'),
    Beer('Imperial IPA'),
    Beer('Weizen/Weissbier'),
    Beer('Dunkelweizen'),
    Beer('Weizenbock'),
    Beer('Roggenbier (German Rye Beer)'),
    Beer('Witbier'),
    Beer('Belgian Pale Ale'),
    Beer('Saison'),
    Beer('Biere de Garde'),
    Beer('Belgian Specialty Ale'),
    Beer('Berliner Weisse'),
    Beer('Flanders Red Ale'),
    Beer('Flanders Brown Ale/Oud Bruin'),
    Beer('Straight (Unblended) Lambic'),
    Beer('Gueuze'),
    Beer('Fruit Lambic'),
    Beer('Belgian Blond Ale'),
    Beer('Belgian Dubbel'),
    Beer('Belgian Tripel'),
    Beer('Belgian Golden Strong Ale'),
    Beer('Belgian Dark Strong Ale'),
    Beer('Old Ale'),
    Beer('English Barleywine'),
    Beer('American Barleywine'),
    Beer('Spice, Herb, or Vegetable Beer'),
    Beer('Christmas/Winter Specialty Spiced Beer'),
    Beer('Classic Rauchbier'),
    Beer('Other Smoked Beer'),
    Beer('Wood-Aged Beer'),
]

json.dump(beers, open('beers.json', 'w', encoding='utf-8'), default=vars, ensure_ascii=False)
