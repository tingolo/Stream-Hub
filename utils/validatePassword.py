import bcrypt

def generateHashPassword(password: str):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode("utf-8"), salt)
    return hashed.decode("utf-8")

def verifyPassword(password: str, hashedPassword: str):
    status = bcrypt.checkpw(password.encode("utf-8"), hashedPassword.encode("utf-8"))
    return status