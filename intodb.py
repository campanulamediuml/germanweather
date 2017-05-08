import MySQLdb as mydatabase

conn = mydatabase.connect(host='117.25.155.149', port=3306, user='gelinroot', passwd='glt#789A', db='db_data2force', charset='utf8')
cursor = conn.cursor()

try:
    sql = """CREATE TABLE German_Weather_data(id INT(11)primary key auto_increment,Date_Time VARCHAR(200),cities TEXT(1000),Temp TEXT(1000),Summe_1 VARCHAR(200),Summe_2 TEXT(1000))"""
    cursor.execute(sql)
except:
    print 'table exists..'

fh = open('weather.txt','r')
result = fh.readlines()

count = 0
for i in result:
    item = []
    i = (i.strip()).decode('utf-8')
    tmp = i.split('\t')
    for j in tmp:
        if j == '':
            continue
        else:
            item.append(j)
    if len(item) == 5:
        cursor.execute('INSERT INTO German_Weather_data(Date_Time,cities,Temp,Summe_1,Summe_2)  values(%s,%s,%s,%s,%s)',item) 
        count = count+1
        if count%50 == 0:
            conn.commit()
    else:
        print item

conn.commit()