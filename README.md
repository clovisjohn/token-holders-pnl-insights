# Token Holders' PNL Insights

Analyze and visualize token holders' PNL and balances for a given Uniswap-like pair address. Supports CSV export and interactive GUI for easy review and analysis.

## Features

- Retrieve token holders' PNL and balances
- Interactive GUI with sortable table view
- CSV export option for further data analysis

## Installation

1. Clone the repository:
```bash
git clone https://github.com/clovisjohn/token-holders-pnl-insights.git
```
2. Install dependencies:
```bash
cd token-holders-pnl-insights
pip install -r requirements.txt
```

## Usage

1. Run the program:
```bash
python main.py
```

2. Enter the pair address and load a list of holder addresses from a text file (one address per line).

3. (Optional) Check the "Output CSV" option if you want to generate a CSV file with the results.

4. Click the "Start" button to retrieve and display token information.

## Important
As of now, the program only works with Camelot AMM

