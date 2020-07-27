# pymap
pymap = python3 + nmap. Im so fucking tried of copy+paste port number

# requriments
- subprocess
- argparse

# usage
```py
python3 pymap.py -h
```
# todo:
- [ ] samba: `nmap -p 445 --script=smb-enum-shares.nse,smb-enum-users.nse <ip>`
- [ ] rpcbind: `nmap -p 111 --script=nfs-ls,nfs-statfs,nfs-showmount <ip>`
- [ ] improve speed