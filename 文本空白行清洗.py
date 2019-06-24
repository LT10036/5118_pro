
# ----------------------------------------------------------------------------
# 5118下载的文本有空白行，需要清洗空白行
# ----------------------------------------------------------------------------


import os


root = 'C:\\Users\\Administrator\\Desktop\\趣头条文本\\'
new_root = 'C:\\Users\\Administrator\\Desktop\\清洗后的文章\\'

list_txt = os.listdir('C:\\Users\\Administrator\\Desktop\\趣头条文本')
print(list_txt)

for i in list_txt:
    try :
        text_root = root + i
        text_root2 = new_root + i
        w = open(text_root2,'a')
        f = open(text_root, 'r')
        while True:
            con = f.readline()
            if not con:
                break
            else:
                if con =="\n":
                    continue
                else:
                    print(con)
                    w.write(con)
                    # w.write('\n')

        f.close()
        w.close()
    except:
        continue

