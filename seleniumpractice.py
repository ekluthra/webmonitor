from selenium import webdriver
import time
browser = webdriver.Chrome('C:/Users/eklut/.wdm/drivers/chromedriver/win32/84'
                           '.0.4147.30/chromedriver.exe')
browser.get('https://www.sportchek.ca/categories/shop-by-sport/fitness'
            '/weightlifting/weights/product/york-50-lb-adjustable-spinlock'
            '-dumbbell-set-282070060.html#282070060=282070060990000')
browser.minimize_window()
while True:
    try:
        browser.find_element_by_class_name('out-of-stock')
        print('it out of stock')
    except:
        print('it is in stock')

    browser.refresh()
    time.sleep(60)

