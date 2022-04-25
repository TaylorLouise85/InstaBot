# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 12:35:51 2022

@author: Taylo
"""

from instapy import InstaPy

session = InstaPy(username='thornfieldvegan', password = '6Ys.E+', want_check_browser=False)

session.login()

users = session.target_list("C://Users//Taylo//Desktop//InstaBot//users.txt")
session.follow_user_followers(users, amount=10, randomize=False)

session.set_do_follow(enabled = True, percentage=50)
session.like_by_tags(["vegan", "plantbased", "veganlife"], amount=10)


session.end()