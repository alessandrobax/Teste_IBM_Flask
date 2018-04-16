# Teste_IBM_Flask

Feito por Alessandro Bax 
-abax@br.ibm.com
-alessandrobaxba@gmail.com
-tel: (31)98240-8504

-----------------------------------------------------------------------

Teste Técnico
As a Software Analyst, I want to collect web links (URL's) from a given initial web link (URL)
- The app needs to receive an URL;
- The app needs to find all links inside this given URL;
- The app needs to save this links found in database (SQL or No-SQL)
- The app needs listing this links saved in the database.

Please, as an extra effort, include in your solution the following:
- Your code needs to be integrated with git on your GitHub personal profile;
- Your code needs to contain unit testing;
- Your code needs to be served on the IBM Cloud;
- Your code needs to run with containers, with in IBM Cloud;

------------------------------------------------------------------------

Comentários:
A aplicação foi desenvolvida com Python, Flask, Bootstrap e IBM Cloudant(No-SQL db).
Ela está disponível no link: http://app-alessandro.mybluemix.net/

Obs: A estrutura do teste unitário foi criada, mas não foi implementada, pois não consegui terminar no prazo.
A aplicação foi hospedada na IBM Cloud.

-------------------------------------------------------------------------

Para testar em localhost:

 - Instale Python 3 /
 - No terminal digite o comando: pip install -r requirements.txt /
 - No terminal digite o comando: python app.py /
 
-------------------------------------------------------------------------

Para rodar a aplicação em container:

 - Acesse a pasta cf-py
 - No cluster (Kubernet) faça o upload do arquivo cf-py.yaml

-------------------------------------------------------------------------

Para publicar na IBM Cloud:

 - cf login
 - cf push :)




