# pymap
pymap = python3 + nmap. Im so fucking tried of copy+paste port number

# requriments
- subprocess
- argparse

# Q&A
- Why using sudo?

read [this](https://security.stackexchange.com/questions/175235/nmap-default-scan-technique) then you will know why sudo. Moreover, something ping sweeping with out sudo cannot detect some hosts... dunno why. If you know, pls let me know
- Why -T4 when ports scanning?

Sometime when I used -T5 is messed up or missed some open port... dunno why. If you know, pls let me know

# usage
```console
$ python3 pymap.py -h # man page
$ sudo python3 pymap.py -t $IP # scan top 10k port
$ sudo python3 pymap.py -t $IP -A # scan every port
$ sudo python3 pymap.py -t $IP -smb # samba scan
$ sudo python3 pymap.py -t $IP -nfs # nfs scan
$ sudo python3 pymap.py -t 192.168.1.0/24 -pS # ping sweep on network, looking for alive hosts
```

# todo:
- [x] samba: `nmap -p 445 --script=smb-enum-shares.nse,smb-enum-users.nse <ip>`
- [x] rpcbind: `nmap -p 111 --script=nfs-ls,nfs-statfs,nfs-showmount <ip>`
- [x] ping sweep
- [x] created cool banner
- [x] Only perfrom SYN scan!!, (sudo = alway -sS)
- [ ] improve speed (using thread?)
- [ ] script=smb-brute?
