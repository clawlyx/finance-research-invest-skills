# Finance Skills Repository

A curated collection of OpenClaw skills for financial analysis, earnings deep dives, and market signal generation.

## Skills

- `stock/earnings-deepdive` - SEC EDGAR-powered earnings analysis for US equities
- *(more coming soon)*

## Getting Started

Each skill lives in its own subdirectory under `skills/` and can be loaded directly into OpenClaw or Claude.

## Contributing

Skills follow the OpenClaw Skill spec:
- `SKILL.md` - description and interface
- `index.ts` - core logic
- `tests/` - sample inputs and outputs

## License

MIT


## Sample Reports

- `examples/reports/AAPL-earnings-sample.md`
- `examples/reports/NVDA-earnings-sample.md`
- `examples/reports/CRCL-earnings-sample.md`
- `examples/reports/HOOD-earnings-sample.md`

Reproduce pattern:
1. Resolve latest filing via SEC submissions endpoint
2. Extract core metrics and management guidance
3. Render short summary + 3 risk highlights


## Quick Run

Generate 4 sample reports:

```bash
python3 scripts/generate_sample_reports.py
```

Output path: `examples/generated/`
