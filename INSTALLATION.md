# Ages of Mankind - Installation and Testing Guide

## Installation Instructions

### For Players

1. **Download the mod**:
   - Clone or download this repository
   - Locate your Crusader Kings 3 mod directory:
     - Windows: `Documents/Paradox Interactive/Crusader Kings III/mod/`
     - Mac: `~/Documents/Paradox Interactive/Crusader Kings III/mod/`
     - Linux: `~/.local/share/Paradox Interactive/Crusader Kings III/mod/`

2. **Install the mod**:
   - Copy the `descriptor.mod` file to your mod directory
   - Copy the entire `mod/ages_of_mankind` folder to your mod directory
   - Your file structure should look like:
     ```
     mod/
     ├── descriptor.mod
     └── ages_of_mankind/
         ├── common/
         ├── events/
         ├── localization/
         └── ...
     ```

3. **Enable the mod**:
   - Launch Crusader Kings 3
   - Go to the launcher's "Mods" tab
   - Find "Ages of Mankind" and enable it
   - Click "Play" to start the game

### For Developers

1. **Development Setup**:
   - Clone this repository directly into your CK3 mod directory
   - Use symlinks to connect the repository to your mod folder for easier development
   - Install a text editor with syntax highlighting for CK3 script files

## Testing the Mod

### Basic Functionality Tests

1. **Mod Loading**:
   - Verify the mod appears in the launcher
   - Confirm no immediate error messages
   - Check that all localization displays correctly

2. **Government System**:
   - Start a new game with Paleolithic start date
   - Confirm "Band" government type is available and functional
   - Test landless mechanics work as intended

3. **Technology System**:
   - Verify innovations appear in the culture screen
   - Test that technology research progresses
   - Confirm prerequisite technologies are properly gated

4. **Traits and Characters**:
   - Check that Paleolithic traits appear on characters
   - Verify trait effects are applied correctly
   - Test trait interactions and compatibility

5. **Events System**:
   - Trigger discovery events (fire, stone tools, etc.)
   - Verify event options work as intended
   - Check that event outcomes apply correctly

### Advanced Testing

1. **Era Progression**:
   - Test advancement through technological eras
   - Verify era bonuses are applied
   - Check government evolution mechanics

2. **Cultural Development**:
   - Test cultural adaptation to different terrains
   - Verify ethnic divergence mechanics
   - Check cultural parameter effects

3. **Balance Testing**:
   - Assess difficulty of early survival
   - Check that progression feels rewarding
   - Verify no game-breaking exploits exist

## Known Issues and Limitations

### Current Version (v1.0)
- Only Paleolithic era fully implemented
- Limited to basic survival mechanics
- No advanced government transitions yet
- Map data not yet customized for early periods

### Planned Fixes
- Complete all historical eras
- Add more complex survival mechanics
- Implement full government evolution tree
- Create era-specific map variants

## Troubleshooting

### Common Issues

1. **Mod doesn't appear in launcher**:
   - Check file paths are correct
   - Verify descriptor.mod is in the right location
   - Restart the CK3 launcher

2. **Game crashes on startup**:
   - Disable other mods to test conflicts
   - Check the error.log file in your CK3 directory
   - Verify all mod files have correct syntax

3. **Localization missing**:
   - Check that .yml files are in the correct encoding (UTF-8)
   - Verify localization file names match expected format
   - Confirm all referenced keys have definitions

4. **Features not working**:
   - Check that required DLCs are installed
   - Verify game version compatibility
   - Test with a clean save file

### Debug Commands

For testing purposes, you can use these console commands:

```
# Add innovations to your culture
effect culture = { add_innovation = stone_tools }

# Add traits to your character  
add_trait hunter

# Add prestige for testing
add_prestige 1000

# Change government type
set_government band_government

# Trigger specific events
event ages_of_mankind.0001
```

## Performance Considerations

- The mod is designed to be lightweight and performant
- Early eras have simplified mechanics to reduce computational load
- File organization optimizes loading times
- Modular design allows selective feature loading

## Feedback and Bug Reports

When reporting issues, please include:
1. Your game version and installed DLCs
2. Complete mod list (other enabled mods)
3. Steps to reproduce the issue
4. Save file if possible
5. Error logs from the game directory

## Development Roadmap

### Short Term (v1.1)
- Complete Mesolithic and Neolithic eras
- Add agricultural mechanics
- Implement settlement founding

### Medium Term (v2.0)  
- Bronze and Iron Age content
- Complex trade systems
- Advanced government types

### Long Term (v3.0+)
- Medieval and Renaissance eras
- EU4 integration support
- Complete visual overhaul

---

This guide will be updated as the mod evolves. For the latest information, check the repository README and documentation files.