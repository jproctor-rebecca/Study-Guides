This study guide should reinforce and provide practice for all of the concepts you have seen in the past week. It consists of written questions and coding exercises, both are equally important to prepare you for the sprint challenge as well as to be able to speak on these topics comfortably in interviews and on the job.

If you get stuck or are unsure of something remember the 20 minute rule. If that doesn't help, then research a solution with [Google](https://www.google.com) and [StackOverflow](https://www.stackoverflow.com). Only once you have exausted these methods should you turn to your Team Lead - they won't be there on your SC, or during an interview. That being said, don't hesitate to ask for help if you truly are stuck.

Have fun studying!

# Questions of Understanding
1. Define the following and give an example of an appropriate task for each:
	- Front-end:  Front end developers help build what users interact with and see.
	- Back-end:  Back end developers are focused on data, modeling, and the back end of a website. 
	- Full-stack:  A full stack developer does some or all of the above.
	- Database:  A database is an organized collection of data, generally stored and accessed electronically from a computer system. The database management system (DBMS) is the software that interacts with end users, applications, and the database itself to capture and analyze the data.

2. What is a decorator?
In object-oriented programming, the decorator pattern is a design pattern that allows behavior to be added to an individual object, dynamically, without affecting the behavior of other objects from the same class.

3. What is a route?
In internetworking, the process of moving a packet of data from source to destination. Routing is usually performed by a dedicated device called a router. Routing is a key feature of the Internet because it enables messages to pass from one computer to another and eventually reach the target machine.

4. Why do we want to separate our code into separate files when writing an application? Why not just one big file?
It is basic organization. Imagine a library would glue every new book to a stack of the old ones.   If every file serves only one topic, you know quickly where to look. You also immediately know what does not belong to the topic, without having to read through commentary.  Multiple files allow for non-linear organisation. The building blocks of a program rarely follow a single, linear chain of interactions.  Loosely coupled components are easily represented by individual files, and folders allow to add external structure.  Distinct files are easier to reorganise.  As complexity grows, components move to sub packages, and sometimes you just need to clean up. A file can simply be moved as a whole.  Copy/Pasting to migrate code is more work, especially if you have tacked on all the structuring manually.  Individual files are easier to track.  Code is ideally in a version control system.  Knowing that backend/datastore/fileio.cpp changed is already quite informative, and lets you know whether the change is relevant for you.  If everything is a single file, you get line 254–378 in app.cpp changed, and have to look up the context yourself.

Basically, a single file is easy to write. Multiple files are much easy to read, maintain and manage. For software development, the later is much more important.  Even if you are working alone, future-you does not know everything that past-you has done.

5. What is an API? Give an example of an API that is not Twitter's.
API stands for Application Programming Interface.  An API is a software intermediary that allows two applications to talk to each other.  In other words, an API is the messenger that delivers your request to the provider that you're requesting it from and then delivers the response back to you.
Most APIs require an API key. ...
The easiest way to start using an API is by finding an HTTP client online, like REST-Client, Postman, or Paw. ...
The next best way to pull data from an API is by building a URL from existing API documentation.

6. What does it mean to pickle a model? Why might this be useful?
Pickle is the standard way of serializing objects in Python.  You can use the pickle operation to serialize your machine learning algorithms and save the serialized format to a file.  Later you can load this file to deserialize your model and use it to make new predictions.
Python pickle module is used for serializing and de-serializing a Python object structure.  Any object in Python can be pickled so that it can be saved on disk.  What pickle does is that it “serializes” the object first before writing it to file.  Pickling is a way to convert a python object (list, dict, etc.). 
This is important because it means you can save a Python object like a class instance to a file, send it to another environment or computer, and deserialize it back into a Python object to be interacted with again.

# Basics of Flask

## Coding
Write a Flask application that displays "Hello World!" to the local host (usually `127.0.0.1:5000` or `localhost:5000`)

