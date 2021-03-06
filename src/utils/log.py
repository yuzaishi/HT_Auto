# -*- coding:utf-8 -*-
__author__ = '朱永刚'
import os
import logging
from logging.handlers import TimedRotatingFileHandler
from utils.config import LOG_PATH,Config

class Logger(object):
    def __init__(self,logger_name='framework'):
        self.logger = logging.getLogger(logger_name)
        logging.root.setLevel(logging.NOTSET)
        c = Config().get('log')
        self.log_file_name = c.get('file_name')
        self.back_count = c.get('backup')
        self.console_output_level = c.get('console_level')
        self.file_output_level =c.get('file_level')
        self.formatter = logging.Formatter(c.get('pattern'))

    def get_log(self):
        """在logger中添加日志句柄并返回，如果logger已有句柄，则直接返回"""
        if not self.logger.handlers:#避免日志重复
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(self.formatter)
            console_handler.setLevel(self.console_output_level)
            self.logger.addHandler(console_handler)

            #每天重新创建一个日志文件，最多保留back_count份
            file_hander = TimedRotatingFileHandler(filename=os.path.join(LOG_PATH,self.log_file_name),
                                                   when='D',
                                                   interval=1,
                                                   backupCount=self.back_count,
                                                   delay=True,
                                                   encoding='utf-8'
                                                   )
            file_hander.setFormatter(self.formatter)
            file_hander.setLevel(self.file_output_level)
            self.logger.addHandler(file_hander)
        return self.logger

logger = Logger().get_log()


