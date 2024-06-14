# -*- coding: utf-8 -*-
"""\

Author:  Peter Liske (for Helix CXM)
https://helixcxm.com

"""

import argparse
import csv
# import whois


def get_domain(s):
    tmp = s["Email"].split('@')
    domain = tmp[1]
    local_part = tmp[0]
    return domain

def read_csv(fp):
    domain_dict = {}
    try:
        file = open(fp, mode ='r')    
        csvFile = csv.DictReader(file)
        for line in csvFile:
            domain = get_domain(line)
        #             # check_domain_end(domain)
        # if '+' in local_part:
        #     print("+ ", local_part) 
        # if  not local_part.isascii():
        #     print("-->", domain)
            if domain in domain_dict:
                domain_dict[domain] = domain_dict[domain] + 1
            else:
                domain_dict[domain] = 1

        domain_dict = dict(sorted(domain_dict.items(), key=lambda item: item[1], reverse=True))
        return domain_dict
    except OSError as e:
        print(f"\nError: {e.strerror}:\t'{fp}'\n" )
        return None


def main():
    parser = argparse.ArgumentParser(prog='analyze')
    parser.add_argument('filepath',  help='path to email-address file')
    args = parser.parse_args()
    # print(args.filepath)
    domain_dict = read_csv(args.filepath)
    for key in domain_dict.keys():
        print(key, domain_dict[key])
        # w = whois.whois(key) 
        # print(w)

version_info = (1, 0, 1)
__version__ = ".".join(map(str, version_info))

if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
   main()