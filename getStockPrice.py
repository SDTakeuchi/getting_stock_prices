from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import smtplib
import random

# enter your stock's tickers ----------------------------

stocks = ["BBY", "DAL", "GLD", "KO", "VOO"]

#--------------------------------------------------------

PATH = "C:/chromedriver.exe"
URL = 'https://www.google.com/'

headers = {"User-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}

message = 'Here are your stock prices!\n'
greetings = ["Tsup!", "Hey!", "Hi!", "Good day!", "Sup!", "Bonjour!", "Hola!"]

def gettingStockPrice():   
    print(greetings[random.randint(0,6)] +" I'll get you the stock prices now, hold on a sec...")
    driver = webdriver.Chrome(PATH)
    global message
    for stock in stocks:
        driver.get(URL)

        search = driver.find_element_by_name("q")
        search.send_keys(stock + " stock price")
        search.send_keys(Keys.RETURN)

        price = driver.find_element_by_xpath('//*[@id="knowledge-finance-wholepage__entity-summary"]/div/g-card-section/div/g-card-section/span[1]/span/span[1]')
        message = message + "\n" + stock + ": $" + str(price.text)
        
    driver.quit()

def sendEmail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    pwd = "wihazgtprwpoqpfg"
    emailAddress = 'kuranku191952996@gmail.com'

    server.login(emailAddress, pwd)

    subject = greetings[random.randint(0,6)] + " here are your stock prices"
    global message 
    body = message

    msg = f"Subject:{subject}\n\n{body}"

    server.sendmail(
        'kuranku191952996@gmail.com',
        'kuranku191952996@gmail.com',
        msg
    )
    
    print('Alright, email has been sent. Have a good day.')

    server.quit()

if __name__ == "__main__":
    gettingStockPrice()
    sendEmail()