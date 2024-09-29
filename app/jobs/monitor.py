from app.repo.product import ProductRepo
from app.repo.alert import AlertQueueRepo
from app.repo.user import UserRepo


user_repo = UserRepo()
product_repo = ProductRepo()
alert_queue_repo = AlertQueueRepo()


def alert_user(user_id, actual_price, product_link):
    
    user = user_repo.get_user_by_id(user_id)[0]
    user_email = user[2]
    
    alert_queue = {
        'product_link':product_link,
        'product_price': actual_price,
        'user_email': user_email
    }

    alert_queue_repo.add_queue(**alert_queue)

def convert_price_value(price_value):

    converted_price_value = ''

    destructured_price = price_value.split('.')

    values_len = len(destructured_price) - 1

    for v in range(values_len):
        converted_price_value += destructured_price[v]

    return converted_price_value

def watch_for_price_decrease():
    
    priced_products = product_repo.get_products_to_alert()

    for product in priced_products:
        desired_price = product[4]
        actual_price = product[5]

        user_id = product[1]
        product_link = product[3]

        converted_desired_price_str = convert_price_value(desired_price)
        converted_actual_price_str = convert_price_value(actual_price)

        converted_desired_price = int(converted_desired_price_str)
        converted_actual_price = int(converted_actual_price_str)

        should_alert_user = converted_actual_price <= converted_desired_price

        if should_alert_user:
            alert_user(user_id, converted_actual_price, product_link)
