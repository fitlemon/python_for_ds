import requests
from bs4 import BeautifulSoup, Tag


def get_table(page: BeautifulSoup) -> Tag:
    table = page.find('table', {'class': 'sorteringsbar_tabell'})

    return table


def get_navigation_table(page: BeautifulSoup) -> Tag:
    return page.find('table', {'id': 'oversiktstabell'})


def get_level(navigation_table: Tag) -> str:
    td_activ = navigation_table.find('td', {'class': 'aktiv'})
    
    return td_activ.parent.get('class')[0]


def get_page(url: str) -> BeautifulSoup:
    # send request and get content
    response = requests.get(url)
    status_code = response.status_code
    
    if status_code == 200:
        # decode content
        content = response.content.decode()  # response.text
        
        # parse content
        soup = BeautifulSoup(content)

        print(f'Parsing page for url {url} OK')
    else:
        soup = None
        print(f'Page for url {url} NOT PARSED, status code is {status_code}')

    response.close()

    return soup
