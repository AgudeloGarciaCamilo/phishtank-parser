from typing import List
from models.phishing_record import PhishingRecord


class PhishingRecordWriter:
    def write_records_to_file(self, records: List[PhishingRecord], file_path: str):
        with open(file_path, 'w') as file:
            for record in records:
                file.write(f"ID: {record.id}\n")
                file.write(f"URL: {record.url}\n")
                file.write(f"Status: {record.is_online.value}\n")
                file.write(f"Target: {record.target}\n")
                file.write("\n")
                
        print(f"Phishing records written to file: {file_path}")