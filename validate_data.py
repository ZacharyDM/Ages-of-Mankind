#!/usr/bin/env python3
"""
Validation script for Ages of Mankind game data files.
Checks JSON syntax and basic data integrity.
"""

import json
import os
import sys

def validate_json_file(filepath):
    """Validate that a file contains valid JSON."""
    try:
        with open(filepath, 'r') as f:
            json.load(f)
        print(f"✓ {filepath} - Valid JSON")
        return True
    except json.JSONDecodeError as e:
        print(f"✗ {filepath} - Invalid JSON: {e}")
        return False
    except FileNotFoundError:
        print(f"✗ {filepath} - File not found")
        return False

def validate_technology_prerequisites(tech_data):
    """Check that technology prerequisites reference valid technologies."""
    technologies = tech_data.get('technologies', {})
    all_tech_ids = set(technologies.keys())
    
    invalid_prereqs = []
    for tech_id, tech in technologies.items():
        prerequisites = tech.get('prerequisites', [])
        for prereq in prerequisites:
            if prereq not in all_tech_ids:
                invalid_prereqs.append(f"{tech_id} -> {prereq}")
    
    if invalid_prereqs:
        print("✗ Invalid technology prerequisites found:")
        for invalid in invalid_prereqs:
            print(f"  - {invalid}")
        return False
    else:
        print("✓ All technology prerequisites are valid")
        return True

def main():
    """Run all validation checks."""
    print("=== Ages of Mankind Data Validation ===")
    
    # Define files to check
    json_files = [
        'common/technologies/technology_types.json',
        'common/governments/government_types.json', 
        'common/technologies/paleolithic_technologies.json'
    ]
    
    all_valid = True
    
    # Validate JSON syntax
    print("\n1. JSON Syntax Validation:")
    for filepath in json_files:
        if not validate_json_file(filepath):
            all_valid = False
    
    # Validate technology prerequisites
    print("\n2. Technology Prerequisites Validation:")
    try:
        with open('common/technologies/paleolithic_technologies.json', 'r') as f:
            tech_data = json.load(f)
        if not validate_technology_prerequisites(tech_data):
            all_valid = False
    except Exception as e:
        print(f"✗ Could not validate technology prerequisites: {e}")
        all_valid = False
    
    # Summary
    print(f"\n=== Validation {'PASSED' if all_valid else 'FAILED'} ===")
    return 0 if all_valid else 1

if __name__ == '__main__':
    sys.exit(main())