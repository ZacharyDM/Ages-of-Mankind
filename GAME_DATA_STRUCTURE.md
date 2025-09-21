# Ages of Mankind - Game Data Structure

This document explains the file structure and data format for the Ages of Mankind mod.

## Directory Structure

```
common/
├── technologies/
│   ├── technology_types.json    # Defines the main technology categories
│   └── paleolithic_technologies.json  # Specific technologies for Paleolithic era
└── governments/
    └── government_types.json    # Government system definitions
```

## Technology System

### Technology Types (`technology_types.json`)
Defines the five main categories of technological advancement:
- **Military**: Warfare, weapons, and military organization
- **Civic**: Governance, law, and social organization  
- **Economic**: Trade, agriculture, and resource management
- **Cultural**: Arts, religion, and cultural practices
- **Scientific**: Knowledge, tools, and understanding of the world

### Technology Definitions
Each technology includes:
- **Basic Info**: Name, description, type, era, tier
- **Research**: Cost and time requirements
- **Prerequisites**: Required technologies
- **Effects**: Gameplay modifiers and bonuses
- **Unlocks**: New buildings, units, decisions, or mechanics

## Government System

### Government Types (`government_types.json`)
Currently defines the starting government: **Tribal Clan**

Features:
- Kinship-based leadership structure
- Council of elders decision-making
- Limited population capacity (500)
- Basic warfare capabilities
- No formal diplomacy

Government attributes include:
- **Modifiers**: Gameplay effect bonuses/penalties
- **Mechanics**: How the government functions
- **Requirements**: What's needed to adopt this government
- **Visual**: Color scheme and icon reference

## Era Progression

The mod is designed to progress through historical eras:
1. **Paleolithic** (Current): Stone tools, fire, basic language
2. **Neolithic** (Planned): Agriculture, settlements, pottery
3. **Bronze Age** (Planned): Metallurgy, writing, kingdoms
4. **Classical** (Planned): Empires, philosophy, trade networks
5. **Medieval** (Planned): Feudalism, religions, advanced warfare
6. **Renaissance** (Planned): Science, exploration, nation-states
7. **Age of Revolutions** (Planned): Democracy, industrialization

## File Format

All data files use JSON format for easy parsing and modification. The structure follows a hierarchical approach where each game element has a unique identifier and comprehensive attribute definitions.