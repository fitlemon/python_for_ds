from collections import defaultdict
from bs4 import BeautifulSoup, Tag


def parse_table(table: Tag) -> dict:
    info = defaultdict(list)

    for tr in table.find_all('tr'):
        if tr.find('th') is not None:
            cells = [th.text for th in tr.find_all('th')]
            keys = [*cells[:3], cells[6]]
        else:
            cells = [td.text for td in tr.find_all('td')]
            values = [*cells[:3], cells[6]]

            for key, value in zip(keys, values):
                info[key].append(value) 

    return info
