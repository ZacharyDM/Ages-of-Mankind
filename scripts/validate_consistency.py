#!/usr/bin/env python3
"""
Validation script to ensure consistent terminology throughout the Ages of Mankind mod.
This script checks for any references to 'tribal_clan' and ensures all references use 'band_clan' instead.
"""

import os
import json
import re
import sys
from pathlib import Path

def find_files_with_pattern(directory, patterns, extensions):
    """Find all files with specified extensions that contain any of the given patterns."""
    found_issues = []
    
    for root, dirs, files in os.walk(directory):
        # Skip .git directory
        if '.git' in dirs:
            dirs.remove('.git')
            
        for file in files:
            if any(file.endswith(ext) for ext in extensions):
                file_path = os.path.join(root, file)
                
                # Skip validation/test scripts and migration documentation
                if (file_path.endswith('validate_consistency.py') or 
                    file_path.endswith('test_consistency.py') or
                    file_path.endswith('MIGRATION.md')):
                    continue
                    
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        
                    for pattern in patterns:
                        if re.search(pattern, content, re.IGNORECASE):
                            found_issues.append({
                                'file': file_path,
                                'pattern': pattern,
                                'line_numbers': [i+1 for i, line in enumerate(content.split('\n')) 
                                               if re.search(pattern, line, re.IGNORECASE)]
                            })
                except (UnicodeDecodeError, IOError):
                    print(f"Warning: Could not read file {file_path}")
    
    return found_issues

def validate_json_files(directory):
    """Validate JSON files for correct band_clan references."""
    json_issues = []
    
    for json_file in Path(directory).rglob('*.json'):
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Check for tribal_clan keys or values
            json_str = json.dumps(data, indent=2)
            if 'tribal_clan' in json_str.lower():
                json_issues.append({
                    'file': str(json_file),
                    'issue': 'Contains tribal_clan references'
                })
                
        except (json.JSONDecodeError, IOError):
            print(f"Warning: Could not parse JSON file {json_file}")
    
    return json_issues

def main():
    """Main validation function."""
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    
    print("Ages of Mankind - Consistency Validation")
    print("=" * 50)
    print(f"Scanning directory: {project_root}")
    
    # Patterns to look for (we want to find 'tribal_clan' usage to flag it)
    problematic_patterns = [
        r'\btribal_clan\b',
        r'\bTribal[_\s]Clan\b',
        r'\bTRIBAL[_\s]CLAN\b'
    ]
    
    # File extensions to check
    extensions = ['.json', '.py', '.js', '.ts', '.md', '.txt', '.yml', '.yaml']
    
    # Find problematic references
    issues = find_files_with_pattern(project_root, problematic_patterns, extensions)
    json_issues = validate_json_files(project_root)
    
    # Report results
    if issues or json_issues:
        print("\n❌ VALIDATION FAILED")
        print("Found inconsistent terminology:")
        
        for issue in issues:
            print(f"\n📄 File: {issue['file']}")
            print(f"   Pattern: {issue['pattern']}")
            print(f"   Lines: {issue['line_numbers']}")
        
        for issue in json_issues:
            print(f"\n📄 File: {issue['file']}")
            print(f"   Issue: {issue['issue']}")
        
        print("\n💡 RECOMMENDATION:")
        print("Please replace all 'tribal_clan' references with 'band_clan' for consistency.")
        return 1
    else:
        print("\n✅ VALIDATION PASSED")
        print("All terminology is consistent - using 'band_clan' correctly.")
        return 0

if __name__ == "__main__":
    sys.exit(main())