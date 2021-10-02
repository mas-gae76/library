from datetime import datetime
from os.path import splitext


def get_timestamp_path_auth(instance, filename):
    return 'authors/%s%s' % (datetime.now().timestamp(), splitext(filename)[1])


def get_timestamp_path_book(instance, filename):
    return 'books/%s%s' % (datetime.now().timestamp(), splitext(filename)[1])