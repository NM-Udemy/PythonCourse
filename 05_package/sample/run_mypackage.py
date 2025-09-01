from mypackage import format_name
from mypackage.string_utils import clean_text
from mypackage import string_utils

def main():
    print('パッケージ使用のデモ')
    name = format_name('smith', 'john')
    print(name)
    print(clean_text('    adfaf.  dsafjej b b'))
    print(string_utils.count_words('text texxt text'))
    
if __name__ == '__main__':
    main()
