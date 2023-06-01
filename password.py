from random import *
base = "abcdefghijklmnopqrstuvwxyz0123456789"
motdepasse = ""
for i in range(8):
    motdepasse=motdepasse+choice(base)
print(motdepasse)
