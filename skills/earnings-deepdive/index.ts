/**
 * Earnings Deepdive Skill - Implementation
 * Fetches latest 10-K from SEC EDGAR and returns structured data.
 */

import axios from 'axios';

const SEC_USER_AGENT = process.env.SEC_USER_AGENT || 'FinanceSkills/1.0';

export const metadata = {
  name: "earnings-deepdive",
  version: "0.2.0",
  description: "US earnings deep-dive (SEC EDGAR integration, returns latest 10-K basic metadata)"
};

export async function run(input: { ticker: string; formType: string }) {
  const { ticker, formType } = input;
  // CIK mapping for demo (simplified)
  const cikMap: Record<string, string> = {
    AAPL: "0000320193",
    // Add more tickers as needed
  };
  const cik = cikMap[ticker.toUpperCase()];
  if (!cik) {
    return { error: `Unsupported ticker: ${ticker}` };
  }

  const url = `https://data.sec.gov/submissions/CIK${cik}.json`;
  try {
    const resp = await axios.get(url, {
      headers: { 'User-Agent': SEC_USER_AGENT },
      timeout: 10000
    });
    const data = resp.data;
    const filings = data.filings?.recent;
    if (!filings) {
      return { error: "No filings data found" };
    }

    const { formType: ft, filingDate, accessionNumber } = filings;
    const idx = ft.findIndex((f: string) => f === formType);
    if (idx === -1) {
      return { error: `No ${formType} found for ${ticker}` };
    }

    return {
      ticker: ticker.toUpperCase(),
      form_type: formType,
      filing_date: filingDate[idx],
      latest_10k_accession: accessionNumber[idx],
      cik: cik,
      source_url: url,
      // Placeholders for future parsing
      revenue: null,
      net_income: null,
      eps: null,
      cash_flow: null,
      summary: "Primary document parsing required to generate a summary",
      risk_highlights: []
    };
  } catch (err: any) {
    return { error: err.message };
  }
}
