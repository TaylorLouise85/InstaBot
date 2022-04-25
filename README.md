# InstaBot
This project is an Instagram bot using InstaPy. The bot opens Firefox, logs into an Instagram account, and will go to different posts based on hashtags and will like the posts.

There have been a lot of changes to the Instagram source code that caused a problem with using InstaPy, so some of the files needed to be adjusted for InstaPy to work. Originally the bot was able to go into the account, find the post, but was not able to like or follow the account.

In order for it to work, geckodriver needs to be installed and put into the path. the updated InstaPy files also need to be installed.

Once everything is installed, you need to input a username and password for the account, and it will go into the account and start liking posts based on hashtags. There can be a limit set for how many posts that the bot likes to avoid the Instagram bot control features

https://realpython.com/instagram-bot-python-instapy/
