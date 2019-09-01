import requests
from bs4 import BeautifulSoup
import smtplib
import time

# URL of the Amazon item you want to track
URL = 'https://www.amazon.co.uk/Sony-ILCE6300M-Compact-SEL18135-F3-5-5-6/dp/B07C14ZH4B' 
#'https://www.amazon.co.uk/Sony-ILCE6300M-Compact-SEL18135-F3-5-5-6/dp/B07C14ZH4B/ref=sr_1_1_sspa?keywords=sony+alpha+e+mount&qid=1567273035&s=gateway&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyRjhTV0RITTVRNDFBJmVuY3J5cHRlZElkPUEwNjc0NDAwMUhUOTA2UzcxWjNQVyZlbmNyeXB0ZWRBZElkPUEwNDMzNjY1MkdURFNGWkozUU9BTSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='

# Simply Google search 'my user agent'
headers = {
	"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}

def check_price():
	page = requests.get(URL, headers=headers)

	soup1 = BeautifulSoup(page.content, "html.parser")
	soup = BeautifulSoup(soup1.prettify(), 'html.parser')

	title = soup.find(id="productTitle").get_text()
	price = soup.find(id="priceblock_ourprice").get_text()
	converted_price = float(price.strip().replace(',','')[1:-1])

	#define the max price you're willing to pay
	threshold = 400

	if (converted_price < threshold):
		send_email()

	print(converted_price)
	print(title.strip())



def send_email():
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo() 
	server.starttls() #encrypts the connection
	server.ehlo()

	# fill in 
	server.login('gmail_address', 'generated_gmail_app_password')

	subject = 'Price of an Amazon item you wanted has fallen.'
	body = f"Check the Amazon link {URL}"
	message = f"Subject: {subject}\n\n{body}"

	#fill in
	server.sendmail('gmail_address', 'target_email_address', message)

	print('Notification email has been sent')

	server.quit()


check_price()

##if you want to continuously check the price 
# while(True):
# 	check_price()
# 	time.sleep(60) #number of seconds between each check







