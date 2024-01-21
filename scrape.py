import csv
import urllib.request
import re

input_csv_file = 'updated_websites.csv'
output_csv_file = 'new_emails.csv'

with open(input_csv_file, 'r') as file:
    reader = csv.reader(file)
    sites = [row[0] for row in reader]

new_emails = []

for site in sites:
    try:
        f = urllib.request.urlopen(site)
        s = f.read().decode('utf-8')
        emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}", s)
        new_emails.extend(emails)
    except Exception as e:
        print(f"Skipping URL: {site}. Error: {str(e)}")

# Remove duplicate emails
new_emails = list(set(new_emails))

# Append the new_emails to the output CSV file
with open(output_csv_file, 'a', newline='') as file:
    writer = csv.writer(file)

    for email in new_emails:
        writer.writerow([email])
        print(f"Email: {email}")

print("New emails appended to:", output_csv_file)