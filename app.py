#!/usr/bin/env python
# coding: utf-8

# In[23]:


from flask import Flask
app = Flask(__name__)


# In[28]:


from flask import request, render_template
import joblib import load


# In[29]:


@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        income = request.form.get("income")
        age = request.form.get("age")
        loan = request.form.get("loan")
        print(income, age, loan)
        model=joblib.load("default_pred")
        pred=model.predict([[float(income),float(age),float(loan)]])
        s="The predicted default score is" + str(pred)
        return(render_template("index.html",result=s))
    else:
        return(render_template("index.html",result="Error"))


# In[ ]:


app.run()


# In[ ]:




