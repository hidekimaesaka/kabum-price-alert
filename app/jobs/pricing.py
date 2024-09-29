from requests import Session

from bs4 import BeautifulSoup

from app.repo.product import ProductRepo

product_repo = ProductRepo()


def scrape_price(product_link):

    with Session() as session:
        
        http_response = session.get(product_link)

        response_text = http_response.text

        page_soup = BeautifulSoup(response_text, 'html.parser')

        purchase_div = page_soup.find_all('div', class_='container-purchase')[0]

        product_price = purchase_div.h4

        return product_price


def update_product_price():

    products = product_repo.get_products()

    for product in products:
        price = scrape_price(product.product_link)

        product_id = product[0]
        text_price = price.getText().replace('R$\xa0','').replace(',', '.')

        product_repo.update_product_price(product_id, text_price)


