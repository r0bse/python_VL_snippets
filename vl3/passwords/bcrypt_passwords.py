# https://martinheinz.dev/blog/59
# pip install passlib
from passlib.hash import bcrypt
from getpass import getpass

print(bcrypt.setting_kwds)
# ('salt', 'rounds', 'ident', 'truncate_error')
print(bcrypt.default_rounds)
# 12
bcrypt.salt = getpass("insert salt: ")
hasher = bcrypt.using(rounds=13)  # Make it slower

password = getpass()
hashed_password = hasher.hash(password)
print(hashed_password)

# $2b$13$P4Sxe61JUWaIoVjxv1AsteSMtuDGMf6ObZSxT4gG7w3zZ4AwknW9q
# \__/\/ \____________________/\_____________________________/
# Alg Rounds  Salt (22 char)            Hash (31 char)

print(hasher.verify(password, hashed_password)) # True
print(hasher.verify("wrong-password", hashed_password))