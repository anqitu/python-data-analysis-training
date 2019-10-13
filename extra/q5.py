# Q5
# A website requires the users to input username
# and password to register. Write a class Registration to check
# the validity of registration data. The username and
# password are to be initialised when the Registration
# object is created and should be stored as object attributes.
# The class has one method validatePassword which will return a
# boolean indicating the validity of the password.
# Following are the criteria for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 1. At least 1 letter between [A-Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 6
# 5. Maximum length of transaction password: 12
#
# Usage:
# r = Registration("username", "password")
# r.validatePassword() # false
# r = Registration("username", "P@ssW0rd")
# r.validatePassword() # true
#
# Hints:
# Consider using built-in functions any() and all()
# Consider using the built-in string library

from string import ascii_lowercase, ascii_uppercase, digits

class Registration:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def validatePassword(self):
        digitPass = any([d in self.password for d in digits])
        lowercasePass = any([l in self.password for l in ascii_lowercase])
        uppercasePass = any([l in self.password for l in ascii_uppercase])
        minLengthPass = len(self.password) >= 6
        maxLengthPass = len(self.password) <= 12
        specialPass = any([l in self.password for l in '$@#'])
        return all([digitPass, lowercasePass, uppercasePass,
            minLengthPass, maxLengthPass, specialPass])

r = Registration("username", "password")
r.validatePassword()

r = Registration("username", "P@ssW0rd")
r.validatePassword()
