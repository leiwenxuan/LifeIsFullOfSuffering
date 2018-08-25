# # -*- coding: utf-8 -*-
# # @Time    : 2018/8/24/024 20:33
# # @Author  : LeiWenXuan
# # @Email   : 892028617@qq.com
# # @File    : Sunday.py
# # @Software: PyCharm
#
# 文件存储格式如下：
# id，name，age，phone，job
# 1,Alex,22,13651054608,IT
# 2,Egon,23,13304320533,Tearcher
# 3,nezha,25,1333235322,IT
# 现在需要对这个员工信息文件进行增删改查。
# 基础必做：
# a.可以进行查询，支持三种语法：
# select 列名1，列名2，… where 列名条件
# 支持：小于大于等于，还要支持模糊查找。
# 示例：
# select name, age where age>22
# select * where job=IT
# select * where phone like 133
# 进阶选做：
# b.可创建新员工记录，id要顺序增加
# c.可删除指定员工记录，直接输入员工id即可
# d.修改员工信息
# 语法：set 列名=“新的值” where 条件
# #先用where查找对应人的信息，再使用set来修改列名对应的值为“新的值”
# 注意：要想操作员工信息表，必须先登录，登陆认证需要完成
# 其他需求尽量用函数实现
# 作业要求：
# 1.今天的作业一起打包交上来
# 2.放在作业文件夹中
# 需要交整理的函数相关的思维导图
# 整理的函数知识点的博客链接
# 3.大作业放在文件夹中
# 　　文件夹中需要包括：
# 　　代码
# 　　流程图（请上交一张png图片。如果没有合适的画图软件，可以用processon画）
# 　　readme文件（请上交一个txt文件，对作业进行一些简单说明，包括作业的整体思路，如何运行，实现了哪些功能，遇到了哪些问题等。）


#
# # #先用where查找对应人的信息，再使用set来修改列名对应的值为“新的值”
# # 注意：要想操作员工信息表，必须先登录，登陆认证需要完成
import os


class File_set:
    '''
    b.可创建新员工记录，id要顺序增加
    c.可删除指定员工记录，直接输入员工id即可
    d.修改员工信息语法：set 列名=“新的值” where 条件
    '''
    myfile = 'Hr_table'
    _username = 'lwx'
    _passworld = 123456

    def __init__(self):
        pass

    def open_file_w(self):
        with open(self.myfile, mode='r', encoding='utf-8') as fw:
            pass

    def register(self, username, passworld):
        if self._username == username and self._passworld == passworld:
            print('验证成功！')
        else:
            print('密码账号不正确！')

    def add_staff(self):
        name = input('添加员工信:'
                  'name, age, phone, job以,号隔开：')

        with open(self.myfile, mode='r+', encoding='utf-8') as fw:
            for line in fw:
                pass
            line = line.strip().split(',')
            print(line[0])
            id = int(line[0]) + 1
            fw.write('\n' + str(id)+ ',' + name)

    def expurgate(self):
        '''输入ID 进行删除'''
        id = input('要删除员工的ID:')
        with open(self.myfile, mode='r', encoding='utf-8') as fr, \
                open(self.myfile + '.bak', mode='w', encoding='utf-8') as fw:
            for line in fr:
                line = line.replace('，', ',')
                line = line.strip().split(',')
                if line[0].isdigit() and int(line[0]) == int(id):
                    print('删除员工\n%s--%s--%s--%s--%s' % (line[0], line[1], line[2], line[3], line[4]))
                else:
                    fw.write(','.join(line) + '\n')
        os.remove(self.myfile)
        os.rename(self.myfile + '.bak', self.myfile)

    def amend(self):
        '''d.修改员工信息语法：set 列名=“新的值” where 条件'''
        pass

    def Open_file(self):
        select = input('输入查询指令：')
        select = select.split(' ')
        # print(select)
        Flag = True
        with open('Hr_table', mode='r', encoding='utf-8') as f:
            first = f.readline().strip().replace('，', ',').split(',')
            # print(first)
            print('ID--name--age--phone--job')
            for line in f:
                line = line.replace('，', ',').strip()
                line = line.split(',')
                if select[-1] in line:
                    print('-'.join(line))
                    Flag = False
                elif '列名' in select[-1]:
                    if int(select[-1][-1]) < 5:
                        print(line[int(select[-1][-1]) - 1])
                    else:
                        print('输入的域名有误')
                        break
                    Flag = False
                elif 'phone' in select:
                    if select[-1] in line[-2]:
                        print('-'.join(line))
                        Flag = False
                elif 'job' in select[-1]:
                    '''输入的命名有job ，执行按职业查找'''
                    if select[-1].strip().split('=')[-1] == line[-1]:
                        ''' job=IT分割成[job,IT]，判断文件里面数据的IT的数据'''
                        print('-'.join(line))
                    Flag = False
                elif '<' in select[-1] or '>' in select[-1]:
                    if select[-1].count('<'):
                        # print(select[-1].split('<')[-1])
                        # print(line[-3])
                        if int(select[-1].split('<')[-1]) > int(line[-3]):
                            print('-'.join(line))
                    elif select[-1].count('>'):
                        if int(select[-1].split('>')[-1]) < int(line[-3]):
                            print('-'.join(line))
                    Flag = False
            if Flag:
                print('没有查找到！')


p1 = File_set()


# p1.add_staff('1','l', '23', '1555', 'IT')
# p1.register(1212,12121)
# p1.expurgate


def matching(select):
    Gt_Lt = ['name', 'eag', '>', '<', 'phone', 'job']
    for s in Gt_Lt:
        if s in select and s == 'name':
            print('匹配成功%s' % s)
            s.isalpha()


dic_ql = {
    1: p1.Open_file,  # 查询
    2: p1.add_staff,  # 创建
    3: p1.expurgate,  # 删除
    4: p1.amend  # 修改
}

while 1:
    '''
        总的话分为3中查询
        select name, age where age>22
        select * where job=IT
        select * where phone like 133
    '''
    print('1:查询 2:创建 3:删除 4:修改')
    select = input('请输入相应的指令查找：').strip()

    if select.upper() == 'Q':
        print('退出系统！')
        break
    elif len(select) < 2 and select.isdigit():
        select = int(select)
        dic_ql[int(select)]()
    elif select.isdigit():
        print('***')

