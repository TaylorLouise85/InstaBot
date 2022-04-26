# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 12:30:56 2022

@author: TJ Augustine
"""
'''
from time import sleep
from selenium import webdriver

#uses firefox
browser = webdriver.Firefox()
browser.implicitly_wait(5)

#goes to instagram
browser.get('https://www.instagram.com/')

#looks for log in button (This could be used in other apps as well)
#login_link = browser.find_element_by_xpath("//a[text()='Log in']")
#login_link.click()

#gives it time to load
sleep(2)

username_input = browser.find_element_by_css_selector("input[name='username']")
password_input = browser.find_element_by_css_selector("input[name='password']")

username_input.send_keys("CS453Project")
password_input.send_keys("InstaPython-2022")

login_button = browser.find_element_by_xpath("//button[@type='submit']")
login_button.click()

#gives it time to load
sleep(2) 

search_input = browser.find_element_by_css_selector("input[name='Search']")
username_input.send_keys("tj_augustine")
browser.close()

from instapy import InstaPy

session = InstaPy(username="CS453Project", password="InstaPython-2022")
session.login()
'''
#above is how to get into Instagram using the webdriver
#below is the simplified version from InstaPy

#imports InstaPy
from instapy import InstaPy

#this creates a session with values for the username and password
#NOTE Taylor and I created two different accounts
session = InstaPy(username='CS453Project', password = 'InstaPython-2022', want_check_browser=False)
#this opens the firefox browser and logs in
session.login()

#these two lines go to a list of accounts that Taylor chose to follow
users = session.target_list("C://Users//Taylo//Desktop//InstaBot//users.txt")
session.follow_user_followers(users, amount=10, randomize=False)

#these are the actions that the bot does
session.set_do_follow(enabled = True, percentage=50) #follows 50% of the accounts that it interacts with
session.like_by_tags(["mlb", "phillies", "sixers"], amount=10) # hashtags of the posts that the account finds and interacts with (10 means it finds 10 posts)
session.set_do_comment(True, percentage=50)#percentage of posts that the bot comments on
session.set_comments(["Awesome!", "Sweet!"])#list of things that the bot will  comment


session.end()
