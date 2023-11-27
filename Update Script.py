import csv
import random

# Function to read lines from a file and remove empty lines
def read_lines_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines if line.strip()]  # Strip whitespace and newline characters and exclude empty lines

# Function to generate random line
def get_random_line(file_lines, selected_lines):
    available_lines = [line for line in file_lines if line not in selected_lines]
    return random.choice(available_lines) if available_lines else ""

# File paths
input_files_path = "D:/Bingo Game/Input/"
output_file_path = "D:/Bingo Game/Output/Bingo Cards.csv"

# File names
b_file = "BINGO_Column1_B.txt"
i_file = "BINGO_Column2_I.txt"
n_file = "BINGO_Column3_N.txt"
g_file = "BINGO_Column4_G.txt"
o_file = "BINGO_Column5_O.txt"
free_space_file = "BINGO_FreeTile.txt"

# Read lines from files and remove whitespace/newline characters
b_lines = read_lines_from_file(input_files_path + b_file)
i_lines = read_lines_from_file(input_files_path + i_file)
n_lines = read_lines_from_file(input_files_path + n_file)
g_lines = read_lines_from_file(input_files_path + g_file)
o_lines = read_lines_from_file(input_files_path + o_file)
free_space_lines = read_lines_from_file(input_files_path + free_space_file)

# Generate data for CSV
data = []

for i in range(1, 81):  # Generate 80 records
    record = {'ID': f"{i:03}"}

    # Ensure uniqueness for each category
    selected_blines = set()
    selected_ilines = set()
    selected_nlines = set()
    selected_glines = set()
    selected_olines = set()

    # B
    for j in range(1, 6):
        field_key = f'B{j}'
        selected_line = get_random_line(b_lines, selected_blines)
        selected_blines.add(selected_line)
        record[field_key] = selected_line

    # I
    for j in range(1, 6):
        field_key = f'I{j}'
        selected_line = get_random_line(i_lines, selected_ilines)
        selected_ilines.add(selected_line)
        record[field_key] = selected_line

    # N (with free space handling)
    for j in range(1, 6):
        field_key = f'N{j}'
        selected_line = get_random_line(n_lines, selected_nlines)
        if j == 3:
            selected_line = random.choice(free_space_lines)
        selected_nlines.add(selected_line)
        record[field_key] = selected_line

    # G
    for j in range(1, 6):
        field_key = f'G{j}'
        selected_line = get_random_line(g_lines, selected_glines)
        selected_glines.add(selected_line)
        record[field_key] = selected_line

    # O
    for j in range(1, 6):
        field_key = f'O{j}'
        selected_line = get_random_line(o_lines, selected_olines)
        selected_olines.add(selected_line)
        record[field_key] = selected_line

    data.append(record)

# Write data to CSV
csv_columns = ['ID', 'B1', 'B2', 'B3', 'B4', 'B5', 'I1', 'I2', 'I3', 'I4', 'I5', 'N1', 'N2', 'N3', 'N4', 'N5', 'G1', 'G2', 'G3', 'G4', 'G5', 'O1', 'O2', 'O3', 'O4', 'O5']

try:
    with open(output_file_path, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for record in data:
            writer.writerow(record)
    print(f"CSV file generated at: {output_file_path}")
except IOError as e:
    print(f"Error writing CSV: {e}")
except Exception as ex:
    print(f"An unexpected error occurred while writing CSV: {ex}")
