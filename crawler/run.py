import subprocess
result = subprocess.Popen('scrapy crawl coinspot -o ../data/test_data.csv',
                          stdout=subprocess.PIPE, shell=True).communicate()[0]
data_process = subprocess.Popen('python ../processors/process_data.py',
        stdout=subprocess.PIPE, shell=True).communicate()[0]
csv_process = subprocess.Popen('python ../processors/process_csv.py',
        stdout=subprocess.PIPE, shell=True).communicate()[0]
