import requests

from models.phishing_record import PhishingRecord, PhishingStatus


class PhishingDataFetcher:
    def fetch_data(self, url):
        response = requests.get(url)
        data = response.json()

        phishing_records = []

        for record in data:
            id = record['phish_id']
            url = record['url']
            status_str = record['online']
            target = record['target']
            is_online = PhishingStatus(status_str)
            phishing_record = PhishingRecord(id, url, is_online, target)
            
            phishing_records.append(phishing_record)

        return phishing_records