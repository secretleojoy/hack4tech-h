#!/usr/bin/env python3
# coding=utf-8

"""
Example
"""

from garuda import Garuda


def garuda(domain):
    test = Garuda(target=domain)
    test.dns = True
    test.brute = True
    test.req = True
    test.takeover = True
    test.run()
    results = test.datas
    print(results)


if __name__ == '__main__':
    garuda('freebuf.com')
