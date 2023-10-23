# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

class RentScrapePipeline:

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn=sqlite3.connect('makaan.db')
        self.curr=self.conn.cursor()

    def create_table(self):
        self.curr.execute(""" drop table if exists rent_details """)
        self.curr.execute(""" create table rent_details(
                        title text, city text, locality text,
                        price text, area text, status text,
                        deposit text, num_bath text)""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self,item):
        self.curr.execute(""" insert into rent_details values (?,?,?,?,?,?,?,?)""",(
            item['title'][0],
            item['city'][0],
            item['locality'][0],
            item['price'][0],
            item['area'][0],
            item['status'][0],
            item['deposit'][0],
            item['num_bath'][0],
        ))
        self.conn.commit()
