import subprocess
import os

dirname = os.path.dirname(__file__)
result = subprocess.Popen('scrapy crawl coinspot -o '+os.path.join(dirname,'../data/test_data.csv'),
                          stdout=subprocess.PIPE, shell=True).communicate()[0]
data_process = subprocess.Popen('python '+os.path.join(dirname,'../processors/process_data.py'),
        stdout=subprocess.PIPE, shell=True).communicate()[0]
csv_process = subprocess.Popen('python '+os.path.join(dirname,'../processors/process_csv.py'),
        stdout=subprocess.PIPE, shell=True).communicate()[0]