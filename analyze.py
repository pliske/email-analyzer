# -*- coding: utf-8 -*-
"""\

Author:  Peter Liske (for Helix CXM)
https://helixcxm.com

"""

import argparse
import csv
from tld import get_tld, get_fld
# import whois



def get_domain(s):
   
    domain = {}
    tmp = s["Email"].split('@')
    user_part = tmp[0].lower()
    domain_string = tmp[1].lower()
    # tmp = domain_string.split('.')
    try:
        # res = get_fld(tmp, fix_protocol=True)
        res = get_tld(domain_string, as_object=True, fix_protocol=True)
        domain["domain"] = res.domain
        domain["tld"] = res.tld 
        domain["fld"] = res.fld
        return domain
    except Exception as e:
        print(domain_string, "---->",e)
        domain["domain"] = domain_string
        domain["tld"] = ""
        domain["Err"] = True
    # if len(dtmp) == 2:
    #     domain['name'] = dtmp[0]
    #     domain['tld'] = dtmp[1]
    # elif len(dtmp) == 3:
    #     if dtmp[2] in country_codes:
    #         domain['name'] = dtmp[0]
    #         domain['tld'] = dtmp[1]
    #         domain['country'] = dtmp[2]
    #         print ('3 Country', domain['name'],   domain['tld'], domain['country'])
    #     else:
    #         domain['name'] = dtmp[0]+'.'+dtmp[1]
    #         domain['tld'] = dtmp[2]
    #         print ('3 Funky', domain['name'],   domain['tld'])
    # else:
    #     print ('funky', len(dtmp), full)

    return domain 

'''
domains segmented by:


'''

def read_csv(fp):
    domain_dict = {}
    try:
        file = open(fp, mode ='r')    
        csvFile = csv.DictReader(file)
        for line in csvFile:
            domain = get_domain(line)
            name = domain["domain"]
            tld = domain["tld"]
            if name in domain_dict:
                domain_dict[name]["count"] = domain_dict[name]["count"] + 1
                domain_dict[name]["tld"].add(tld)
            else:
                domain_dict[name] = {"count": 1, "tld": set([tld])}

        domain_dict = dict(sorted(domain_dict.items(), key=lambda d: d[1]["count"], reverse=True))
        return domain_dict
    except OSError as e:
        print(f"\nError: {e.strerror}:\t'{fp}'\n" )
        return None


def main():
    # company_domain = read_csv
    # priority_companies
    # free_domains

    parser = argparse.ArgumentParser(prog='analyze')
    parser.add_argument('filepath',  help='path to email-address file')
    args = parser.parse_args()
    # print(args.filepath)
    domain_dict = read_csv(args.filepath)
    
    for key in domain_dict.keys():
        if len(domain_dict[key]["tld"]) > 1:
            print(key,  domain_dict[key]["count"], domain_dict[key]["tld"] )
        # w = whois.whois(key) 
        # print(w)

version_info = (1, 0, 1)
__version__ = ".".join(map(str, version_info))

if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
   main()