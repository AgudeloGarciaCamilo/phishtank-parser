# Create instances of PhishingDataFetcher and PhishingRecordWriter
from core.phishing_data_fetcher import PhishingDataFetcher
from core.phishing_record_writer import PhishingRecordWriter

from constants.app_constants import PHISHTANK_URL, RECORD_FILE_PATH


data_fetcher = PhishingDataFetcher()
record_writer = PhishingRecordWriter()

data_url = PHISHTANK_URL
file_path = RECORD_FILE_PATH

phishing_records = data_fetcher.fetch_data(data_url)
record_writer.write_records_to_file(phishing_records, file_path)