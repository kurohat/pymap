# pymap
pymap = python3 + nmap. Im so fucking tried of copy+paste port number

# requriments
- subprocess
- argparse

# usage
```console
$ python3 pymap.py -h
$ python3 pymap.py -t $IP # scan top 10k port
$ python3 pymap.py -t $IP -all # scan every port
$ python3 pymap.py -t $IP -smb # samba scan
$ python3 pymap.py -t $IP -nfs # nfs scan
```
# todo:
- [x] samba: `nmap -p 445 --script=smb-enum-shares.nse,smb-enum-users.nse <ip>`
- [x] rpcbind: `nmap -p 111 --script=nfs-ls,nfs-statfs,nfs-showmount <ip>`
- [ ] improve speed (using thread?)