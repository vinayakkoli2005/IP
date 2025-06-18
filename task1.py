import json
import csv

# Open the input JSON file and output CSV file
with open("wikidata.jsonl", "r", encoding='utf-8') as infile, open("wikidataoutput.csv", "w", newline='', encoding='utf-8') as outfile:
    writer = csv.writer(outfile)

    # Write CSV header
    writer.writerow(['id', 'content', 'date'])

    # Process each line in the JSON file
    for line in infile:
        try:
            item = json.loads(line)
            writer.writerow([
                item.get('identifier', ''),
                item.get('abstract', ''),
                item.get('event', {}).get('date_published', '')
            ])
        except json.JSONDecodeError as e:
            print(f"Skipping line due to JSON error: {e}")



# import gzip





# input_gz_file = "wiki insertions.tsv"
# output_csv_file = "wiki insertions_output.csv"

# with gzip.open(input_gz_file, "rt", encoding="utf-8") as gzfile, open(output_csv_file, "w", newline="", encoding="utf-8") as csvfile:
#     reader = csv.DictReader(gzfile, delimiter="\t")
#     # Use the same fieldnames as in the input file (or just select the ones you want)
#     fieldnames = ["base_sentence", "phrase", "edited_sentence"]
    
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
    
#     for row in reader:
#         # Write only the columns you want to save
#         filtered_row = {field: row[field] for field in fieldnames}
#         writer.writerow(filtered_row)

# print(f"Data saved successfully to {output_csv_file}")