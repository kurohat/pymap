import subprocess, argparse, sys

banner = """                                                    
@@@@@@@   @@@ @@@  @@@@@@@@@@    @@@@@@   @@@@@@@  
@@@@@@@@  @@@ @@@  @@@@@@@@@@@  @@@@@@@@  @@@@@@@@  
@@!  @@@  @@! !@@  @@! @@! @@!  @@!  @@@  @@!  @@@  
!@!  @!@  !@! @!!  !@! !@! !@!  !@!  @!@  !@!  @!@  
@!@@!@!    !@!@!   @!! !!@ @!@  @!@!@!@!  @!@@!@!   
!!@!!!      @!!!   !@!   ! !@!  !!!@!!!!  !!@!!!    
!!:         !!:    !!:     !!:  !!:  !!!  !!:       
:!:         :!:    :!:     :!:  :!:  !:!  :!:       
 ::          ::    :::     ::   ::   :::   ::       
 :           :      :      :     :   : :   :        
Author: kuroHat
Github: https://github.com/gu2rks\n
"""
print(banner)

def parse():
    parser = argparse.ArgumentParser(
        description="pymap = python3 + nmap. Im so fucking tried of copy+paste port number")
    parser.add_argument('-t', '--target', type=str,
                        required=True, help='Target ip or network')
    parser.add_argument('-s', '--script', type=str,
                        help="[Optional] Name of script")
    parser.add_argument('-A', '--all', action="store_true",
                        help="[Optional] scann all ports, only scan top 10000 ports if this is not given")
    parser.add_argument('-smb', '--samba', action="store_true",
                        help="[Optional] nmap smb script at port 445")
    parser.add_argument('-nfs', '--nfs', action="store_true",
                        help="[Optional] nmap nsf script at port 111")
    parser.add_argument('-pS', '--sweep', action="store_true",
                        help="[Optional] prefrom host discovery aka ping sweep")
    return parser.parse_args()

def ping_sweep():
    print('sweeping on network: %s \nLooking for alive hosts...' %(target))
    output = subprocess.getoutput('sudo nmap %s -sn | grep for' % (target))
    print(output)

args = parse()
target = args.target
port = None
script = None

if args.sweep is True:
    ping_sweep()
    sys.exit(0)

if args.samba or args.nfs is True: #samba or nfs scan
    if args.samba is True:
        output = subprocess.getoutput('sudo nmap %s -Pn -p 445 --script=smb-enum-shares.nse,smb-enum-users.nse -T5' % (target))
    else:
        output = subprocess.getoutput('sudo nmap %s -Pn -p 111 --script=nfs-ls,nfs-statfs,nfs-showmount -T5' % (target))
    print(output)
    sys.exit(0)

else: 
    if args.all:
        port = '-p-'
    if args.script:
        script = args.script

    print('port scanning...')
    if port is None:
        output = subprocess.getoutput('sudo nmap %s -T4 -Pn | grep "/" | grep -v "https://nmap.org"' % (target))
    else:
        output = subprocess.getoutput('sudo nmap %s %s -T4 -Pn | grep "/" | grep -v "https://nmap.org"' % (target, port))
    
    print(output) # print open port
    
    port = ''
    for line in str(output).splitlines(): # parse ports
        port = port+line.split('/')[0]+','

    print('Enumerating open ports...')
    if script is None:
        output = subprocess.getoutput('sudo nmap %s -p%s -Pn -A -O -T5' % (target, port))
    else:
        output = subprocess.getoutput('sudo nmap %s -p%s -A -O -Pn -T5 --script %s' % (target, port, script))

    print(output) # print result