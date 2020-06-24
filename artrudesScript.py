#Made by https://www.fiverr.com/gustavomatteo
#Remove the <> from vars
#import instapy
from instapy import InstaPy

#Set your account here: 
# username = <username>
# password = <pass>
session =InstaPy(username="justgustavomatteo", password="68762982$").login()

#login
session.login()

#Set your tag here: <tag> and the amount of likes: <likes>
session.like_by_tags(["fiverr_matteo"], amount=200)

#ignore account's req.
session.set_relationship_bounds(enabled=False)

#Set if you want to comment posts:
# True for comments and False if you don't want to comment
# percentage = lower values will decrease the chance of your account comment the post
#Set the comments you will drop at the post changing <comment1>, <comment2>, <comment3>. The bot will comment it randomly and if you want to add more options of comments, just write a , and than "<commentNew>"
session.set_do_comment(True, percentage=50)
session.set_comments(["test1", "test2", "test3"])

#finish the program
session.end()

#Made by https://www.fiverr.com/gustavomatteo