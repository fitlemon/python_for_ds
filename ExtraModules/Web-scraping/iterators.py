from bs4 import Tag

from getters import get_page
from consts import URL


def iter_navigation_table(navigation_table: Tag):
    tds = navigation_table.find_all('td')
    td_activ_index = [index for index, td in enumerate(tds) if td.get('class') == ['aktiv']][0]

    for td in tds[(td_activ_index + 1):]:
        a = td.a

        # get district
        district = a.text

        # get page
        href = a.get('href')
        url = f'{URL}/{href[(href.find("R") + 2):]}'
        page = get_page(url)

        yield district, page
