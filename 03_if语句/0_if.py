x = -4

# pass
# 1(0)
# : 可以增加缩进
if x < 0 :
   ## 2(3)
   print("x 小于 0")
   print("x 真的小于 0")
   if x < -5 :
    ## 3(4)
    pass
    print("x 小于 -5")
   ## 想结束一个代码块的时候，只需要去减少缩进就可以了
   print("x 小于 0 但是大于 -5")
elif x == 0 :
    pass
else :
    print("上面的条件都没满足")

# tab
    
    

print("已经跳出代码块")