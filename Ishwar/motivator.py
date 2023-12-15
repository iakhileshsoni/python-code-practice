import requests
from twilio_conn import send_whatsapp_txt, client

def get_quote_of_the_day(category):
    url = "https://quotes.rest/god?language=en&category={}".format(category)
    res = requests.get(url=url)
    data = res.json()
    status = res.status_code
    match status:
        case 200:
            quote = data['contents']['quote']
        case 400:
            quote = data['error']['message']
        case _:
            quote = "Sorry, couldn't get the data"
    return quote

quote = get_quote_of_the_day(category='inspect')
send_whatsapp_txt(client, quote)