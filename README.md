# AgriPath 🌾

![Python](https://img.shields.io/badge/python-3.12-blue)
[![CI](https://github.com/luismanfredi/agripath/actions/workflows/ci.yml/badge.svg?branch=main&event=push)](https://github.com/luismanfredi/agripath/actions/workflows/ci.yml)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-alpha-orange)

A system that tracks the journey of an agricultural product from its origin to the final consumer.

> ⚠️ **Alpha software.** AgriPath is in early development. Expect breaking changes, missing features, and an evolving architecture until a stable release is tagged.

## About

An agricultural product goes through multiple stages before reaching the end consumer. AgriPath enables every step of this journey to be accurately tracked, providing detailed records, timestamps, and descriptions throughout the supply chain.

Tracking begins at the point of production or harvest and continues through distributors, wholesalers, retailers, and other participants until the product reaches the consumer.

The project's goal is to increase transparency and traceability across the agricultural supply chain, giving every participant clear visibility into a product's journey while also helping consumers better understand how agricultural products reach their tables.

## How It Works

**AgriPath** is built around a **Product** and an **Event**.

**Product**: A Product represents an agricultural item being tracked throughout the supply chain. Each product has a unique identifier and a name, allowing it to be uniquely recognized and traced.

Additionally, every product maintains a collection of Events, which together form its complete lifecycle history.

**Event**: An Event represents a single stage in a product's journey. Each event contains:

- Description – A summary of the action performed (e.g., Harvested, Packaged, Shipped).
- Registered By – The individual or organization responsible for the action.
- Timestamp – The date and time when the event occurred.

One of the most important design decisions is that Events are immutable. Once created, an event cannot be modified or deleted. This reflects the nature of real-world traceability systems, where historical records should remain permanent and tamper-resistant, ensuring the integrity of the product's history.

## Features

- [X] Simple CLI menu
- [X] Register Product and Events
- [X] Display Product and Event history
- [X] PostgreSQL persistence layer via SQLAlchemy ORM

## Demo

![Agripath Demo](assets/demo.gif)

## Tech Stack


| Stack | Usage                  |
|------------|-----------------------|
| Python                  | Backend language                         |
| PostgreSQL              | Relational database                      |
| SQLAlchemy              | ORM                                      |
| psycopg                 | PostgreSQL database driver               |
| Docker / Docker Compose | Containerized local database environment |

## Project Structure

```
agripath/
├── assets/            # README images
├── src/agripath/      # Core application code
├── tests/             # Tests
├── main.py            # Entry point
└── pyproject.toml
```

## Architecture

```mermaid
flowchart LR

    User --> CLI
    CLI --> Services
    Services --> SQLAlchemy
    SQLAlchemy --> psycopg
    psycopg --> PostgreSQL
```

## Getting Started

### Prerequisites

- Docker and Docker Compose
- Python 3.12+
- [uv](https://docs.astral.sh/uv/)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/luismanfredi/agripath.git
cd agripath
```
2. Copy the example environment file and adjust if needed
```bash
cp .env.example .env
```

3. (Optional) Create a virtual environment:

```bash
python -m venv .venv
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

4. Start the PostgreSQL container
```bash
docker compose up -d
```

5. Install dependencies

```bash
uv sync
```

6. Initialize the database schema
```bash
uv run python src/agripath/db/init_db.py
```

### Usage

Run the CLI:
```bash
uv run python main.py
```

## Roadmap

- [ ] REST API (FastAPI)
- [ ] Multi-actor authentication

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author
**Luís Antonio Manfredi Sodré**
- [GitHub](https://github.com/luismanfredi)
- [Email](mailto:luismanfredi920@gmail.com)