## Questions of Understanding
1. Flask is described as a "microframework" for developing web applications. What is a "microframework"?
A web framework (WF) or web application framework (WAF) is a software framework that is designed to support the development of web applications including web services, web resources, and web APIs.  A microframework is a term used to refer to minimalistic web application frameworks.  It lacks most of the functionality which is common to expect in a full-fledged web application framework, such as: Accounts, authentication, authorization, roles. Database abstraction via an object-relational mapping.

2. What is another web development framework in Python?
A Web framework is a collection of packages or modules which allow developers to write Web applications (Web Applications) or services without having to handle such low-level details as protocols, sockets or process/thread management.  Django, a free and open-source Python framework, enables developers to develop complex code and apps quickly.  Django framework assists in developing quality web applications.  It is among the best python frameworks and is used for the quick development of APIs and web applications.

3. In this line of code: `APP = Flask(__name__)` What does `__name__` do?
__name__ is just a convenient way to get the import name of the place the app is defined. Flask uses the import name to know where to look up resources, templates, static files, instance folder, etc. app instead of mypackage.

4. What line of your code tells when and where "Hello World!" should be displayed?


5. What do we need to type into the terminal to run our flask application?
FLASK_APP=<directoryname> flask run

# API's

## Coding
API's are a common part of programming, whether setting up your own or using someone else's. Today we will be looking at the API for the board gaming hobby site BoardGameGeek (BGG). The API instructions can be found [here](https://boardgamegeek.com/wiki/page/BGG_XML_API&redirectedfrom=XML_API#). There are many wrappers online for the BGG API that you may use but the sample code below will use `requests` and the web scraping library `BeautifulSoup`.

```python
import requests
import bs4

game_id = 13
url = 'https://www.boardgamegeek.com/xmlapi/boardgame/' + str(game_id)
result = requests.get(url)
soup = bs4.BeautifulSoup(result.text, features='lxml')

print(soup.find('name').text)
```

The code above uses the API to search for a game by its ID number (more than 16,000 entries on BGG). Once the API returns the results, BeautifulSoup is used to parse the XML and make it easily searchable.

Explore the BGG API and see if you are able to find the following information about a game:

* Name
* Max and Min Players
* Play Time
* Game Description
* Some of the game mechanics

# Flask and Databases

## Code
Write a Flask web application using `SQLAlchemy` with the following:
- [ ] A home route that displays at least one entry from a database of stored BGG game information

  

- [ ] A dynamic route `/add/<game_id>` that adds game information into your database based on the ID in the route.

  

- [ ] A route that resets the database

  

- [ ] The database should have the following following columns as a minimum: id (integer), name (string), and max_players (integer)

## Questions of Understanding
1. What line of code establishes what database should be used for your application?

   

2. How do we define our table, what columns are going to be in it, and what those column datatypes are?

   

3. How do we make a query to our database?

# HTML Templates

## Code
- [ ] Create a small HTML template to display all the games in your database. Update your home route to use this template.

## Questions of Understanding
1. What is an HTML template?
A website template is a pre-built website composed of HTML pages that include integrated images, text content and support files for font styles and Javascripts.  Web templates and website templates are the same thing.  An HTML web template may be built using HTML or XHTML and will include CSS and Javascript code.

   

2. What module do we need to import from `flask` to use our HTML template?

# Heroku

## Code
It is not necessary, but you can try putting your application on Heroku.

## Questions of Understanding
1. What is a platform-as-a-service?
Platform as a service (PaaS) or application platform as a service (aPaaS) or platform-based service is a category of cloud computing services that provides a platform allowing customers to develop, run, and manage applications without the complexity of building and maintaining the infrastructure typically associated with developing and launching an app.
   

2. Why do we need to use a service like Heroku? Why not just host the application on our local machine?
They have the ability to automate processes and provide all the building blocks for companies in need of a full-service package.  Perhaps one of the most important reasons for looking at PaaS is the potential business advantages they can provide.  PaaS allow companies to be very agile and responsive to issues or demand.