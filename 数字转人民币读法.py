#将数字分成整数和小数部分
def divide(num):
  integer = int(num)
  fraction = round((num -integer)*100)
  return (str(integer),str(fraction))

# a = 123124.8374
# print(divide(a))
han_list = ['零','壹','贰','叁','肆','伍','陆','柒','捌','玖']
unit_list = ['拾','佰','仟']

def four_to_hansstr(numstr): #1234
  result = ""
  num_len = len(numstr) # 4
  for i in range(num_len):
    num = int(numstr[i])

    #最后一位数不为0 ，直接加在字符串末尾
    if i == num_len -1 and num != 0:
      result+=han_list[num]

    if num != 0 and i< num_len -1:
      result += han_list[num] + unit_list[num_len-2-i]
    else:
      if i+1 < num_len and numstr[i+1] != '0' :
        result += han_list[num]
      else:
        pass
      
  return result

# a = '345'
# print(four_to_hansstr(a))

def integer_to_str(num_str):
  str_len = len(num_str)
  if str_len > 12:
    print('数字太大，翻译不了')
    return
  elif str_len > 8:
    return four_to_hansstr(num_str[:-8])+"亿"+four_to_hansstr(num_str[-8:-4])+'万'+\
      four_to_hansstr(num_str[-4:])
  elif str_len > 4:
    return four_to_hansstr(num_str[:-4])+'万'+\
      four_to_hansstr(num_str[-4:])
  else:
    return four_to_hansstr(num_str)

num = float(input('请输入一个浮点数:'))
integer,fraction = divide(num)
jiao = int(fraction[0])
fen = int(fraction[1])


print(integer_to_str(integer)+"元"+han_list[jiao]+"角"+han_list[fen]+"分")
