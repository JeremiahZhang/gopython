# encoding=utf-8
import io

f = io.open("abc.txt", "wt", encoding="utf-8")
f.write(u"我爱编程")
f.close()

text = io.open("abc.txt", encoding="utf-8").read()
print('---')
print(text)