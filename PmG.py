#!/usr/bin/env python3
# coded by : khaled nassar @knassar702
# Github : http://github.com/knassar702/pmg
import sys,re
red = '\u001b[31m'
end = '\u001b[0m'
black = '\u001b[30m'
green = '\u001b[32m'
yellow = '\u001b[33m'
blue = '\u001b[34m'
magenta = '\u001b[35m'
cyan = '\u001b[36m'
white = '\u001b[37m'
print(f"""

{red} , __
/|/  \             () |
{cyan} |___/ _  _  _     /\/|
 |    / |/ |/ |   /   |
{blue} |      |  |  |_//(__/
{end}
[{magenta}#{end}] Coded By : Khaled Nassar @knassar702
 """)
wordlist = [
        r'(url=|password=|link=|u=|username=|link_id=)',
        '/+CSCOU+', # CVE-2020-3452
        r'\.(sql|db|tar|backup|bak|zip|git|php)'
        ]

red = '\u001b[31m'
end = '\u001b[0m'
green = '\u001b[32m'

if __name__ == '__main__':
    for i in sys.stdin:
        i = i.rstrip()
        for word in wordlist:
            r = re.search(word,i)
            try:
                if r.group() != None:
                    I = i.replace(r.group(),f'{red}{r.group()}{end}')
                    print(f'[{green}+{end}] Found :> {I}')
            except:
                pass
