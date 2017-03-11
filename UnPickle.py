import pickle

f = open('clinton_Debate_1.p','rb')
my_dict = pickle.load(f)
f.close()

print(my_dict)
