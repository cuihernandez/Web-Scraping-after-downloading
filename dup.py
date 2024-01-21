import csv

def remove_duplicate_emails(csv_file):
    # Read the CSV file and collect unique emails
    unique_emails = set()
    duplicate_emails = set()
    with open(csv_file, "r",  encoding='Latin1') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 0:
                continue

            email = row[0].strip()  # Assuming the email is in the first column
            if email in unique_emails:
                duplicate_emails.add(email)
            else:
                unique_emails.add(email)

    # Write the unique emails to a new CSV file
    output_file = "unique_emails1.csv"
    with open(output_file, "w", newline="\n",encoding='Latin1') as file:
        writer = csv.writer(file)
        writer.writerow(["Email"])  # Write the header
        for email in unique_emails:
            writer.writerow([email])

    print(f"Duplicate emails removed. Unique emails saved in {output_file}.")

# Provide the path to your CSV file
csv_file = "unique_emails.csv"

# Call the function to remove duplicate emails
remove_duplicate_emails(csv_file)