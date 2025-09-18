# Currently chrome validate this regex to validate the email

import re

email = input("What is your email?\n").strip()

pattern = r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+" \
          r"@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?" \
          r"(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$"

if re.fullmatch(pattern, email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")
