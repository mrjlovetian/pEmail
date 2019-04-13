import yagmail
import pymysql

yag = yagmail.SMTP(user='1520312758@qq.com', password='nowvmlstbelshdhf',host='smtp.qq.com')#参数为发送邮箱, 邮箱密码(授权码), 发送邮箱服务器

#邮箱正文,是一个列表
contents = [
            "<h1 style='color:red'>一级标题</h1>",#可以是html语言
            #'beauty.jpg',#可以是文件,以附件形式发送
            yagmail.inline('beauty.jpg'),# 这样的话,图片会内嵌到正文
            'hello world', #可以是普通文本
            ]

db = pymysql.connect('localhost', 'root', '897011805', 'yhj')
cursor = db.cursor()
sql = "select email from newhaiwai limit 20"
cursor.execute(sql)
db.commit()
results = cursor.fetchall()
for row in results:
    fname = row[-1]
    # lname = row[1]
    # age = row[2]
    # sex = row[3]
    # income = row[4]
    print('zzzzzzzzzzzzzzzzzzzzzzzzzzz', fname)
db.close()

# yag.send(to = '409360559@qq.com',subject ='test',contents = contents)