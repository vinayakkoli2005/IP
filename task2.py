import pandas as pd
import re

# load file 
# twitter = pd.read_csv('twitterdataoutput.csv', encoding='utf-8')

# import re

# text = "@nytpolitics Finally some great news, hope they lose!"
# clean_text = re.sub(r'[^A-Za-z0-9 ]+', '', text)
# print(clean_text)
# output- nytpolitics Finally some great news hope they lose

# text = "The latest The SPORTS Daily! https://t.co/VwI91583JF Thanks to @anaesthete @chachies4eva #sports #news"
# output - The latest The SPORTS Daily httpswwwtcovwI91583JF Thanks to anaesthete chachies4eva sports news


# text = "@nytpolitics Finally some great news, hope they lose"
# clean_text = re.sub(r'@\w+', '', text)
# print(clean_text)
# Finally some great news, hope they lose

# sentence - The latest The SPORTS Daily! https://t.co/VwI91583JF Thanks to @anaesthete @chachies4eva #sports #news
# result - The latest The SPORTS Daily! https://t.co/VwI91583JF Thanks to   #sports #news


# no of special charater (cond) 
# one lakh example 
# gemini 2000 examample (given this context  )


# ------------------------------------------------------------------------------------------------------------------------


# twitter total rows - Number of rows: 306102 
#short sentences twitter - (30) Total short sentences found: 11830
# Number of rows filteredtwitter : 294272                                                       ====>>> Info
# wikidata total rows - Number of rows: 309056
#short sentences wiki- (30) Total short sentences found: 2497
# Number of rows filteredwiki: 306559

# ---------------------------------------------------------------------------------------------------------------------

# filter the small sentences 


# import csv

# # Set threshold for minimum content length
# MIN_CONTENT_LENGTH = 30

# def filter_and_save(input_file, output_file, label):
#     print(f"\n--- Short sentences from {label} ---")
#     short_count = 0
#     total_rows = 0

#     with open(input_file, "r", encoding='utf-8') as infile, \
#          open(output_file, "w", encoding='utf-8', newline='') as outfile:

#         reader = csv.DictReader(infile)
#         fieldnames = reader.fieldnames
#         writer = csv.DictWriter(outfile, fieldnames=fieldnames)
#         writer.writeheader()

#         for row in reader:
#             total_rows += 1
#             content = row.get('content', '').strip()
#             if len(content) < MIN_CONTENT_LENGTH:
#                 print(f"ID: {row.get('id', '')} | Content: {content} | Date: {row.get('date', '')}")
#                 short_count += 1
#             else:
#                 writer.writerow(row)

#     print(f"Total short sentences found: {short_count}")
#     print(f"Filtered data written to {output_file}. Remaining rows: {total_rows - short_count}\n")


# # Process each dataset independently
# filter_and_save("twitterdataoutput.csv", "filteredtwitter.csv", "Tweets Dataset")
# filter_and_save("wikidataoutput.csv", "filteredwiki.csv", "Wikidata Dataset")

# -------------------------------------------

# date to timestamp

# import csv
# from datetime import datetime
# from dateutil import parser  # Handles ISO date formats

# def standardize_timestamp(input_file, output_file, label):
#     print(f"\n--- Processing {label} ---")

#     timestamps = []
#     rows = []

#     # Step 1: Read and convert dates to UNIX timestamps
#     with open(input_file, 'r', encoding='utf-8') as infile:
#         reader = csv.DictReader(infile)
#         for row in reader:
#             date_str = row['date'].strip()
#             try:
#                 dt = parser.parse(date_str)
#                 timestamp = dt.timestamp()
#                 row['timestamp'] = timestamp
#                 timestamps.append(timestamp)
#                 rows.append(row)
#             except Exception as e:
#                 print(f"Skipping row due to error in date parsing: {e}")

#     if not timestamps:
#         print("No valid timestamps found.")
#         return

#     min_ts = min(timestamps)
#     max_ts = max(timestamps)

#     def scale(ts):
#         return 0 if min_ts == max_ts else ((ts - min_ts) / (max_ts - min_ts)) * 100

#     # Step 2: Normalize and write to new file
#     with open(output_file, 'w', encoding='utf-8', newline='') as outfile:
#         writer = csv.DictWriter(outfile, fieldnames=['id', 'content', 'timestamp'])
#         writer.writeheader()

#         for row in rows:
#             scaled_ts = round(scale(row['timestamp']), 3)  # Rounded to 3 decimals
#             writer.writerow({
#                 'id': row['id'],
#                 'content': row['content'],
#                 'timestamp': scaled_ts
#             })

#     print(f"Standardized timestamps written to {output_file}.\n")

# # Run for both datasets
# standardize_timestamp("filteredtwitter.csv", "standardisedtwitter.csv", "Twitter Dataset")
# standardize_timestamp("filteredwiki.csv", "standardisedwiki.csv", "Wikidata Dataset")
