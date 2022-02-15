#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask
import joblib


# In[2]:


app = Flask(__name__)


# In[3]:


from flask import request,render_template

@app.route("/",methods = ["GET","POST"])
def index():
    if request.method == "POST":
        sugar = request.form.get("sugar")
        milk = request.form.get("milk")
        print(sugar,milk)
        model = joblib.load("CTaste")
        pred = model.predict([[float(sugar),float(milk)]])
        pred = pred[0]
        print(pred)
        s="The predicted taste is: " + str(pred)
        return(render_template("index.html", result=s))
    else:
        return(render_template("index.html", result = "Predict Chocolate Taste"))


# In[ ]:


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=1111)


# In[ ]:





# In[ ]:




