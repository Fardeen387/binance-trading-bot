# Binance Futures Trading Bot — Python Developer Intern Assignment

A modular, CLI-based trading bot for the Binance Futures Testnet (USDT-M). Supports `MARKET` and `LIMIT` order types with robust input validation and structured logging.

---

## Project Structure

```
trading_bot/
├── bot/
│   ├── cli.py             # CLI entry point via argparse
│   ├── orders.py          # Order placement orchestration
│   ├── client.py          # Binance API wrapper (+ MockBinanceClient)
│   ├── validators.py      # Pre-flight input validation
│   └── logging_config.py  # Centralized logging setup
├── logs/
│   └── app.log            # Sample log output (market, limit, validation failure)
├── .env.example
├── requirements.txt
└── README.md
```

---

## Setup & Installation

**1. Clone the repository**
```bash
git clone <your-repo-url>
cd trading_bot
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Configure environment variables**

Copy the example file and add your credentials:
```bash
cp .env.example .env
```

`.env` format:
```
BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_api_secret
```

> **Note:** See the [Mock Client](#mock-client) section below if you don't have Binance Testnet credentials.

---

## Usage

The bot is run as a module to ensure clean internal imports.

**Place a MARKET order**
```bash
python -m bot.cli --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

**Place a LIMIT order**
```bash
python -m bot.cli --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.002 --price 68500
```

**Validation error — missing price on LIMIT order**
```bash
python -m bot.cli --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001
# Error: --price is required for LIMIT orders
```

---

## Design Decisions

### Mock Client

Due to regional KYC restrictions (no PAN card) preventing Binance Testnet API key generation, a `MockBinanceClient` is included as a drop-in replacement for the live client.

The mock accurately mirrors the Binance Futures API response structure, ensuring that the application's validation, order logic, and logging layers behave identically to a live integration. This allows full end-to-end demonstration without requiring real credentials.

To switch to the live client once credentials are available, update the client instantiation in `orders.py` — no other changes are needed.

### Input Validation

Validation runs before any API call is attempted:
- `quantity` and `price` must be positive numbers
- `price` is required for `LIMIT` orders and rejected for `MARKET` orders

### Logging

All activity is logged to both console and `logs/app.log`, including:
- Outgoing order parameters
- API responses (real or mock)
- Validation errors with descriptive messages

---

## Deliverables

- [x] Full source code with modular architecture
- [x] `requirements.txt`
- [x] `logs/app.log` — sample output covering MARKET order, LIMIT order, and validation failure

---

**Author:** Fardeen Khan  
**Role:** Python Developer Intern Applicant — Primetrade.ai
