
import os
import subprocess
import time


class Saver(object):
    def write(self, content, user_name, group_name, content_type, timestamp, append=True):
        raise NotImplementedError('This method didn\'t implement yet')


class TextSaver(Saver):

    def __init__(self, location=None, strategy='BY_GROUP', verbose=False):
        self._store_strategy = strategy
        self._location = location
        self._echo = verbose

    def write(self, content, user_name, group_name, timestamp, content_type='text', append=True):
        label = group_name if group_name else user_name
        is_group = True if group_name else False
        file = self._get_file_name(is_group, label)
        formatted_msg = '{} {}:\n\t{}\n'.format(timestamp, user_name, content)
        with open(file, 'a', encoding='utf-8') as f:
            f.write(formatted_msg)

        if self._echo:
            print(formatted_msg)

    def _get_file_name(self, is_group, who):
        category = 'groups' if is_group else 'friends'
        location = self._location
        if not location:
            bot_dir = 'wechatbot_data'
            if os.name == 'poxis':
                root = '/home'
                user = subprocess.check_output('whoami')
                location = os.path.join(root, user, bot_dir, category)
            else:
                root = 'C:\\Users'
                b_str = subprocess.check_output('whoami')
                b_str = b_str[:-2]
                user_str = str(b_str, encoding='utf-8')
                user = user_str.split('\\')[-1]
                location = os.path.join(root, user, bot_dir, category)
        if not os.path.exists(location):
            os.mkdir(location)
        prefix = time.strftime('%Y_%m_%d_')
        suffix = who
        return os.path.join(location, prefix + suffix + '.txt')
