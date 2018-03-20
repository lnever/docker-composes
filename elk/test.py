import logging
import logstash
import sys

# host = '127.0.0.1'
# port = 5045
#
# test_logger = logging.getLogger('python-logstash-logger')
# test_logger.setLevel(logging.INFO)
# test_logger.addHandler(logstash.LogstashHandler(host, port))
#
# test_logger.addHandler(logstash.TCPLogstashHandler(host, port))

# test_logger.error('python-logstash: test logstash error message.')
# test_logger.info('python-logstash: test logstash info message.')
# test_logger.warning('python-logstash: test logstash warning message.')

# add extra field to logstash message
# extra = {
#     'test_string': 'python version: ' + repr(sys.version_info),
#     'test_boolean': True,
#     'test_dict': {'a': 1, 'b': 'c'},
#     'test_float': 1.23,
#     'test_integer': 123,
#     'test_list': [1, 2, '3'],
# }
# test_logger.info('python-logstash: test extra fields', extra=extra)

import time
from datetime import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch()

es.index(index="test-alert", doc_type="test-type", body={"any": "test", "@timestamp": datetime.now()})

# res = es.search(index="test-alert")
#
# print(res)
