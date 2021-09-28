SIZE = 7
array = [[0]*SIZE]

for i in range(SIZE-1):
  array += [[0]*SIZE]

#orient代表绕圈方向
# 0代表向下 1代表向右 2代表向左 3代表向上
orient = 0
#将1~SIZE*SIZE的数字填写到二维表中

# j控制行索引 ，k控制列索引
j,k = (0,0)
for i in range(1,SIZE*SIZE + 1):
  array[j][k] = i

  if j+k == SIZE - 1:
    if j>k:
      orient = 1
    else:
      orient = 2
  elif k == j and k >= SIZE/2:
    orient = 3
  elif j == k-1 and k <= SIZE/2:
    orient = 0
  
  #根据方向来控制行索引、列索引的改变
  if orient == 0:
    j+=1
  elif orient == 1:
    k+=1
  elif orient == 2:
    k -= 1
  elif orient == 3:
    j-=1

for i in range(SIZE):
  for j in range(SIZE):
    print("%02d" % array[i][j],end = " ")
  print("")
