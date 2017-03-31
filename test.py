import commentjson

s = """
  {
      //fsadfdsafdsaf
       "template": "fsdafdsaf"
  }
"""
print(commentjson.loads(s))