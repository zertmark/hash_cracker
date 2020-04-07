# hash_cracker
Simple hash bruteforcer on Python 3                                               
# INSTALL:                               
git clone https://github.com/zertmark/hash_cracker.git && cd hash_cracker && chmod +x hash_cracker                       
# RUN:                                                   
./hash_cracker -h                                                               
usage: hash_cracker.py [-h] [--file FILE] [--wordlist WORDLIST] hash

Hash Cracker

positional arguments:
  hash                 Type of hash:md5,sha256,sha1,sha224,sha384,sha512

optional arguments:                                         
  -h, --help           show this help message and exit                                                   
  --file FILE          File with hash                                                                           
  --wordlist WORDLIST  Wordlist file                                                                 
