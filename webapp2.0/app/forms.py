from flask.ext.wtf import Form 
from wtforms import StringField, SelectField, SelectMultipleField 
from wtforms.validators import DataRequired 
from wtforms import widgets
#, CheckboxInput, ListWidget

class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class ArticleSearch(Form): 
    article_name = StringField('article_name', validators=[DataRequired()])
    news_site = MultiCheckboxField('news_site', choices=[('bbc_technology.json', 'BBC Technology'), ('bbc_health.json', 'BBC Health'), ('bbc_us_and_canada.json', 'BBC US/Canada'), ('bbc_world.json', 'BBC World'),('foxbusiness_markets.json', 'Fox Markets'),('foxbusiness_politics.json', 'Fox Politics'),('foxbusiness_technology.json', 'Fox Technology'), ('independent_americas.json', 'Independent Americas'), ('independent_business.json', 'Independent Business'), ('independent_gadgets-and-tech.json','Independent Technology'), ('independent_politics.json', 'Independent Politics'), ('independent_world.json','Independent World'),('theguardian_technology.json','The Guardian Technology'), ('theguardian_us-elections-2016.json','The Guardian US Politics'), ('theguardian_us-news.json','The Guardian US news'),('theguardian_world.json','The Guardian World') ]) 

   
    #news_site = SelectMultipleField('news_site', choices=[('bbc_technology.json', 'BBC Technology'), ('bbc_health.json', 'BBC Health'), ('bbc_us_and_canada.json', 'BBC US/Canada'), ('bbc_world.json', 'BBC World'),('foxbusiness_markets.json', 'Fox Business'),('foxbusiness_politics.json', 'Fox Politics'), ('any', 'Any')]) 
    
