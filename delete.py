import csv

# Read the CSV file
with open('contact_us_new_emails.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    rows = list(reader)

# Delete cells containing 'jpg' or 'png'
for row in rows:
    for i, cell in enumerate(row):
        if 'jpg' in cell or 'png' in cell or 'heic' in cell or 'gif' in cell or 'webp' in cell or 'JPG' in cell or 'JPEG' in cell or 'jpeg' in cell or 'svg' in cell or 'PNG' in cell or 'example' in cell or 'user' in cell:
            row[i] = ''

# Write the updated rows back to the CSV file
with open('12.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(rows)