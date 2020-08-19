from myapp import app
import json, plotly
from flask import render_template
#from wrangling_scripts.wrangle_data import return_pass

@app.route('/')
@app.route('/index')
def form1():
    return render_template('index.html')

@app.route('/',method=['GET', 'POST'])
def index():
    test = request.form['test']
        #secure password should contain a mix of uppercase, lowercase, symbols,numbers
    case1 = string.ascii_uppercase
    case2 = string.ascii_lowercase
    case3 = string.punctuation
    case4 = string.digits


    # In[4]:


    get_len = int(test)


    # In[5]:


    #put each case into a list and puts them all together
    l = []
    l.extend(list(case1))
    l.extend(list(case2))
    l.extend(list(case3))
    l.extend(list(case4))

    print("Your password is: ",end="")
    #we join a null string with ramdomized string from above and give it a length based on users input
    print("".join(random.sample(l,get_len)))
    # In[7]:
    return render_template('index.html',test="".join(random.sample(l,get_len)))



if __name__=="__main__":
    app.run()
    # figures = return_figures()

    # # plot ids for the html id tag
    # ids = ['figure-{}'.format(i) for i, _ in enumerate(figures)]

    # # Convert the plotly figures to JSON for javascript in html template
    # figuresJSON = json.dumps(figures, cls=plotly.utils.PlotlyJSONEncoder)

    # return render_template('index.html',
                           # ids=ids,
                           # figuresJSON=figuresJSON)