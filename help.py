#-----!!!DONT CHANGE THIS!!!-----#
# This is a program to help you to know the words on the program!!!
from argparse import ArgumentParser
from importlib import import_module as eximport
from hashlib import sha256
from json import (
    dumps as stringify,
    loads as parse
)
from os import (
    getenv,
    kill,
    listdir,
    makedirs,
    mkdir,
    mknod,
    popen,
    remove,
)
from os.path import (
    abspath,
    basename,
    dirname,
    isdir,
    isfile,
    join
)
from platform import uname
from re import search, sub
from shutil import (
    copy2,
    get_terminal_size,
    rmtree,
)
from signal import (
    SIGINT,
)
from subprocess import (
    DEVNULL,
    PIPE,
    Popen,
    run
)
from smtplib import SMTP_SSL as smtp
from sys import (
    stdout,
    version_info
)
from tarfile import open as taropen
from time import (
    sleep,
)
from zipfile import ZipFile

# Color snippets
black="\033[0;30m"
red="\033[0;31m"
bred="\033[1;31m"
green="\033[0;32m"
bgreen="\033[1;32m"
yellow="\033[0;33m"
byellow="\033[1;33m"
blue="\033[0;34m"
bblue="\033[1;34m"
purple="\033[0;35m"
bpurple="\033[1;35m"
cyan="\033[0;36m"
bcyan="\033[1;36m"
white="\033[0;37m"
nc="\033[00m"

version="1.2.0"

# Regular Snippets
ask = f"{green}[{white}?{green}] {yellow}"
success = f"{yellow}[{white}√{yellow}] {green}"
error = f"{blue}[{white}!{blue}] {red}"
info = f"{yellow}[{white}+{yellow}] {cyan}"
info2 = f"{green}[{white}•{green}] {purple}"
final = f"{blue}[{green}:){blue}] {blue}"

# Aqui começa o novo código
import time

def main():
    user_input = input(f"{ask}Você precisa de ajuda com o programa? (y/n): ")
    if user_input.lower() == 'y':
        print(f"{info}Ok! Carregando...")
        time.sleep(1)
        print("Installing python3...")
        time.sleep(1.1)
        print(f"Installing help {version}...")
        time.sleep(1.1)
        print("Running...")
        time.sleep(1.1)
        print(f"{green}Please wait...")
        time.sleep(1.1)
        print(f"{info} Thi is in development!!!")
    else:
        print(f"{final} Se precisar de ajuda mais tarde, não hesite em perguntar.")
        time.sleep(2)  # Aguarda 2 segundos antes de encerrar o programa

if __name__ == "__main__":
    main()