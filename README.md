# pymap
Pymap provides an easy way to use Nmap. With Pymap, you can forget different flags that you need to provide to Nmap every single time when you are playing a CTF. Pymap starts by scanning for open ports. Thereafter, Pymap feeds the open ports to Nmap to scan for service version, run vuln script, etc. This makes Pymap **faster** than the typical way of running Nmap. 

Pymap also provide:
- Ip sweeping, 
- SMB scanning
- NFS scan
- using Nmap scripts

**PS**: you should learn how to use Nmap before using this tool

## UPDATED v 1.0
Pymap is using threading when performing a service scan. It reduces the time taken for service scans by more than 50% (Upon scanning a target with more than 5 open ports). I tested by scanning `beep.htb` which has 12 open ports. Pymap last version would take 350 sec, **V 1.0 takes only 150 sec!!!**

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
- [x] improve speed (using thread?)
- [x] add -sC
- [x] remove `Service detection performed. Please report any incorrect results at https://nmap.org/submit/Nmap done: 1 IP address (1 host up) scanned in 2.10 seconds Starting Nmap 7.80 ( https://nmap.org ) at 2020-11-02 15:10 EST Nmap scan report for 10.200.11.232 Host is up (0.046s latency).`
- [ ] script=smb-brute?
