import subprocess
result = subprocess.Popen('scrapy crawl coinspot -o test_data.csv',
                          stdout=subprocess.PIPE, shell=True).communicate()[0]
