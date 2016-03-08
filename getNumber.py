import re
import MySQLdb as mdb
import sys

reload(sys)
sys.setdefaultencoding( "utf-8" )

input = open("0.txt")
weiboId = input.readline()
selectedType = ['ni', 'b', 'nl', 'ns', 'nt', 'nz', 'i', 'j', 'n', 'ws', 'nh']
dictionary = {}
while weiboId:
    userId = input.readline()
    content = input.readline()
    content  = re.split('\t',content)
    content.pop(len(content)-1)
    for i in range(len(content)):
        content[i] = re.split(' ',content[i])
    for word in content:
        if dictionary.has_key(word[0]):
            if (word[1] in selectedType):
                dictionary[word[0]]+=1
        else:
            if (word[1] in selectedType):
                dictionary[word[0]]=1
    weiboId = input.readline()
# print sorted(dictionary.iteritems(), key=lambda d:d[1], reverse = True )
dictionary = sorted(dictionary.iteritems(), key=lambda d:d[1], reverse = True )
# for i in range(100):
#     print dictionary[i][0]+' '+str(dictionary[i][1])
wordsNumber = len(dictionary)
#save to database
con = mdb.connect('liuqi.xyz', 'root', 'liuqisdb', 'publicopinion',charset='utf8')
cur = con.cursor()
for i in range(wordsNumber):
    values=[str(i),'-1',dictionary[i][0],str(dictionary[i][1])]
    sql = "insert into hot_words values(%s,%s,%s,%s)"
    cur.execute(sql,values)
# sql = "insert into hot_words values(0,-1,123,123)"
# values = ['1','-1',"hello","123"]
# cur.execute("insert into hot_words values(%s,%s,%s,%s)",values)
con.commit()
con.close()
print   dictionary[0][1]
