import csv

# Open the input CSV file
with open('12.csv', 'r') as input_file:
    # Read the CSV content
    csv_reader = csv.reader(input_file)

    # Open the output CSV file
    with open('output7.csv', 'w', newline='') as output_file:
        # Create a CSV writer object
        csv_writer = csv.writer(output_file)

        # Iterate through each row in the input CSV
        for row in csv_reader:
            # Remove spaces from each value in the row
            cleaned_row = [value.strip() for value in row if value.strip()]

            # Write the cleaned row to the output CSV if it is not empty
            if cleaned_row:
                csv_writer.writerow(cleaned_row)