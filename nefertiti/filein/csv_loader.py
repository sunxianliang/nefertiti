import csv


class CsvLoader(object):

    @staticmethod
    def load(file):
        with open(file, encoding='GBK') as f_in:
            reader = csv.reader(f_in)
            for row in reader:
                yield row
