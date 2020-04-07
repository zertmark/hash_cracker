#!/bin/python3
import threading
import time
import argparse
import sys
import os 
import colorama
from colorama import Fore,Back,Style
import hashlib 
from hashlib import *
colorama.init()
banner="""                  ▄▄  ▄▄▄▄▄▄▄▄                                ▄▄        ▄▄
       ██        ██   ▀▀▀▀▀███                        ██       █▄        █▄
      ██        ██        ██▀    ▄████▄    ██▄████  ███████     █▄        █▄
     ██        ██       ▄██▀    ██▄▄▄▄██   ██▀        ██         █▄        █▄
    ▄█▀       ▄█▀      ▄██      ██▀▀▀▀▀▀   ██         ██          █▄        █
   ▄█▀       ▄█▀      ███▄▄▄▄▄  ▀██▄▄▄▄█   ██         ██▄▄▄        █▄        █▄
  ▄█▀       ▄█▀       ▀▀▀▀▀▀▀▀    ▀▀▀▀▀    ▀▀          ▀▀▀▀         █▄        █▄
                                Hash Cracker
"""
def print_banner():
 while line<lines and not 'is correct' in password:
  time.sleep(1)
  os.system('clear') 
  print(Fore.GREEN+banner+"""

                                                                                             
                                                                        
                            Try:{0}/{1}                         
                            Current password:{2}                
                            Hash:{3}                                                                                                                                                                                                                                                 
""".format(line,lines,password,hash)+Fore.RESET)
 sys.exit()
def parse_args():
 global hash_type,wordlist,start_time,path_to_hash
 parser = argparse.ArgumentParser(description="Hash Cracker")
 parser.add_argument("hash", help="Type of hash:md5,sha256,sha1,sha224,sha384,sha512")
 parser.add_argument("--file", help="File with hash")
 parser.add_argument("--wordlist", help="Wordlist file")
 args = parser.parse_args()
 hash_type=args.hash
 path_to_hash=args.file
 wordlist=args.wordlist
 start_time=time.time()
def main():
 parse_args()
 read_hash()
 crack()
def hash_check(passwd):
 if hash_type=="md5":
  hash_output=md5(passwd).hexdigest()
 if hash_type=="sha512":
  hash_output=sha512(passwd).hexdigest()
 if hash_type=="sha256":
  hash_output=sha256(passwd).hexdigest()
 if hash_type=="sha384":
  hash_output=sha384(passwd).hexdigest()
 if hash_type=="sha224":
  hash_output=sha224(passwd).hexdigest()
 if hash_type=="sha1":
  hash_output=sha1(passwd).hexdigest()
 return hash_output
def crack():
 global line,password
 line=0;password=""
 thread=threading.Thread(target=print_banner)
 thread.start()
 with open(wordlist,'r', errors='ignore') as words_file:
  for pas in words_file.readlines():
   password=pas
   line+=1
   if hash_check(password.strip().encode()) == hash.strip():  
    password="{} is correct(PASSWORD FOUND)".format(pas.strip())+'\n                            Time:{}'.format(get_time())
    exit()
   else:
    continue
  print(Fore.RED+'Password not found'+Fore.RESET)
  exit() 
def get_time():
 result=time.time()
 output=result-start_time
 return str(output)
def read_hash():
 global hash,lines
 lines=0
 with open(path_to_hash,'r') as file:
  hash=file.read()
 print("Found hash:{}".format(hash))
 with open(wordlist,'r',errors='ignore') as o:
  for i in o.readlines():
   lines+=1
 print("Found {} passwords".format(lines))
main()
