import os

'''
自己写一个随机生成字母的类，因为如果要导入random库的话，最后发布出来的程序就会更大，而我们可以用os来完成这个
功能，os库又是必须的，因为我用到的os库的功能没办法自己来完成。
'''


class Random_name():
    def __init__(self, name_length):
        self.alpha = [chr(x) for x in range(65, 91)] + ['_'] + [chr(x) for x in range(97, 123)]#变量名允许的格式，不用中文
        self.name_length = name_length

    def generate_name(self):
        random_number = os.urandom(self.name_length)
        name = ''
        for number in random_number:
            name += self.alpha[number % len(self.alpha)]
        return name


