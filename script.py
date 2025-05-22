import subprocess
from os import *
from getpass import getpass

# Regra: uso de eval()
user_input = input("Digite um código Python para executar: ")
eval(user_input)

# Regra: senha hardcoded
password = "password"

# Regra: subprocess com shell=True
subprocess.run("ls -la", shell=True)

# Regra: importação com wildcard
from math import *

# Regra: uso de assert
def checar_idade(idade):
    assert idade >= 18, "Menores de idade não permitidos"

checar_idade(16)
