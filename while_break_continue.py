my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0

while len(my_list) > index:
  elem = my_list[index]
  index += 1
  if elem < 0:
      break
  elif elem > 0:
      print(elem)
      continue
