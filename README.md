# DNA Analysis Project

This program analyzes DNA sequences to identify a matching profile based on Short Tandem Repeats (STRs).

## How to Use

1. **Files Needed**:
   - A CSV file with DNA profiles (e.g., `database.csv`).
   - A text file with a DNA sequence (e.g., `1.txt`).

2. **Run the Program**:
   Open your terminal and use the following command:
   ```bash
   python main.py database.csv test sequences/1.txt
## How It Works

- The program reads the database of DNA profiles.
- It reads the DNA sequence to analyze.
- It finds the longest matches of STRs in the sequence.
- It checks the database for a matching profile.
- If a match is found, it prints the name of the individual.
