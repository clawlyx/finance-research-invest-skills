#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime

TICKERS = {
    'AAPL': 'Revenue remained resilient with services mix improving; watch hardware re-acceleration.',
    'NVDA': 'AI infra demand remains strong; guidance sensitivity and policy/export risk remain key.',
    'CRCL': 'Stablecoin infra growth is solid but rate/regulatory sensitivity remains a core driver.',
    'HOOD': 'Retail activity improved; durability depends on retention and monetization mix quality.'
}

outdir = Path('examples/generated')
outdir.mkdir(parents=True, exist_ok=True)
ts = datetime.now().strftime('%Y%m%d-%H%M%S')
for t,summary in TICKERS.items():
    p = outdir / f'{t}-report-{ts}.md'
    p.write_text(
f'''Ticker: {t}
GeneratedAt: {ts}
Summary: {summary}
Risk Highlights:
1) Macro/regulatory shift
2) Concentration/cycle risk
3) Execution and guidance miss risk
''')
print('generated', len(TICKERS), 'reports', 'timestamp', ts)
