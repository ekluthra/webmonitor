from selenium import webdriver
import ezgmail
import time

#browser
browser = webdriver.Chrome('C:/Users/eklut/.wdm/drivers/chromedriver/win32/84'
                           '.0.4147.30/chromedriver.exe')
browser.get('https://www.sportchek.ca/categories/shop-by-sport/fitness'
            '/weightlifting/weights/product/york-50-lb-adjustable-spinlock'
            '-dumbbell-set-282070060.html#282070060=282070060990000')
browser.minimize_window()
while True:
    try:
        #if its out of stock, do nothing
        browser.find_element_by_class_name('out-of-stock')
    except:
        #else exit the loop
        print('it is in stock')

    browser.refresh()
    time.sleep(900)

#send email saying that it's in stock
