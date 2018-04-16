import urllib
from bs4 import BeautifulSoup
import json
import os

from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey
from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField


app = Flask(__name__)

port = int(os.getenv("PORT"))

#Conexao com Cloudant
serviceUsername = "e50789af-0965-4379-87c4-f7f145beccd0-bluemix"
servicePassword = "1c2d47b7c03356823da0a5354561ae268caa01f0620b3a8493dee3d447c72049"
serviceURL = "https://e50789af-0965-4379-87c4-f7f145beccd0-bluemix:1c2d47b7c03356823da0a5354561ae268caa01f0620b3a8493dee3d447c72049@e50789af-0965-4379-87c4-f7f145beccd0-bluemix.cloudant.com"

client = Cloudant(serviceUsername, servicePassword, url=serviceURL)
client.connect()


databaseLinks = "databaselinks"
myDatabaseLinks = client[databaseLinks]


Documents = myDatabaseLinks

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/urlcrawler', methods=['GET', 'POST'])
    
def urlcrawler():
    form = URLform(request.form)
    if request.method == 'POST' and form.validate():
        
       url = 'http://' + form.url.data
       nomeDoc = form.nomeDoc.data
       data = {'links': []}

       html = urllib.request.urlopen(url).read()
       soup = BeautifulSoup(html, "lxml")

       for link in soup.find_all('a'):
        if 'http' or 'https' in link.get('href'):
           listaLinks = link.get('href')         
           data['links'].append(listaLinks)

       arrayLinks = data['links']
       jsonDocument = { "tabela": nomeDoc, "links": arrayLinks}

       databaseLinks = "databaselinks"
       myDatabaseLinks = client[databaseLinks]

       listaLinksDoc = myDatabaseLinks.create_document(jsonDocument)

    return render_template('urlcrawler.html', form=form)

@app.route('/links')
def links():
    return render_template('links.html', documents = Documents)

class URLform(Form):
    url = StringField('http://', [validators.Length(min=1, max=200)])
    nomeDoc = StringField('Lista', [validators.Length(min=1, max=50)])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
