import pickle
mdl=pickle.load(open('assets/cancer1.sav','rb'))
a=mdl.predict([[0,5,1,1,2,1,3,1,1]])
print(a)
