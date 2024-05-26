#!/usr/bin/python
#######################################
#               TorCrack              #
#   https://github.com/victorpavoni   #
#######################################
import crypt,sys

hash = str(input("Hash: "))
salt = str(input("Salt: "))
wordlist = str(input("Wordlist: "))

with open(wordlist, 'r') as wl:
    linhas = wl.readlines()

    for linha in linhas:
        comppass = linha.strip()
        comp = crypt.crypt(comppass, salt)
        if comp == hash:
            print(f"[+] Senha encontrada: {comppass}")
            sys.exit(0)
        else:
            print(f"Testando {comppass}...")
    print("Senha não encontrada =(")
    sys.exit(0)
