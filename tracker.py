import requests
from bs4 import BeautifulSoup
import smtplib
URL = 'https://www.amazon.ca/DualShock-Jet-Black-Controller-PlayStation/dp/B01LBH9ILW/ref=sr_1_4?keywords=ps4&qid=1567889111&s=gateway&sr=8-4'

headers = {
    "User Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()

    converted_price = float(price[4:15])

    if (converted_price < 65):
        send_mail()

    print(title.strip())
    print(converted_price)

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('enter gmail here', 'enter password here')
    subject = 'Check amazon link '
    body = 'https://www.amazon.ca/DualShock-Jet-Black-Controller-PlayStation/dp/B01LBH9ILW/ref=sr_1_4?keywords=ps4&qid=1567889111&s=gateway&sr=8-4'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'from address',
        'to address',
        msg
    )
    server.quit()