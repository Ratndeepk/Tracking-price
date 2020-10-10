#some important libraries
import requests
from bs4 import BeautifulSoup  #parse all data and return individual items only
import smtplib   #protocol to send an email

#url to scrap data from you can change it to whatever data you're scrapping
URL = 'https://www.amazon.in/dp/B077Q7GW9V/ref=gwdb_bmc_1_CP_Latest_RedmiNote9Pro?pf_rd_s=merchandised-search-7&pf_rd_t=Gateway&pf_rd_i=mobile&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_r=5BSQNMWEX5ZPDV3KZ35W&pf_rd_p=6c1f63dd-d673-460c-aa20-1a9261118fde'

#search for my user agent 
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}


# what's the current price? if less let's get an email
def check_price():
    #this will return all data from website 
    page = requests.get(URL, headers = headers)

    soup = BeautifulSoup(page.content,'html.parser')

    # scrap individual data
    title = soup.find(id="productTitle").get_text() 
    price = soup.find(id="priceblock_ourprice").get_text()    #string value
    price = price[2:]     # removing currency symbol

    try:
        price =int(float(price.replace(',','')))    #just removing comma converting into integer :D
    except:
        pass
    
    # time to get an email 
    if int(price)<15000:
        send_mail()
    print(title.strip()) #strip to remove spaces only (Comment it if needed)
    
# you need to do two-step verification of email or you can simply allow less secure apps 
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()        # just estabilishing connection with gmail  
    server.starttls()    #encrypt connection
    server.ehlo()

    server.login('ratndeepk07@gmail.com','xvqcrryysdxapvzw')  #generate this password using google app passwords

    # this will be sent on email (change accordingly)
    subject  = 'Hey! Price fall down'
    body = 'Check the amazon link -> https://www.amazon.in/dp/B077Q7GW9V/ref=gwdb_bmc_1_CP_Latest_RedmiNote9Pro?pf_rd_s=merchandised-search-7&pf_rd_t=Gateway&pf_rd_i=mobile&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_r=5BSQNMWEX5ZPDV3KZ35W&pf_rd_p=6c1f63dd-d673-460c-aa20-1a9261118fde'

    msg = f"Subject:{subject}\n\n{body}"

    # ughhh sending sending email
    server.sendmail('ratndeepk07@gmail.com','nagendra.cse1@gmail.com',msg)       # senders email & receiver emails

    print("Email sent")

    server.quit()

check_price()
