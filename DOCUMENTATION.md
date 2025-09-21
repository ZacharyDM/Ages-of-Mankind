# Ages of Mankind - Crusader Kings 3 Mod Documentation

## Overview

Ages of Mankind is a total conversion mod for Crusader Kings 3 that takes players on humanity's journey from the Paleolithic era (Stone Age) all the way to the Age of Revolution. The mod fundamentally reimagines the CK3 experience to cover the entire span of human history, with each era featuring distinct gameplay mechanics, technologies, and cultural evolution.

## Key Features

### 1. Era System
The mod divides human history into distinct eras, each with unique characteristics:

- **Paleolithic Era (2.6M - 10,000 BCE)**: Hunter-gatherer bands, basic stone tools
- **Mesolithic Era (10,000 - 8,000 BCE)**: Transition period, early settlements  
- **Neolithic Era (8,000 - 3,300 BCE)**: Agricultural revolution, first chiefdoms
- **Chalcolithic Era (3,300 - 2,500 BCE)**: Copper Age, fortified settlements
- **Bronze Age (2,500 - 1,200 BCE)**: First true civilizations
- **Iron Age (1,200 - 500 CE)**: Classical civilizations
- **Early Medieval (500 - 1000 CE)**: Dark Ages, rise of feudalism
- **High Medieval (1000 - 1300 CE)**: Peak medieval period
- **Late Medieval (1300 - 1500 CE)**: Renaissance begins
- **Age of Revolution (1500 - 1800 CE)**: Final era, transition to EU4

### 2. Band Government
The starting government type represents small nomadic groups:
- **Landless**: Bands cannot hold traditional territories
- **Nomadic**: Constant movement in search of resources
- **Consensus-based**: Leadership through prowess and wisdom
- **Survival-focused**: All mechanics centered on basic survival

### 3. Technology Progression
Technologies are era-specific and unlock gradually:
- **Stone Tools**: Foundation of human technology
- **Fire Making**: Revolutionary survival advancement
- **Hunting Techniques**: Organized prey tracking and killing
- **Shelter Construction**: Protection from elements
- **Language Development**: Complex communication systems

### 4. Cultural Evolution
Dynamic cultural systems that evolve based on environment:
- **Geographic Adaptation**: Mountains, coasts, and deserts create specialization
- **Environmental Pressure**: Climate and terrain drive cultural innovation
- **Ethnic Divergence**: Populations split and develop unique characteristics
- **Technological Diffusion**: Innovations spread between cultures

### 5. Specialized Traits
Era-appropriate character traits:
- **Hunter**: Expert in tracking and killing prey
- **Gatherer**: Skilled at finding edible plants and resources
- **Fire Keeper**: Guardian of fire-making knowledge
- **Stone Shaper**: Master tool crafter
- **Storyteller**: Keeper of oral traditions
- **Tracker**: Navigation and pathfinding expert
- **Weather Wise**: Predictor of seasonal patterns

## Gameplay Mechanics

### Progression System
1. **Start as Band**: Begin with a small nomadic group
2. **Technological Development**: Research basic survival technologies
3. **Cultural Adaptation**: Adapt to local environment and conditions
4. **Era Advancement**: Meet requirements to progress to next historical period
5. **Government Evolution**: Gradually develop more complex political systems
6. **Territorial Control**: Eventually gain ability to settle and hold land

### Survival Elements
- **Resource Scarcity**: Constant need to find food and materials
- **Environmental Challenges**: Weather, terrain, and seasonal changes
- **Leadership Dynamics**: Prove worth through capability and wisdom
- **Technology Gates**: Certain abilities locked behind innovation requirements

### Cultural Development
- **Innovation Spread**: Technologies diffuse through cultural contact
- **Environmental Specialization**: Geographic conditions drive adaptation
- **Population Growth**: Successful bands grow and split into new groups
- **Ethnic Divergence**: Separated populations develop distinct characteristics

## File Structure

```
mod/ages_of_mankind/
├── common/
│   ├── governments/00_band_government.txt          # Band government definition
│   ├── laws/00_eras.txt                           # Historical era system
│   ├── innovations/01_paleolithic_innovations.txt  # Stone Age technologies
│   ├── cultures/01_paleolithic_cultures.txt       # Early human cultures
│   └── traits/01_paleolithic_traits.txt           # Survival-focused traits
├── events/
│   └── paleolithic_events.txt                     # Stone Age event chains
├── localization/english/
│   ├── ages_of_mankind_l_english.yml              # Core mod text
│   ├── traits_cultures_l_english.yml              # Traits and cultures
│   └── paleolithic_events_l_english.yml           # Event descriptions
└── descriptor.mod                                  # Mod metadata
```

## Design Philosophy

### Historical Accuracy
- Based on archaeological and anthropological evidence
- Represents realistic technological progression
- Reflects actual human migration and cultural development patterns

### Gameplay Balance  
- Maintains CK3's core engagement while adding new mechanics
- Provides meaningful choices at each technological level
- Creates clear progression goals without making early eras boring

### Scalability
- Modular design allows easy addition of new eras
- Technology trees can be expanded with additional innovations
- Cultural system supports unlimited ethnic divergence

### Educational Value
- Players learn about human technological and cultural development
- Showcases the challenges faced by early human societies
- Demonstrates how environment shapes cultural adaptation

## Future Development

### Planned Additions
1. **Advanced Technologies**: Agriculture, metallurgy, writing systems
2. **Complex Governments**: Chiefdoms, kingdoms, early states
3. **Trade Networks**: Resource exchange and cultural diffusion
4. **Population Mechanics**: Demographic growth and migration
5. **Environmental Systems**: Climate change and resource depletion
6. **Warfare Evolution**: From personal combat to organized armies
7. **Religious Development**: From animism to organized religions
8. **Art and Culture**: Symbolic expression and cultural identity

### Integration Possibilities
- **EU4 Converter**: Seamless transition to Europa Universalis IV
- **Map Extensions**: Accurate historical geography for each era
- **Music and Audio**: Era-appropriate soundscapes and music
- **Visual Overhauls**: Time-period accurate artwork and interfaces

## Installation and Usage

1. Place mod files in Crusader Kings 3 mod directory
2. Enable "Ages of Mankind" in launcher
3. Start new game - select Paleolithic start date
4. Begin as band leader and guide your people through history
5. Research technologies, adapt to environment, and advance through eras

## Modding Support

The mod is designed to be extensible:
- Clear file organization for easy modification
- Comprehensive localization for community translation
- Modular technology and culture systems
- Well-documented code with extensive comments

## Credits and Attribution

This mod represents a comprehensive reimagining of human history within the Crusader Kings 3 framework. It draws inspiration from archaeological research, anthropological studies, and historical documentation to create an authentic experience of humanity's journey from our earliest origins to the threshold of the modern world.