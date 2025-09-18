# Here we can take username from any of the link
import re
url = input("URL: ").strip()
'''
UserName = url.removeprefix("https://x.com/")  # https://x.com/_manvendra31
print(f"Username: {UserName}")
'''

# re sub used

UserName = re.sub(r"https://x.com/","",url)
print(f"Username: {UserName}")
