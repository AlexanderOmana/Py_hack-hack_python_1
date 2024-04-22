"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    result = [1,2,3]
    result = []
    i = 0
    while i < len (result):
     result.append(result[i])
    if i < len (result) -1:
         result.append("@")
         i += 1
         print (result)
    return result  