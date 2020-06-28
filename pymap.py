import subprocess, argparse

intro = """created by gu2rks/kurohat \nfind me here https://github.com/gu2rks
"""
print(intro)

def parse():
    parser = argparse.ArgumentParser(
        description="pymap = python3 + nmap. Im so fucking tried of copy+paste port number")
    parser.add_argument('-t', '--target', type=str,
                        required=True, help='target ip')
    parser.add_argument('-s', '--script', type=str,
                        help="[Optional] Name of script")
    parser.add_argument('-all', '--all', action="store_true",
                        help="[Optional]scann all ports, only scan top 10000 ports if this is not given")
    return parser.parse_args()

args = parse()
target = args.target
port = None
script = None

if args.all:
    port = '-p-'
if args.script:
    script = args.script

print('port scanning...')
if port is None:
    output = subprocess.getoutput('nmap %s -T4| grep "/" | grep -v "https://nmap.org"' % (target))
else:
    out = subprocess.getoutput('nmap %s %s -T4| grep "/" | grep -v "https://nmap.org"' % (target, port))
print(output)
port = ''
for line in str(output).splitlines():
    port = port+line.split('/')[0]+','

print('Enumerating open ports...')
if script is None:
    output = subprocess.getoutput('nmap %s -p%s -A -O -T4' % (target, port))
else:
    output = subprocess.getoutput('nmap %s -p%s -A -O -T4 --script %s' % (target, port, script))

print(output)
