import csv
import sys


def main():
    # Check for command-line usage
    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        return

    # Read database file into a variable
    with open(sys.argv[1]) as chosen_database:
        reader = csv.DictReader(chosen_database)
        database = list(reader)  # Convert to list of dictionaries
        STRs = reader.fieldnames[1:]  # Get STR names from the header

    # Read DNA sequence file into a variable
    with open(sys.argv[2], 'r') as sequence_file:
        sequence = sequence_file.read()

    # Find longest match of each STR in DNA sequence
    longest_matches = {STR: longest_match(sequence, STR) for STR in STRs}

    # Check database for matching profiles
    for person in database:
        match = True  # Assume it's a match unless proven otherwise

        for STR in STRs:
            if longest_matches[STR] != int(person[STR]):
                match = False  # If any STR does not match, set to False
                break  # No need to check further if one doesn't match

        if match:
            print(person['name'])  # Print the person's name (assuming the first column is 'name')
            return  # Exit after finding the first match

    print("No match")  # If no matches were found


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    for i in range(sequence_length):
        count = 0
        while True:
            start = i + count * subsequence_length
            end = start + subsequence_length

            if sequence[start:end] == subsequence:
                count += 1
            else:
                break

        longest_run = max(longest_run, count)

    return longest_run


main()
