from app.repo.alert import AlertQueueRepo

from app.service.mail import send_email


alert_queue_repo = AlertQueueRepo()

def build_message(product_link, price):

    msg = f'Hey! If you are receiving this email, the product {product_link} is now at the price you want! Yeah this is now costing R$: {price}'

    return msg

def send_alerts():
    
    queue = alert_queue_repo.get_queue()

    for item in queue:

        item_id = item[0]
        msg = build_message(item[1], item[2])
        mail_to = item[3]

        send_email(mail_to, msg)
        alert_queue_repo.remove_queue(item_id)
