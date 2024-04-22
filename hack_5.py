"""
text: "fooziman" output => "f00z1m@n"
"""

def fn_hack_5():
   fn_hack_5 = "fooziman"
fn_hack_5 = fn_hack_5.replace('o', '0').replace('i', '1').replace('a', '@')
print(fn_hack_5)
