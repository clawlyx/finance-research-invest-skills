# Earnings Deepdive Skill

US earnings deep-dive skill. Input a ticker and form type, then output a structured analysis report.

## Inputs
- ticker (string)
- formType (10-K | 10-Q)

## Output (JSON)
{
  "ticker": "AAPL",
  "form_type": "10-K",
  "filing_date": "2025-10-31",
  "revenue": 394330000000,
  "net_income": 93659000000,
  "eps": 5.89,
  "cash_flow": 114010000000,
  "summary": "Summary within 150 words",
  "risk_highlights": ["Risk item 1", "Risk item 2"],
  "source_urls": ["https://..."]
}

## Data Source
SEC EDGAR: https://data.sec.gov/submissions/CIK{CIK}.json

## Model
Claude 4.6 Sonnet (anthropic/claude-4-6-sonnet)

## Notes
- Follow SEC rate limits (10 req/s)
- This report is not investment advice; research use only
- Risk highlights require human review
