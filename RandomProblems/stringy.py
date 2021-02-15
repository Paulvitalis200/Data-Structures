# def stringy(size):
#     # Good Luck!
#     if size == 0:
#       return
    
#     output = []
#     output.append(1)
#     count = 0
#     for i in range(size-1):
#       if output[count] == 1:
#         output.append(0)
#         count += 1
#       else:
#         output.append(1)
#         count += 1

#     output_str = ''
#     for i in output:
#         output_str += str(i)


#     # print("Here:", output)
#     # print(output_str)
#     # # print(''.join(output))
    
#     # # return ''.join(output)

# stringy(3)


# def markdownparser(markdown):
#   split_str = markdown.split()
  
#   if len(split_str) <= 1:
#     return ''.join(split_str)
  
#   hashtags = split_str[0]
#   markdown_text = ' '.join(split_str[1:])

# #   if markdown_text.lower() != "header" or markdown_text.lower() != "smaller header":
# #     hashtags = ''.join(hashtags)
# #     markdown_text = hashtags + '' + markdown_text
  
#   count = 0
#   for i in range(len(hashtags)):
#       print(i)
#       count += 1
    
#   return "<h{0}>{1}</h{2}>".format(count, markdown_text, count)

def count_change(money,coins):
    count = 0
    for i in range(len(coins)):
      
      for j in range(i+1, len(coins)):
          if coins[i] + coins[j] == money:
              print(coins[i], coins[j])
              count += 1
    return count


print(count_change(4,[1,2]))