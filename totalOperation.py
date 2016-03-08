import MySQLdb as mdb
import sys
import originSegementFunciton
import json
#概率检测编码
import chardet
import thread
#设置编码
reload(sys)
sys.setdefaultencoding( "utf-8" )
#连接mysql，获取连接的对象

def writeToFile(m,n):
    # print m,n
    con = mdb.connect('localhost', 'root', '1234', 'publicopinion',charset='utf8')
    with con:
        #仍然是，第一步要获取连接的cursor对象，用于执行查询
        cur = con.cursor()
        #类似于其他语言的query函数，execute是python中的执行查询函数
        sql = "SELECT * FROM total_weibo limit "+str(m)+','+str(n)
        cur.execute(sql)
        #使用fetchall函数，将结果集（多维元组）存入rows里面
        rows = cur.fetchall()
        #依次遍历结果集，发现每个元素，就是表中的一条记录，用一个元组来显示
        filename =str(m)+".txt"
        fp = open(filename,'w')
        for row in rows:
            text = row[5].encode("UTF-8")
            # print text
            # print row
            ans = originSegementFunciton.Analyze(text,'pos')
            ans = json.loads(ans)
            weibo = {'id': '0', 'text': '', 'ans': ''}
            weibo['id'] = row[0]
            print row[0]
            weibo['text'] = text
            structedAns = []
            weibo['ans'] = ans
            # print ans[0][0]
            fp.write(str(row[0]))
            fp.write('\n')
            fp.write(row[1])
            fp.write('\n')
            for single in ans[0][0]:
                fp.write(single['cont'])
                fp.write(' ')
                fp.write(single['pos'])
                fp.write('\t')
            fp.write("\n")
            # fencoding=chardet.detect(text)
            # print fencoding
            # print row[5]
        # for row in rows:
            # ans = originSegementFunciton.Analyze(row[5].decode('utf-8'),'pos')
            # print (row[5].decode('utf-8'))
        # ans = json.loads(ans)
        # print ans[0][0][0]


        fp.close()
    con.close()
    # thread.exit_thread()
