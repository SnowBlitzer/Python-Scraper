from flask.ext.wtf import Form 
from wtforms import StringField, SelectField 
from wtforms.validators import DataRequired 

class ArticleSearch(Form): 
    article_name = StringField('article_name', validators=[DataRequired()])   
    news_site = SelectField('news_site', 
                            choices=[('bbc', 'BBC'), 
                                     ('any', 'Any'),
                                     ('fox', 'FOX', 'Fox'),
                                     ('Independent', 'independent'),
                                     ('guardian', 'Guardian')]) 
