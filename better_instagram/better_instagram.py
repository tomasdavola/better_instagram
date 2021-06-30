import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from webdriver_manager.chrome import ChromeDriverManager
ratelimited=False


def login(username,password):
    global browser
    global ratelimited
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get('https://www.instagram.com')
    browser.implicitly_wait(1)
    try:
        userinput = browser.find_elements_by_css_selector('form input')[0]
        passwordinput = browser.find_elements_by_css_selector('form input')[1]
        userinput.send_keys(username)
        passwordinput.send_keys(password)
        passwordinput.send_keys(Keys.ENTER)
        time.sleep(3)
        browser.implicitly_wait(1)
        try:
            notification = browser.find_element_by_class_name('cmbtv')
            notification.click()
        except selenium.common.exceptions.NoSuchElementException:
            print(
                "Instagram has ratelimied you(only lasts like 10 minutes), you can try a VPN or a different account, I will try find a work around this in BetterInstagram 0.0.1+")
            ratelimited = True
            return
    except IndexError:
        browser.quit()
        login(username, password)


def getuser(username):
    global browser
    global ratelimited
    if ratelimited:
        return
    userinfo={}
    span=[]
    #Username
    userinfo["username"] = username
    #Setup for no login call
    try:
        browser.get(f'https://www.instagram.com/{username}')
    except NameError:
        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser.get(f'https://www.instagram.com/{username}')
    #Name & Setup
    try:
        name = browser.find_element_by_class_name("rhpdm")
        userinfo["name"]=name.text
    except selenium.common.exceptions.NoSuchElementException:
        if browser.current_url=='https://www.instagram.com/accounts/login/':
            print("it seems instagram is forcing a login for this URL.")
            return
        else:
            userinfo["name"] = ''
    # #Bio Placeholder
    userinfo["biography"]=""
    #Number Info
    headinfo = browser.find_elements_by_class_name("g47SY")
    userinfo["posts"]=headinfo[0].text
    userinfo["followers"] = headinfo[1].text
    userinfo["following"] = headinfo[2].text
    #Verified
    try:
        isverified=browser.find_element_by_class_name("mTLOB")
    except selenium.common.exceptions.NoSuchElementException:
        isverified=False
    try:
        if isverified.text=="Verified":
            isverified=True
    except AttributeError:
        pass
    userinfo["is_verified"]=isverified
    #Website
    try:
        website=browser.find_element_by_class_name("yLUwa")
    except selenium.common.exceptions.NoSuchElementException:
        website= None
    try:
        userinfo["website"]=website.text
    except AttributeError:
        userinfo["website"] = website
    #You are following
    try:
        youarefollowing=browser.find_element_by_class_name("_5f5mN")
    except selenium.common.exceptions.NoSuchElementException:
        youarefollowing = browser.find_element_by_class_name("sqdOP")
    if youarefollowing.text == "Follow":
        youarefollowing=False
    else:
        youarefollowing=True
    userinfo["are_you_following"]=youarefollowing
    #URL
    userinfo["url"]=browser.current_url
    #Bio
    bio=browser.find_elements_by_tag_name("span")
    biocount=0
    for x in bio:
        span.append(str(x.text))
    while biocount<10:
        for i in span:
            if i == userinfo["posts"]:
                span.remove(i)
            if i == userinfo["followers"]:
                span.remove(i)
            if i == userinfo["following"]:
                span.remove(i)
            if i == f'{userinfo["posts"]} posts':
                span.remove(i)
            if i == '':
                span.remove(i)
            if i == 'Verified':
                span.remove(i)
            if i == 'Follow':
                span.remove(i)
        biocount+=1
    if span[0]=='POSTS' or span[0][:12]=='Followed by ':
        span[0]=""
    userinfo["biography"]=span[0]

    return userinfo