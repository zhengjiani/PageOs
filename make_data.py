from ruamel import yaml
from faker import Factory
from random import choice
fake = Factory.create('zh-CN')
#个人信息类
def make_user_data():
    for _ in range(10):
        uesrname = fake.user_name()
        phone = fake.phone_number()
        passwd = fake.password()
        gender_keys=['男','女','未知']
        level_keys=['普通用户','VIP用户','高级VIP用户']
        state_keys=['可用','禁用','注销']
        gender_key=choice(gender_keys)
        level_key=choice(level_keys)
        state_key=choice(state_keys)
        birthday = fake.date(pattern="%Y-%m-%d", end_datetime=None)
        profile = {
            'username':uesrname,
            'phone': phone,
            'passwd': passwd,
            'gender_key':gender_key,
            'level_key':level_key,
            'state_key':state_key,
            'birthday': birthday
        }
        a=[]
        for i in profile.values():
            a.append(i)
            # with open('D:\\code\\python\\bok-choy-master\\tests\\demo\\user.yml', 'w') as nf:
            #     yaml.(a, nf)
        print(a)

make_user_data()


