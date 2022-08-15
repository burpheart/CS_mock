# CS_mock
模拟cobalt strike beacon上线包.  Simulation cobalt strike beacon connection packet.

拿到c2通信使用的RSA public key和提交metedata的url 即可模拟上线

Use the CobaltStrikeParser extract public key from the payload https://github.com/Sentinel-One/CobaltStrikeParser  parse_beacon_config.py payload_url --json

Remember to remove the extra padding from the public key
![](CSMOCK.png)


matadata 协议结构

``` 
        ┌─────────────────────────────────────────────────┐
        │                      head                       │
        ├──────────────────────────┬──────────────────────┤
        │         4  Byte          │      4  Byte         │
        ├──────────────────────────┼──────────────────────┤
        │    magic 00 00 be ef     │     metadata_len     │
        ├──────────────────────────┴──────────────────────┤
        │                     metadata                    │
        ├─────────────────────────────────────────────────┤
        │                     16 Byte                     │
        ├─────────────────────────────────────────────────┤
        │                     aes_key                     │
        ├────────┬────────┬────────┬───────┬──────┬───────┤
        │ 2 byte │ 2 byte │ 4 byte │ 4 byte│2 byte│ 1 byte│
        ├────────┼────────┼────────┼───────┼──────┼───────┤
        │os_info1│os_info2│   id   │  pid  │ port │ flag  │
        ├────────┼────────┼────────┼───────┼──────┼───────┤
        │ 1 byte │ 1 byte │ 2 byte │ 4 byte│4 byte│4 byte │
        ├────────┼────────┼────────┼───────┼──────┼───────┤
        │ os_ver │os_ver_2│os_bulid│ ptr_1 │ptr_2 │ptr_3  │
        ├────────┴────┬───┴────────┴───────┴──────┴───────┤
        │   4 byte    │          TAB split TEXT           │
        ├─────────────┼───────────────────────────────────┤
        │inner_ip_addr│ computername username processname │
        └─────────────┴───────────────────────────────────┘

```
