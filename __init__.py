import wolframalpha

input = raw_input("Whatsup: ")
app_id = '6PLLPG-TEU7A7WGGG'
client = wolframalpha.Client(app_id)

res = client.query(input)
# print res
# print res.results
answer = next(res.results).text

print answer
