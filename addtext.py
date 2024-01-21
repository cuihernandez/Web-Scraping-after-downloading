import csv

input_csv_file = 'websites.csv'
output_csv_file = 'contact_us_websites.csv'

with open(input_csv_file, 'r') as file:
    reader = csv.reader(file)
    websites = [row[0] for row in reader]

updated_websites = ['http://' + website + '/pages/contact-us' for website in websites ]

with open(output_csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    for website in updated_websites:
        writer.writerow([website])

print("Websites updated and saved to:", output_csv_file)