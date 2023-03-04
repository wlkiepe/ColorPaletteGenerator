# import everything that I will need
import colorgram
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains


# Make a function to convert rgb to hexcode. Colorgram will give me colors in RGB, but when I have selenium go to
# colorhunt it wil require inputs in hexcode.
def rgb2hex(r, g, b):
    return "#{:02x}{:02x}{:02x}".format(r, g, b)


# Use a for loop with colorgram and the rgb2hex function to create a list of hexvalues based on the image
# 'Watermelon.jpeg'
hex_colors = []
colors = colorgram.extract('Watermelon.jpg', 4)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    hex_color = rgb2hex(r, g, b)
    hex_colors.append(hex_color)

# I had the program print the list of hexcodes so that I could manually check that the program was working properly, but
# after I ran some test I commented it out

# print(hex_colors)

# Set up my driver and ActionChains since I will need to do that
chromedriver_path = "C:/Users/Winny/Desktop/Web_Development/chromedriver.exe"
s = Service(chromedriver_path)
driver = webdriver.Chrome(service=s)
ac = ActionChains(driver)

# Have Selenium go to colorhunt's create a palette page.
driver.get("https://colorhunt.co/create")

# Make the first tile on the palette change colors to the first hexcode value in my list.
tile1 = driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div[1]/div[2]/div[1]/div[4]")
tile1.click()
color_selector = driver.find_element(By.ID, 'colorInput')
color_selector.clear()
color_selector.send_keys(hex_colors[0])
color_selector.send_keys(Keys.RETURN)

# Make the second tile on the palette change colors to the second hexcode value on my list.
# Because the tile elements overlap each other, Selenium was giving me an ElementNotSelectableException.
# To circumvent the exception I used ActionChains to click on a specific point of the webpage that would allow me to
# click on the second color palette tile.
tile2 = driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div[1]/div[2]/div[1]/div[3]")
ac.move_to_element(tile2).move_by_offset(0, 100).click().perform()
color_selector = driver.find_element(By.ID, 'colorInput')
color_selector.clear()
color_selector.send_keys(hex_colors[1])
color_selector.send_keys(Keys.RETURN)

# Make the 3rd tile on the palette change colors to the third hexcode value on my list.
# Similar to tile2. I needed to use ActionChains to avoid the ElemenentNotSelectableException, but I realized I could
# click on tile3 in the website using the same locator tile2, so no need to find a new element, I only have to change
# the move_by_offset y value.
ac.move_to_element(tile2).move_by_offset(0, 150).click().perform()
color_selector = driver.find_element(By.ID, 'colorInput')
color_selector.clear()
color_selector.send_keys(hex_colors[2])
color_selector.send_keys(Keys.RETURN)

# Make the 4th tile the final color. Done with the same process as the 3rd tile.
tile2 = driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div[1]/div[2]/div[1]/div[3]")
ac.move_to_element(tile2).move_by_offset(0, 210).click().perform()
color_selector = driver.find_element(By.ID, 'colorInput')
color_selector.clear()
color_selector.send_keys(hex_colors[3])
color_selector.send_keys(Keys.RETURN)

# I need a way to make sure that Selenium doesn't close the window before I am able to view it, so I created an
# input function to prompt the user to answer if they like it. Once answered the program will finish running.
input("Do you like your palette? Yes or No: ")

driver.quit()

