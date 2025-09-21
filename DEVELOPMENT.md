# Development Guidelines - Ages of Mankind

## Terminology Standards

### Government Types
- **Use**: `band_clan` (ID and references)
- **Display Name**: "Band Clan"
- **Description**: Small nomadic groups organized around kinship ties

### Consistency Rules
1. All JSON keys should use `band_clan` (lowercase with underscore)
2. Display names should use "Band Clan" (title case with space)
3. Descriptions should refer to "Band Clan societies" or "Band Clans"
4. Never use the deprecated term (formerly used: t-r-i-b-a-l underscore c-l-a-n) - always use `band_clan` instead

### File Naming Conventions
- Data files: `snake_case.json`
- Scripts: `snake_case.py`
- Documentation: `kebab-case.md`

### Validation
Run the consistency validation script before committing changes:
```bash
python scripts/validate_consistency.py
```

This ensures all terminology follows the established standards and prevents introduction of the deprecated term that was previously used.

## Government System Design

### Band Clan Characteristics
- **Population Range**: 10-150 individuals
- **Leadership**: Elective based on capability
- **Social Structure**: Kinship-based organization
- **Economic Model**: Hunter-gatherer subsistence
- **Diplomatic Capacity**: Limited (3 relations max)

### Technology Integration
Band Clans are unlocked by the `hunter_gatherer_basics` technology and enhanced by `tribal_cooperation` (which should be renamed to `band_cooperation` in future updates).

## Contributing
When adding new content that references early human social organization:
1. Always use `band_clan` terminology
2. Run validation scripts before submitting
3. Update this guide if new patterns emerge
4. Maintain historical accuracy in descriptions