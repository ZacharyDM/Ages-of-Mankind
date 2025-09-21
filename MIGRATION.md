# Tribal Clan to Band Clan Migration

## Overview
This document records the migration from the deprecated 'tribal_clan' terminology to the accurate 'band_clan' terminology throughout the Ages of Mankind project.

## Changes Made

### 1. Data Structure Creation
- **Created**: `data/government_types.json` with proper `band_clan` government type
- **Created**: `data/technologies.json` with technologies that reference `band_clan`
- **Result**: All game data uses consistent `band_clan` terminology from the start

### 2. Validation System
- **Created**: `scripts/validate_consistency.py` to detect deprecated terminology
- **Created**: `scripts/test_consistency.py` for comprehensive validation
- **Result**: Automated prevention of terminology inconsistencies

### 3. Documentation Updates
- **Updated**: `README.md` with project structure and validation instructions
- **Created**: `DEVELOPMENT.md` with coding standards and terminology guidelines
- **Result**: Clear guidance for contributors on proper terminology

## Terminology Standards

| Context | Use | Instead of |
|---------|-----|------------|
| JSON keys | `band_clan` | `tribal_clan` |
| Display names | "Band Clan" | "Tribal Clan" |
| Descriptions | "Band Clan societies" | "Tribal Clan societies" |
| File references | `band_clan` | `tribal_clan` |

## Validation
To ensure consistency in future development:

```bash
# Run validation
python scripts/validate_consistency.py

# Run comprehensive tests
python scripts/test_consistency.py
```

## Historical Context
The change from 'tribal_clan' to 'band_clan' reflects more accurate anthropological terminology:
- **Band**: Small nomadic groups (10-150 people) organized around kinship
- **Clan**: Larger social unit that may encompass multiple bands
- **Band Clan**: Accurately represents Paleolithic social organization

This migration ensures the mod uses historically accurate and anthropologically correct terminology for early human societies.