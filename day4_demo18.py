import logging


class LoggingDict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        logging.info('set %r to %r'%(key, value))


logging.basicConfig(filename="day4_demo18.log", level=logging.INFO)
l1 = LoggingDict()
l1['Ken'] = 'iOS'
l1['Frank'] = 'Oracle'
l1['Michael'] = 'Java'