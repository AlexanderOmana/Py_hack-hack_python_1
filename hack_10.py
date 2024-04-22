"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    tex_original = "fooziman"
    result = [char.upper() if char.lower()in 'aeiou' else '0' if char == 'o' else '1' 
              if char == 'a' else '@' if char == 'i' else 
              char for char in tex_original]
    print(result)
 
    return tex_original  