import csv

def read_points_from_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file if line.strip()]

def write_points_to_csv(points, output_file):
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Key Points"])  # Header
        for point in points:
            writer.writerow([point])
    print(f"Points saved to: {output_file}")

if __name__ == "__main__":
    txt_file = "your_notes.txt"         # Replace with your input file
    csv_file = "summary_points.csv"     # Output file for Excel

    points = read_points_from_txt(txt_file)
    write_points_to_csv(points, csv_file)
