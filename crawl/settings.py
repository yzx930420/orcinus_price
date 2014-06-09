__author__ = 'Dazdingo'

BOT_NAME = 'orcinus_price spiders'

SPIDER_MODULES = ['crawl.spiders']
NEWSPIDER_MODULE = 'crwal.spiders'
ITEM_PIPELINES = {
    'crawl.pipelines.BookPipeline': 300,
    'crawl.pipelines.DetailPipeline': 800,
}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
DOWNLOAD_DELAY = 2
RANDOMIZE_DOWNLOAD_DELAY = True
USER_AGENT = ['Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.114 Safari/537.36',
              'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.66 Safari/537.36',
              'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)',
              'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.2)',
              'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
              'Mozilla/4.0 (compatible; MSIE 5.0; Windows NT)',
              'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070309 Firefox/2.0.0.3']
COOKIE_ENABLED = True
#LOG_FILE = 'C:/Users/Administrator/Source/Repos/orcinus_price/crawl/error.txt'
LOG_FILE = 'log/error.txt'
LOG_ENABLED = False