# import pandas as pd
# import re

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

import csv

# Set threshold for minimum content length
MIN_CONTENT_LENGTH = 200

def filter_and_save(input_file, output_file, label):
    print(f"\n--- Short sentences from {label} ---")
    short_count = 0
    total_rows = 0

    with open(input_file, "r", encoding='utf-8') as infile, \
         open(output_file, "w", encoding='utf-8', newline='') as outfile:

        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            total_rows += 1
            content = row.get('content', '').strip()
            if len(content) < MIN_CONTENT_LENGTH:
                # print(f"ID: {row.get('id', '')} | Content: {content} | Date: {row.get('date', '')}")
                short_count += 1
            else:
                writer.writerow(row)

    print(f"Total short sentences found: {short_count}")
    print(f"Filtered data written to {output_file}. Remaining rows: {total_rows - short_count}\n")


# Process each dataset independently
# filter_and_save("filtered_wiki_english.csv", "shortlisted_wiki.csv", "Wikipedia Dataset")
filter_and_save("filtered_twitter_english.csv", "shortlisted_twitter.csv", "Twitter Dataset")


# Filtered data written to shortlisted_wiki.csv. Remaining rows: 77708
# Filtered data written to shortlisted_twitter.csv. Remaining rows: 59466
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

# ----------------------------------------------------------------------------------------

# find no. of non english sentences 

# import pandas as pd
# from langdetect import detect
# from langdetect.lang_detect_exception import LangDetectException

# def is_english(text):
#     try:
#         return detect(text) == 'en'
#     except LangDetectException:
#         return False

# def count_non_english_sentences(file_path):
#     df = pd.read_csv(file_path)

#     if 'content' not in df.columns:
#         print(f"'content' column not found in {file_path}")
#         return

#     non_english_count = 0
#     total = len(df)

#     for i, text in enumerate(df['content'].astype(str)):
#         if not is_english(text):
#             non_english_count += 1

#     print(f"{file_path}: {non_english_count} non-English sentences out of {total} total rows.")

# # count_non_english_sentences('standardisedtwitter.csv')
# count_non_english_sentences('standardisedwiki.csv')
# # print("done")

# standardisedtwitter.csv: 78300 non-English sentences out of 294271 total rows.
# standardisedwiki.csv: 3330 non-English sentences out of 306558 total rows.

# ------------------------------------------------------------------------------------------------------------------------


#  eliminating non english sentences

# import pandas as pd
# from langdetect import detect
# from langdetect.lang_detect_exception import LangDetectException

# # Function to detect if the text is in English
# def is_english(text):
#     try:
#         return detect(text) == 'en'
#     except LangDetectException:
#         return False

# # Function to process one file and remove non-English rows
# def remove_non_english_rows(input_path, output_path):
#     df = pd.read_csv(input_path)

#     if 'content' not in df.columns:
#         print(f"'content' column not found in {input_path}")
#         return

#     # Apply language detection
#     df['is_english'] = df['content'].astype(str).apply(is_english)

#     # Filter only English rows and drop the helper column
#     english_df = df[df['is_english']].drop(columns=['is_english'])

#     # Save to output file
#     english_df.to_csv(output_path, index=False)
#     print(f"Saved {len(english_df)} English rows to '{output_path}' (from {len(df)} total).")


# remove_non_english_rows('standardisedtwitter.csv', 'filtered_twitter_english.csv')
# remove_non_english_rows('standardisedwiki.csv', 'filtered_wiki_english.csv')

# print(len(pd.read_csv('filtered_wiki_english.csv')))