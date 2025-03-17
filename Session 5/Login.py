class UserAuthentication:
    def login(self):
        pass

class EmailPasswordAuth(UserAuthentication):
    def login(self):
        return "Logging in with email and password."

class GoogleAuth(UserAuthentication):
    def login(self):
        return "Logging in with Google authentication."

class FingerprintAuth(UserAuthentication):
    def login(self):
        return "Logging in with fingerprint authentication."

auth_methods = [EmailPasswordAuth(), GoogleAuth(), FingerprintAuth()]

for auth in auth_methods:
    print(auth.login())
