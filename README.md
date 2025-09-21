# Ages-of-Mankind
A grand mod that encompasses the human journey from the Paleolithic era all the way to the Age of Revolutions.

## Overview
This mod focuses on historical accuracy and authentic terminology. Early human societies are represented as **Band Clans** - small nomadic groups organized around kinship ties, reflecting the actual anthropological understanding of Paleolithic social organization.

## Project Structure
```
├── data/                 # Game data files (JSON)
│   ├── government_types.json
│   └── technologies.json
├── scripts/              # Development and validation tools
│   └── validate_consistency.py
├── DEVELOPMENT.md        # Development guidelines
└── README.md            # This file
```

## Development
See [DEVELOPMENT.md](DEVELOPMENT.md) for contribution guidelines and terminology standards.

## Validation
To ensure consistency, run:
```bash
python scripts/validate_consistency.py
```
