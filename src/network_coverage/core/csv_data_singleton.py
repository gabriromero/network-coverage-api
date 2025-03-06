import csv

class CsvDataSingleton:
    _instance = None
    sites_mobiles_data = {}
    mcc_mnc_data = {}

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._load_sites_mobiles_data()
            cls._load_mcc_mnc_data()
        return cls._instance

    @classmethod
    def _load_sites_mobiles_data(cls):
        with open('src/network_coverage/data/sites_mobiles.csv', 'r') as f:
            reader = csv.reader(f, delimiter=';')
            for row in reader:
                key = tuple(row[1:3])
                value = (row[0], tuple(row[3:6]))
                cls.sites_mobiles_data[key] = value

    @classmethod
    def _load_mcc_mnc_data(cls):
        with open('src/network_coverage/data/mcc_mnc_table.csv', 'r') as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                
                if len(row) < 8:
                    continue
                
                mcc = row[0].strip()
                mnc = row[2].strip()
                operator = row[7].strip()

                key = f"{mcc}{mnc}"
                cls.mcc_mnc_data[key] = operator

    @classmethod
    def get_site_mobile_data(cls, key):
        """Retrieve data from the dictionary using a key."""
        return cls.sites_mobiles_data.get(key)
    
    @classmethod
    def get_operator_name(cls, key):
        """Retrieve data from the dictionary using a key."""
        return cls.mcc_mnc_data.get(key)

csv_data = CsvDataSingleton()
