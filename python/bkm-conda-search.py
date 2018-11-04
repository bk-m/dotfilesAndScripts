#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://api.anaconda.org/docs

curl -X GET --header 'Accept: application/json' 'https://api.anaconda.org/search/?name={}'
"""

import argparse
import platform
import requests

arch = platform.system()
arch_map = {'Windows': 'win-64',
            'Linux': 'linux-64'}

def query_conda_api_and_print_result(package_name):
    print('*** Searching for {} {} packages.'.format(package_name, arch_map.get(arch)))    
    tmp = "https://api.anaconda.org/search/?name={}"
    r = requests.get(tmp.format(package_name))

    for entry in r.json():
        if arch_map.get(arch) in entry['conda_platforms'] and entry['public'] is True:
            print('* ', end='') if entry['owner'] == 'conda-forge' else print('  ',end='')
            py_versions = sorted({ver[:4] for ver in entry['builds']})
            print(entry['owner'].ljust(22), entry['latest_version'].ljust(7), entry['html_url'].ljust(52), py_versions)

def main():
    # TODO 2018-11-04 add a -e flag (exact) to set wether to search anything containing the search term or only exact matches    
    parser = argparse.ArgumentParser(description='Search anaconda.org for a given package name.')    
    parser.add_argument('package_name', type=str, metavar='PACKAGENAME', help='Name of the package to search for.')
    args = parser.parse_args()
    query_conda_api_and_print_result(args.package_name)

if __name__ == '__main__':
    main()