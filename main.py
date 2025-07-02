from llm import query_llama

with open("eligible2.txt", "r") as file:
    eligibility = file.read()

with open("user2.txt", "r") as file:
    userprofile = file.read()


query_llama(eligibility, userprofile)




