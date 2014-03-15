__author__ = 'Dazdingo'

BOT_NAME = 'crawl'

SPIDER_MODULES = ['crawl.spiders']
NEWSPIDER_MODULE = 'crawl.spiders'
ITEM_PIPELINES = ['crawl.pipelines.dangdangPipeline']
# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.66 Safari/537.36'
LOG_FILE = 'C:/Users/Administrator/Source/Repos/orcinus_price/crawl/error.txt'
LOG_ENABLED = True