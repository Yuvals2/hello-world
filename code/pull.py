from bs4 import BeautifulSoup
from urllib import request
from urllib.request import Request, urlopen
import smtplib
from email.mime.text import MIMEText
MAX_PRICE = 79

def send_email(subject, body, sender, recipient, password):
  msg = MIMEText(body)
  msg['Subject'] = subject
  msg['From'] = sender
  msg['To'] = recipient
  with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
    smtp_server.login(sender, password)
    smtp_server.sendmail(sender, recipient, msg.as_string())
def main():
  url = "https://www.pullandbear.com/il/%D7%A0%D7%A9%D7%99%D7%9D/%D7%91%D7%99%D7%92%D7%95%D7%93/%D7%92%27%D7%99%D7%A0%D7%A1/mom-fit-n6584"
  request_site = Request(url, headers={"User-Agent": "Mozilla/5.0"})
  html_doc = urlopen(request_site).read()
  soup = BeautifulSoup(html_doc, 'html.parser')
  all_jeans = soup.find_all('noscript')[1].find_all('p')
  prices = []
  for jeans in all_jeans:
    if jeans.contents[0][:2].isdigit():
      prices.append(float(jeans.contents[0]))
  p = min(prices)
  if p < MAX_PRICE:
    subject = "pull and bear jeans price"
    body = str(p)
    sender = "yuvalschrieber@gmail.com"
    recipient = "yuvalschrieber@gmail.com"
    password = "rhwm njxx neaf ktrl"
    send_email(subject, body, sender, recipient, password)

if __name__ == '__main__':
  main()
