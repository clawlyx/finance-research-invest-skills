#!/usr/bin/env python3
"""
Simplified PoC: Fetch latest 10-K accession number for AAPL from SEC EDGAR.
"""

import os
import json
import requests

SEC_USER_AGENT = os.getenv('SEC_USER_AGENT', 'FinanceSkills/1.0')
CIK = "0000320193"
URL = f"https://data.sec.gov/submissions/CIK{CIK}.json"
HEADERS = {'User-Agent': SEC_USER_AGENT}

def main():
    try:
        resp = requests.get(URL, headers=HEADERS, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        filings = data.get('filings', {}).get('recent', {})
        if not filings:
            print(json.dumps({"error": "No filings data found"}))
            return 1
        ft = filings.get('formType', [])
        idx = next((i for i, f in enumerate(ft) if f == "10-K"), -1)
        if idx == -1:
            print(json.dumps({"error": "No 10-K found"}))
            return 1
        result = {
            "ticker": "AAPL",
            "cik": CIK,
            "latest_10k_accession": filings['accessionNumber'][idx],
            "filing_date": filings['filingDate'][idx]
        }
        print(json.dumps(result))
        return 0
    except Exception as e:
        print(json.dumps({"error": str(e)}))
        return 1

if __name__ == '__main__':
    exit(main())
