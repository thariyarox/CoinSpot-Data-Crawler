# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class CrawlerPipeline:
    def process_item(self, item, spider):
        return item


# This pipeline will store all the scraped data to the specified text file
class TextDataPipeline:

    def open_spider(self, spider):
        # Create the text data file and set the character set to utf-8
        self.file = open('text_data.txt', 'w', encoding='utf-8')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        # Save the crawled text in every line of the text file
        dataItem = str(item).replace('{', '')
        dataItem = dataItem.replace('}', '')
        self.file.write(dataItem+'\n')
        return item
