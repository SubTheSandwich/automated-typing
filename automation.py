from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://typing-speed-test.aoeu.eu/')

type = driver.find_element_by_xpath('//*[@id="input"]')

global running
running = True


while running:
    try:

        current_word = driver.find_element_by_xpath('//*[@id="currentword"]').text
        modified = current_word + " "
        type.send_keys(modified)

    except:
        running = False
        print("No current word found. Process has been stopped.")
