# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
class dangdangPipeline(object):
	con = pymongo.Connection("localhost", 27017)
	db = con.bestbuyer
	def process_item(self, item, spider):
		if(len(item['ISBN']) == 0):
			return item
		dbdata = {"name":"","price":"","ISBN":"","author":"","press":""}
		dbdata["name"] = item["name"][0]
		dbdata["price"] = item["price"][0]
		dbdata["ISBN"] = item["ISBN"][0]
		dbdata["author"] = item["author"][0]
		dbdata["press"] = item["press"][0]
		try:
			self.db.bookInfo.insert(dbdata)
		except:
			print "====================================wocao"

		return item
