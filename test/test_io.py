
import sys
print(sys.path)
from src.saver import GroupMsgSaver

def test_GroupMsgSaver_get_file_name():
    s = GroupMsgSaver()
    file = s._get_file_name('dummp_group')
    print(file)


def test_GroupMsgSaver_write():
    s = GroupMsgSaver()
    s.write('test msg', 'zmyzhou', 'group1', '2017-9-9')

if __name__ == '__main__':
    test_GroupMsgSaver_get_file_name()
    test_GroupMsgSaver_write()
