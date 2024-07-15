import csv

# Read your CSV file
input_file = 'contacts.csv'
output_file = 'my_contacts.vcf'  # Change this to your desired output filename

with open(input_file, mode='r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open(output_file, mode='w', encoding='utf-8') as vcf_file:
        for row in csv_reader:
            # Add "ACM" to the last name
            last_name_with_acm = f"{row['Last Name']} ACM"

            vcf_file.write("BEGIN:VCARD\n")
            vcf_file.write("VERSION:3.0\n")
            vcf_file.write(f"N:{last_name_with_acm};{row['First Name']};;;\n")
            vcf_file.write(f"FN:{row['First Name']} {last_name_with_acm}\n")
            vcf_file.write(f"EMAIL;TYPE=INTERNET:{row['Email Address']}\n")
            vcf_file.write(f"TEL;TYPE=CELL:{row['Mobile Number']}\n")
            vcf_file.write("END:VCARD\n")

print(f"Converted contacts saved to {output_file}")
