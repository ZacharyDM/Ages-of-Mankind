#!/usr/bin/env python3
"""
Simple test to verify that the band_clan government type is properly defined
and that the validation system works as expected.
"""

import json
import os
import sys
from pathlib import Path

def test_government_types():
    """Test that government_types.json contains proper band_clan definition."""
    print("Testing government_types.json...")
    
    with open('data/government_types.json', 'r') as f:
        data = json.load(f)
    
    # Check that band_clan exists
    assert 'government_types' in data, "Missing government_types section"
    assert 'band_clan' in data['government_types'], "Missing band_clan government type"
    
    band_clan = data['government_types']['band_clan']
    
    # Verify required fields
    required_fields = ['id', 'name', 'description', 'category', 'tier']
    for field in required_fields:
        assert field in band_clan, f"Missing required field: {field}"
    
    # Verify correct values
    assert band_clan['id'] == 'band_clan', "Incorrect ID"
    assert band_clan['name'] == 'Band Clan', "Incorrect display name"
    assert 'band' in band_clan['description'].lower(), "Description should mention 'band'"
    
    print("✅ government_types.json test passed")

def test_technologies():
    """Test that technologies.json references band_clan correctly."""
    print("Testing technologies.json...")
    
    with open('data/technologies.json', 'r') as f:
        data = json.load(f)
    
    # Check that technologies reference band_clan
    technologies = data['technologies']
    
    # Verify hunter_gatherer_basics unlocks band_clan
    hunter_basic = technologies['hunter_gatherer_basics']
    assert 'band_clan' in hunter_basic['unlocks']['governments'], \
           "hunter_gatherer_basics should unlock band_clan"
    
    print("✅ technologies.json test passed")

def test_no_deprecated_references():
    """Test that no files contain deprecated terminology."""
    print("Testing for deprecated terminology...")
    
    # Run the validation script
    result = os.system('python scripts/validate_consistency.py > /dev/null 2>&1')
    assert result == 0, "Validation script failed - found deprecated terminology"
    
    print("✅ No deprecated terminology found")

def main():
    """Run all tests."""
    print("Running Ages of Mankind consistency tests...")
    print("=" * 50)
    
    try:
        test_government_types()
        test_technologies()
        test_no_deprecated_references()
        
        print("\n🎉 ALL TESTS PASSED")
        print("The band_clan migration is complete and consistent!")
        return 0
    except AssertionError as e:
        print(f"\n❌ TEST FAILED: {e}")
        return 1
    except Exception as e:
        print(f"\n💥 UNEXPECTED ERROR: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())