import datetime
name = input("Enter your name: ")
print(f"Good Afternoon, {name}")

# Q2. letter = '''
#         Dear <|Name|>,
#         You are selected!
#         <|Date|>
# '''


letter = f'''
        Dear {name},
        You are selected!
        {datetime.datetime.now()}
'''

print(letter)

