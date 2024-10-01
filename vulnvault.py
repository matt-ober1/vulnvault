#!/usr/bin/env python3

'''
    vulnvault - Search for Vulnerabilities using the VulDB API
    
    License: GPL-3.0    
    Required Dependencies: requests, argparse, json
    Optional Dependencies: None
'''

import requests
import argparse
import json

# Define arguments for the API script
parser = argparse.ArgumentParser(description="Search for vulnerabilities using the VulDB API.")
parser.add_argument('--service', dest='service', help='Specify the service to search for (e.g., OpenSSH).')
parser.add_argument('--version', dest='version', help='Specify the service version (e.g., 8.1).')
parser.add_argument('--search', dest='search', help='Search for vulnerabilities using a specific query string.')
parser.add_argument('--recent', dest='recent', default=5, type=int, help='Show the most recent entries (default: 5).')
parser.add_argument('--details', dest='details', default=0, type=int, help='Set details level: 0 (basic) or 1 (detailed).')
parser.add_argument('--id', dest='id', help='Request details for a specific vulnerability entry by VulDB Id.')
args = parser.parse_args()

# Add your personal VulDB API key here
personalApiKey = '139b345cdf055e9fd7172a793dc40ecd'

# Set HTTP Header
userAgent = 'VulDB API Python Search Script'
headers = {'User-Agent': userAgent, 'X-VulDB-ApiKey': personalApiKey}

# URL VulDB endpoint
url = 'https://vuldb.com/?api'

# Prepare the data for the API call based on the passed arguments
postData = {}

if args.id is not None:
    postData = {'id': args.id}
elif args.service and args.version:
    postData = {'search': f"{args.service} {args.version}"}
elif args.search is not None:
    postData = {'search': args.search}
else:
    postData = {'recent': args.recent}

if args.details is not None:
    postData['details'] = int(args.details)

# Get API response
response = requests.post(url, headers=headers, data=postData)

# Display result if everything went OK
if response.status_code == 200:
    responseJson = json.loads(response.content)
    
    # Output
    if responseJson['result']:
        for i in responseJson['result']:
            entry = i['entry']
            print(f"ID: {entry.get('id', 'N/A')}")
            print(f"Title: {entry.get('title', 'N/A')}")
            print('-' * 40)
    else:
        print("No results found.")
else:
    print(f"Error: Unable to fetch data (status code: {response.status_code})")

