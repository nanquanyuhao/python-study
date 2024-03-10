f = open(r"D:\code\github\python-study\16_读写文件\file_w.txt", 'a', encoding='utf8')
f.write("你好\n她也好")
f.writelines(["hello\n", "world\n"])
f.close()