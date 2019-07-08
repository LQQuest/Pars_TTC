import csv
import requests
from bs4 import BeautifulSoup
import re
import set
import price_list
import constant
from random import choice


def clear(string):
    string = re.sub(r'\s+', ' ', string)
    string = re.sub(r'\r\n', '', string)
    return string


def get_html(url, proxy=None, useradent=None):
    print("get_html")
    response = requests.get(url, headers=useradent, proxies=proxy)
    return response.text


def get_page_count(html):
    soup = BeautifulSoup(html)
    pagination = soup.find('ul', class_='pagination').find_all('li')[-1].a.get('href')
    return pagination


def local_discard(loc):
    project = []
    with open(loc, 'r', encoding='utf-8') as location:
        for line in location:
            project.append(clear(line))
    return project


def pars(html, project_title, project_quality, kol):
    soup = BeautifulSoup(html)
    table = soup.find('table', class_='trade-list-table max-width')
    project = []
    for tr in table.find_all('tr', class_='cursor-pointer'):
        td = tr.find_all("td", class_="hidden-xs")[1:2]
        name = tr.find('td')
        place = td[0].find_all('div')[:1]
        trader = td[0].find_all('div')[1:]
        price = tr.find('td', class_='gold-amount bold')
        price = re.sub(r'\,', '', clear(price.text)[1:clear(price.text).find('X') - 1])
        time = tr.find('td', class_='bold hidden-xs')
        title = name.find('img').get('data-master-writ-description')
        set_trait = title[int(title.find('Set')) + 5:int(title.find("; Style"))]
        vouchers = name.find_all('div')[1].text
        vouchers = clear(vouchers[int(vouchers.find('Rewards')) + 8: int(vouchers.find('Vou') - 1)])
        if not clear(place[0].text) is None:
            pr = local_discard('txt/location.txt')
            if (title[int(title.find('Quality')) + 9:int(title.find("; Set"))]) in project_quality and \
                    (title[int(title.find('a(n)')) + 5:int(title.find(";"))]) in project_title \
                    and not clear(place[0].text) in pr and set_trait in set.main(kol):
                project.append({
                    "Title": title[int(title.find('a(n)')) + 5:int(title.find(";"))],
                    "Quality": title[int(title.find('Quality')) + 9:int(title.find("; Set"))],
                    "Set": set_trait,
                    "Style": title[int(title.find('Style')) + 7:],
                    "Vouchers": vouchers,
                    "Place": clear(place[0].text),
                    "Trader": clear(trader[0].text),
                    "Price": price,
                    "Time": time.get('data-mins-elapsed')
                })
        # print(clear(place[0].text))
    return project


def save(projects, path):
    with open(path, 'a', encoding="utf-8", newline='') as csv_file:
        writen = csv.writer(csv_file)
        writen.writerow(('WoodWork',))
        writen.writerow(
            ('Title', 'Quality', 'Set', 'Style', 'Vouchers', 'Place', 'Trader', 'Price', 'Time', 'Price per voucher'))
        writen.writerow('')

        for project in projects:
            if "Ruby Ash" in project['Title']:
                if project['Quality'] == 'Epic':
                    price_voucher = int((price_list.woodworking_sum_epic + constant.sanded_ruby_ash * 13))
                else:
                    price_voucher = int((price_list.woodworking_sum_legendary + constant.sanded_ruby_ash * 13))
            elif "Rubedite" in project['Title']:
                if project['Quality'] == 'Epic':
                    price_voucher = int((price_list.blacksmith_sum_epic + constant.rubedite_ingot * 13))
                else:
                    price_voucher = int((price_list.blacksmith_sum_legendary + constant.rubedite_ingot * 13))
            elif "Ancestor Silk" in project['Title']:
                if project['Quality'] == 'Epic':
                    price_voucher = int((price_list.clothing_sum_epic + constant.ancestor_silk * 13))
                else:
                    price_voucher = int((price_list.clothing_sum_legendary + constant.ancestor_silk * 13))
            elif "Rubedo Leather" in project['Title']:
                if project['Quality'] == 'Epic':
                    price_voucher = int((price_list.clothing_sum_epic + constant.rubedo_leather * 13))
                else:
                    price_voucher = int((price_list.clothing_sum_legendary + constant.rubedo_leather * 13))

            price_voucher = (int(project['Price']) + price_voucher) / int(project['Vouchers'])

            if price_voucher <= 710:
                writen.writerow((project['Title'], project['Quality'], project['Set'], project['Style'],
                                 project['Vouchers'], project['Place'], project['Trader'],
                                 project['Price'], project['Time'], price_voucher))


def main(project_title, project_quality, BASE_url, num_range, trait_kol):
    projects = []

    proxeis = open('txt//proxeis.txt').read().split('\n')
    useragents = open('txt//user-agent.txt').read().split('\n')

    for i in range(1, num_range):
        if i % 5 == 0 or i == 1:
            for j in range(0, 10):
                proxy = {'https': 'https://' + choice(proxeis)}
                # useragent = {'User-Agent': choice(useragents)}
                try:
                    html = get_html(BASE_url + str(i), proxy)
                    break
                except:
                    continue

        projects.extend(pars(html, project_title, project_quality, trait_kol))
        print('Pars', i)
    save(projects, 'Writ_Pars.csv')
    print('project save')


if __name__ == '__main__':
    WoodWork_URL = 'https://eu.tamrieltradecentre.com/pc/Trade/SearchResult?ItemID=12749&ItemNamePattern=Sealed+Woodworking+Writ&page='
    main(["Ruby Ash Bow"], ["Epic"], WoodWork_URL, 10, 5)
