#!/usr/bin/python3
import sys
import argparse
from .core.xss import XSS
from .core.ssti import SSTI
from .core.reflect import Reflect


p = argparse.ArgumentParser()
p.add_argument('-a', '--all', action='store_true', help='Enable all attacks except reflect')
p.add_argument('-r', '--reflect', action='store_true', help='Enable reflect attack')
p.add_argument('--xss', action='store_true', help='Enable XSS attack')
p.add_argument('--ssti', action='store_true', help='Enable SSTI attack')
p.add_argument('-x', '--proxy', help='Specify your proxy, like http://127.0.0.1:8080')
p.add_argument('-t', '--threads', type=int, default=64, help='Max Concurrency')
args = p.parse_args()

x_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
x_proxies = {
    'http': args.proxy,
    'https': args.proxy
}


def main():
    if sys.stdin.isatty():
        sys.exit(0)
    urls = []
    for line in sys.stdin.readlines():
        url = line.strip('\n')
        if '?' not in url:
            continue
        urls.append(url)

    if args.all or args.xss:
        i = XSS(urls, x_headers, x_proxies, max_threads=args.threads)
        i.attack()
    if args.all or args.ssti:
        i = SSTI(urls, x_headers, x_proxies, max_threads=args.threads)
        i.attack()
    if args.reflect:
        i = Reflect(urls, x_headers, x_proxies, max_threads=args.threads)
        i.attack()


if __name__ == '__main__':
    main()
