from myapp import app
import json, plotly
from flask import render_template, request, Response, jsonify
from wrangling_scripts.wrangle_data import return_pass
import string
import random
@app.route('/')
@app.route('/index')

def index():
    return render_template('index.html')

@app.route('/', methods=['GET','POST'])
def my_form_post():
    variable = request.form['test']
    case1 = string.ascii_uppercase
    case2 = string.ascii_lowercase
    case3 = string.punctuation
    case4 = string.digits


    # In[4]:


    get_len = int(variable)


    # In[5]:


    #put each case into a list and puts them all together
    l = []
    l.extend(list(case1))
    l.extend(list(case2))
    l.extend(list(case3))
    l.extend(list(case4))

    print("Your password is: ",end="")
    print("".join(random.sample(l,get_len)))
    
    return render_template('index.html',test="".join(random.sample(l,get_len)))
    

    
    
if __name__ == '__main__':
    app.run()
    # test = request.form['test']
        # #secure password should contain a mix of uppercase, lowercase, symbols,numbers
    # case1 = variable.ascii_uppercase
    # case2 = variable.ascii_lowercase
    # case3 = variable.punctuation
    # case4 = variable.digits


    # # In[4]:


    # get_len = test


    # # In[5]:


    # #put each case into a list and puts them all together
    # l = []
    # l.extend(list(case1))
    # l.extend(list(case2))
    # l.extend(list(case3))
    # l.extend(list(case4))

    # print("Your password is: ",end="")
    # #we join a null variable with ramdomized variable from above and give it a length based on users input
    # print("".join(random.sample(l,get_len)))
    # # In[7]:
    # return render_template('index.html',test="".join(random.sample(l,get_len)))



# if __name__=="__main__":
    # app.run()
    # figures = return_figures()

    # # plot ids for the html id tag
    # ids = ['figure-{}'.format(i) for i, _ in enumerate(figures)]

    # # Convert the plotly figures to JSON for javascript in html template
    # figuresJSON = json.dumps(figures, cls=plotly.utils.PlotlyJSONEncoder)

    # return render_template('index.html',
                           # ids=ids,
                           # figuresJSON=figuresJSON)