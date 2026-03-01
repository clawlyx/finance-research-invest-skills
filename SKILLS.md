# Skills Directory

## earnings-deepdive (stock)
Description: Fetches the latest 10-K/10-Q filing for a US stock ticker via SEC EDGAR, returns structured data and a summary.

Input:
- ticker (string)
- formType (10-K | 10-Q)

Output (JSON):
{
  "ticker": "AAPL",
  "form_type": "10-K",
  "filing_date": "2025-10-31",
  "latest_10k_accession": "0000320193-25-000079",
  "cik": "0000320193",
  "source_url": "https://data.sec.gov/submissions/CIK0000320193.json",
  "revenue": null,
  "net_income": null,
  "eps": null,
  "cash_flow": null,
  "summary": "Summary requires parsing primary document",
  "risk_highlights": []
}

Dependencies:
- SEC EDGAR public API (data.sec.gov)
- Claude (anthropic/claude-4-6-sonnet) for summarization (future)

Status: PoC in progress
