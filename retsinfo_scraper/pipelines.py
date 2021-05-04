# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

class RetsinformationPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter.get('doc_id'):
            item.save()
            return adapter.get('doc_id')
        else:
            raise DropItem(f"Missing price in {item}")
