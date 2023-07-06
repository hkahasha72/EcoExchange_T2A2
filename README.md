

## Identification of the problem you are trying to solve by building this particular app and Why is it a problem that needs solving?

The problem which i am attempting to solve by creating this API webserver is to fill in the lack of a convenient platform for people to sell or trade recyclable items and unwanted goods at reduced prices, such as wood that could be turned into a crib, or an out of style couch which could be turned into a dog bed. Many people have items they no longer need or want or may be in dire need of the spare change, then there are people who might be interested in those items and trade with others for items that may be just as valuable to another. However there is often a lack of a accessability or an actual platform specifically designed to cater to these needs. This app aims to bring people together whether your a newly wed couple who just mpved in together and are in need of furniture or whether someone has an DIY project that needs to be carried out, by providing a user-friendly interface in which sellers can list their recyclables or unwanted items, and buyers can easily find and purchase them at reduced prices.

for example if someone is buliding a usually expensive project such as an dinning table which can range from 200-300+ dollars one can use a platform such as this to purchase wood and devices needed at a cheaper price than it would be to buy the table desgin u have in mind or than buying the materials in store, these days people usually post a facebook status however some of their friends might not even live in the same state as them let alone have the specfic supplies that may be of use. hence why having accessibility to a platform such as this helps connect people who can benefit one another.

By developing this API webserver i hope to cater to the needs of those who face this issue of the inefficient disposal of reusable items and help promote the reuse of said items. The app fights for a sustainable lifestyle by making it easier for people to access and utilize second hand goods within their community whilst also allowing those to sustainabily rid of items they might no longer find use of, which would hopefully help in the reduction and the demand for new products and help those who may not have the funds to splurge on specfic items.

The app benefits both sellers and buyers as sellers are able to declutter their spaces whilst also making some money by listing their items for sale and buyers can find affordable options for items they need, fostering a culture of reusing and reducing waste.

## Installtion and set up

Step #1 Clone the repository: locate the folder to save the app, open a terminal, navigate to the wanted folder and then clone the repository from GitHub.

Step #2 Set up postgresql database: open code with vscode and open postgresql in the intergrated terminal by putting in and running the command “psql” 

   Create a new database using the this command:
  		      
         CREATE DATABASE eco;
  

   Connect to the newly created database:
 		  
      \c eco ;
 

   Create a user and then set a temporary password:
   
      CREATE USER user WITH PASSWORD 'password';
 

   Grant all privileges to the user created:
   		
      GRANT ALL PRIVILEGES ON DATABASE eco TO user;

Step #3 Virtual Environment + Dependencies: open another terminal create a virtual environment and activate it with the following commands:
   	   
         python3 -m venv .venv
   		
         . .venv/bin/activate 


  	Install the required packages by running:
		  pip install -r requirements.txt
	
Step #4 Configuration: rename the “.env.sample” file to “.env” then open the “.env” file and make sure to set the “DATABASE_URL” to connect to your postgresql database, example:

      DATABASE_URL=postgresql+psycopg2://user:password@127.0.0.1:5432/eco

   Set the “JWT_SECRET_KEY” to a secure secret key for JWT encryption.

Step #5 Create + Seed and run the Database: run the below commands in order to create, seed and run the database: 

      flask db create
      flask db seed
      flask run
      
      The application will be accessible at “127.0.0.1:5000” 


## Why have you chosen this database system. What are the drawbacks compared to Others?

The chosen database system for this application is postgresql which is a powerful and popular relational database management system, i had chosen it due to its suitability in supporting the requirements needed for my API web server app 'EcoExchange', with its ability to be efficient in the management of complex relational data structures, its strong data integrity, scalability and the wide range of community support that follows and would better help support my app. While it may need some initial configuration and may not match the performance of some no sql databases its drawbacks are outweighed by how suitable it is to the specific needs that i hope to be met in the creation of the application. Overall postgresql betters the developers experience by allowing for a smooth operation and also meets the functionality requirements of the my API app 'EcoExchange'. 

Postgresql offers multiple benefits which help with the construction of my application, such as providing a strong foundation for managing complex relational data structures which is a big pro when it comes to organizing and storing the information which is related to recyclable items, sellers and buyers as well as supporting the categorization of data into entities and the establishment of relationships between them. The structured and organized of the way data is stored in postgresql allows for an efficient query processing and the support when complex operations are needed to carried out whilst searching, listing and trading recyclable items. it also offers data integrity through the use of primary and foreign keys, normalization and data validation rules. This makes sure that there is accuracy/consistency of the data which is stored, which is important when it comes to maintaining the reliability of the recyclable trade and purchase platform. Scalability is another pro which postgresql offers as it allows my application to handle a growing number of users and items over time, postgresql can properly manage and process the growing dataset, allowing for optimal performance and responsiveness for devleopers.

Furthermore, Postgresql is an open source database system which caters to a large and active community, which ultimately means that there is a vast range of resources and community support available to developers who are working with postgresql. This support can help a great deal when it comes to soloving issues in the development, maintenance and troubleshooting aspect of my recycling buy and trade web server API app.

As it is important to explore the benefits, one must also consider the drawbacks of PostgreSQL in comparison to other database systems, One of the drawbacks when it comes to using postgresql is that it may need more initial configuration and setup in comparison to some alternatives. The installation and configuration processes might be considered a bit more complex, another drawback that needs to be taken into consideration is that even though postgresql is highly scalable, it might not give the same level of performance as some no sql databases when it comes to handling extremely large data sets or high speed data streams however, in the context of my app which handles recyclable trades and purchases which has data volume that may not reach such extreme levels postgresql is still sufficient to use for my app.

All in all, postgresql is a great choice for my application as its features have a great compatibility rate with my app data requirments, provides the needed management of relational data, ensures data integrity, offers scalability and has an active community. These qualities/features allow for postgresql to properly support the functionality requirements of the application which ultimately helps in enhancing the user experience and a smooth operation of the application and its drawbacks are outweighed by how suitable it is when meeting my specific requirements for the application.


## Identify and discuss the key functionalities and benefits of an ORM
An ORM also knonw as an object relational mapper is known as a valuable tool in object-oriented programming (OOP) which allows for a simpler communication between a programming language and a relational database, It acts as a bridge which helps/allows  developers to make alterations to objects indirectly to the database system, in accordance to my EcoExchange recycling buy/trade API web server app implementing an ORM offers multiple advantages.

### A break down of the key functionalities:
#### Object relational mapping:
One can define a User model in their app using ORM, which would map to the users table in the database, the attributes of the User class, such as “name” and “email” correspond to columns within the users table, similarly one is able to define models for other entities in their app like Post and Comment entities and establish the relationships between the entities with the use of ORM mechanisms like foreign keys.

#### Queries:
With the use of an ORM one is able to write high-level code in order to help the prefomrance of CRUD operations on the database. For example the use of a method such as ‘create_user()’ which inserts a new user record into the Users table without needing to write raw sql queries.

#### Relationship management:
By utilizing ORM relationships developers can specifically define how each item is associated like how a user and has multiple comments, this method allows for one to easily get posts which belong to a specific user without having to manually construct complex sql JOIN queries.

#### Data validation and sanitization/ better security:
The ORM provides tools to validate and sanitize data before sending it to the database, like how one can define validation rules for the email field within the User model in order to make sure that it follows the needed email format, ORM helps enforce the rules needed when creating or updating user records.

#### Transaction management:
ORM allows one to gather many database operations into one single transaction, for example if i added a transaction element to my app then when a new user adds a new item for purchase i would be able to wrap the database insertion and any associated updates within a transaction. If any operation fails the the ORM is able to automatically roll back the entire transaction in order to maintain consistency within data.

#### Data integrity and consistency:
On topic of data consistency proplerly utilising ORM's data validation features one is able to make sure that user input is properly validated and sanitized before it is stored in the database which ultimately helps maintain data integrity whilst also preventing security vulnerabilities which helps for a much more reliable and secure app. 

#### Database independence:
ORM can also allow one to smoothly switch between different database systems such as mysql and postgresql simply by altering the database connection configuration and the app remains unaffected since the ORM abstracts away the database-specific details which allows an easy migration or deployment process to various environments.

By utilizing an ORM such as SQLAlchemy i am able to allow for a connection between my application and the database without having to write raw SQL queries, instead i would be able to interact with the database using high level programming language constructs which would make the code more readable. As well as the ability to be able to reuse code by defining models or classes which represent the many entities in my app such as users, posts and messages etc. In addition an ORM like sqlalchemy is able to properly help with data validation and sanitization and makes handling relationships between entities a simpler process.


## Document endpoints for your API
Endpoint: /users
   * Method: POST
   * Identifier: create_user
   * Authentication: not required
   * Token: 
   * Description: creates a new user.
   * Error: returns an error if there's an issue creating the user, like some requires aren met such as a unique email.
   * Request Body: json object containing username and password.
   * Request Response: Returns a json object representing the newly created user.

Endpoint: /users/login
   * Method: POST
   * Identifier: login
   * Authentication: not required
   * Token: 
   * Description: logs a user in and then returns an access token.
   * Error: returns an error if the login credentials are invalid.
   * Request Body: json object which contains username and password.
   * Request Response: returns a json object containing the access token upon successful login.

Endpoint: /item_posts
   * Method: POST
   * Identifier: create_item_post
   * Authentication: required
   * Token: Bearer token
   * Description: creates a new item post.
   * Error: displays an error when the user is not authenticated or if there's an issue creating the post(ItemPost).
   * Request Body: json object containing title and content of the item post.
   * Request Response: returns a json object representing the newly created item post.


Endpoint: /comments
   * Method: POST
   * Identifier: create_comment
   * Authentication: required
   * Token: Bearer token
   * Description: creates a new comment on a post (ItemPost).
   * Error: Returns an error if there's an issue creating the comment.
   * Request Body: json object containing content and item_post_id of the comment.
   * Request Response: returns a JSON object representing the newly created comment.

Endpoint: /groups
   * Method: POST
   * Identifier: create_group
   * Authentication: required
   * Token: bearer token
   * Description: creates a new group.
   * Error: Returns an error if the user is not authenticated or if there's an issue creating the group.
   * Request Body: json object containing the name of the group.
   * Request Response: returns a JSON object representing the newly created group.



### An ERD for your app, describe your projects models in terms of the relationships they have with each other and Discuss the database relations to be implemented in your application
![ERD](docs/ERD.png)

Models are known as classes or structures which represent the entities or tables within a database, their role is to define the structure, its attributes and its relationships of the data that will be stored and accessed by the app. In my EcoExchange the models are defined with the use of sqlalchemy library (which is an ORM) tool, each model class represents a table in the database (e.g User model represents users) and the attributes of the class correspond to the columns in the table (e.g User has name, email, password etc), defining models allows  developers to better define the data schema and establish relationships between different entities.

The User model represents users within the app, It includes attributes like id, name, email. This model allows for storing and managing user information. It establishes a one to many relationship with the ItemPost and Comment models which means that a user is able to have multiple posts(ItemPosts) and comments associated with their account.
	Relationship Example:
	Hope commented “is this still avaliable?” on your post ‘metal poles’
	Hope replied “oh thanks, ill shoot you a messsage” under your comment 
	
However it can never display:
	Hope and Mahi commented “is this still avaliable?” on your post ‘metal poles’

Since only one user can belong to a comment 

The ItemPost model represents posts which are made by users, it contains attributes like id, title, description, user_id and created_at. This model is to store data about the posts that was created by user and includes the title, content and the user who created the post so that buyers know who to contact, it also establishes a one to many relationship with the Comment model, this allows for comments to be connected with a specific item post.
	Example:
	Post: Mahi posted in furniture ‘Leather couch’, “Leather couch is up for sell, any takers? Negotiable”, $87,
	Relationships Example: Hope commented “is this still avaliable?” on your post ‘metal poles’

The Comment model represents comments that are made by users on posts (ItemPost). It contains attributes like id, message, user_id, item_post_id and created_at. This model is stores the content of comments and links them to the matching user and item post. It establishes relationships with the User and ItemPost models, allowing for an easy retrieval of user information and item post details related to a specific comment.

The Group model represents groups within the app which people join in order to narrow down accessible items, It has attributes such as id, name and created_at. This model allows for the creation and management of groups within the system. It establishes a many to many relationship with the User model through the join table, allowing users to be associated with multiple groups and group can have multiple users.
	Relationship Example:
      Hope joined ‘VIC suburbs’ and ‘VIC suburbs d.i.y’ group
      Hope, Mahi, Kahasha have joined your group ‘VIC suburbs’

#### Category:
The Category model represents different categories which can be assigned to posts (ItemPosts) such as, reusable materials, electronics, furniture etc, It has a one to many relationship with ItemPost model which means that one Category can be connected to multiple posts (ItemPosts), however each post (ItemPost) can only belong to one Category, such as metal poles can only belong to reusable materials category rather than electronics.

#### Comment:
The Comment model represents comments that are made on posts (ItemPosts) such as “is this item still avavliable”, “is the price negotiable” etc, It has relationships with both the ItemPost and User models. There is a one to many relationship between ItemPost model and Comment model, which ultimately means that one post (ItemPost) is able to have multiple comments whilst each Comment belongs to a single post (ItemPost). There is also a one to many relationship with User and Comment showing that one User can make multiple comments and each Comment is connected with a single User.

#### Group:
The Group model represents a group of Users, in this app it could be the suburbs one lives in so that the materials are accessible or even for specfic uses such as “vintage collectors items”, “baby items”, “pet furniture/toys”, Group model has a many to many relationship with the User model through the UserGroup association table which means that multiple Users can be connected to multiple Groups and the relationship is facilitated by the UserGroup association table.

#### ItemPost:
The ItemPost model represents individual posts for items, like if you would want to sell something you would post what u want to sell, a description of it as well as a photo, how u would sell it (sell or swap), ItemPost has relationships with Category, User and Comment models. There is a one to many relationship between Category and ItemPost model, meaning that one Category can have multiple posts (ItemPosts) and each post (ItemPost) belongs a Category.

There is also a one to many relationship between User and ItemPost models which means that a User is able to create multiple posts (ItemPosts) whilst each post (ItemPost) is connected with a single User. Additionally there is a one to many relationship between ItemPost and Comment models which can mean that one ItemPost can have multiple comments whilst each Comment belongs to a single ItemPost.

#### PersonalMessage:
The PersonalMessage model represents personal messages sent between Users, such as a negotiation about prices or information about payments and even sharing information such as where to meet and how to transport the item, PersonalMessage has relationships with the User model through the sender and receiver fields. There is a one to many relationship between User and PersonalMessage models for both the sender and receiver associations, meaning that one User is able to send and receive multiple inbox messages (PersonalMessages) whilst each PersonalMessage has a single sender and receiver associated with it.

#### User:
The User model represents the individual users of the app, It has relationships connected with the ItemPost, Comment, PersonalMessage and Group models. There is a one to many relationship between User and ItemPost which indicates that one User is able to create multiple posts (ItemPosts) whilst each ItemPost is associated with a User, Similarly there’s a one to many relationship between User and Comment models meaning that one User can post/make multiple comments, while each Comment is connected with a User. There is a one to many relationship between User and PersonalMessage both as a sender and a receiver signifying that a User is able to send and receive multiple PersonalMessages whilst each PersonalMessage has a single sender and receiver associated with it, lastly there is a many to many relationship between User and Group which allows multiple Users to be a part of various Groups.




## Detail any third party services that your app will use
My EcoExchange recycling buy/trade API web server app, will be utilizing mutiple third party services in order to better enhance the functionality/performance of my application, these third party services help provide many different capabilities and integrations which contribute to the experience of the user, these are the third party services used:

#### Flask: 
Flask is a well known web framework in python which provides the needed foundation for building apps as it offers a light weight and flexible build which allows the oppurtunity for smooth development and deployment of web APIs. Flask provides the needed essential features like routing and request handling which are some fundamental components of the application.
      
      Simplified Example:
		Route: “@app.route('/user’, methods=['POST'])”
      The Handler function: “def create_user():”


#### SQLAlchemy and Flask_SQLAlchemy: 
Sqlalchemy is an open source sql tool kit and object relational mapping (ORM) library for Python, It helps make the interaction with the database easier by offering a high level interface for working with database models and the relations. Sqlalchemy allows for smooth communication between the app and underlying database system, making sure of smooth data storage and retrieval. Flask_sqlalchemy is an extension of flask which integrates sqlalchemy into the flask framework and provides access to additional functions whilst simplifying the configuration of sqalchemy within the flask app.
 	
      Simplified code example:
	   “db = SQLAlchemy(app)”
      The defining of database models are do able due to the use of sqlalchemys syntax = "class ItemPost(db.Model):"

#### Flask_Marshmallow: 
Flask_marshmallow is a light weight integration of Marshmallow library with flask, marshmallow is a powerful serialization/deserialization library for python which simplifies the process of complex data structure conversion (like databases) into formats like json. Flask_marshmallow allows for smooth and seamless serialization/deserialization process of data between the app and the API endpoints, making sure that data transfer and manipulation is being done efficiently.

#### Flask_JWT_Extended: 
Flask_JWT_extended is a flask extension which provides a json web token also know as JWT authentication used for securing API endpoints, it offers features like token generation, token verification and token based authentication which allows for secure access to protected routes in the app. Flask_JWT_extended betters the authentication and authorization capabilities of the API, which ultimately allow for a more secure user interaction and the protection of sensitive data.

The third party services listed play a great role in the development and operation of the app and help provide needed functionalities such as web framework, database management, serialization/deserialization and authentication, allowing for seamless integration and smooth handling of user requests and data.



## Describe the way tasks are allocated and tracked in your project
Task planning and tracking is important and a fundamental part of assesing that the needs of the project are better met without the feeling of being overwhelhemed which was an aspect which i have learned is very important when for projects even if one may seem to have an understanding of the project, ive utilised some agile methodology when dealing with the plannning and tracking progress of this project:

#### Task Planning:
This is done prior to starting the assignment as it helps set the pace of the assignment and better helps one to understand what requirements need to be met, how to meet them accordingly, ways thats can be done is by:
   *  Breaking down the project requirements into smaller tasks or as a checkmark
   *  Each task is defined with clear objectives such as “research information needed for R2, make sure to answer it accordingly and make sure to meet the rubric requirements by 10:30pm wednesday”
   * Tasks are then labeled prioritized based on their importance 

#### Task Tracking:
   * Using project management tools to track the progress (in this case Trello) in order to track the task that i need to complete and monitor my progress.
   * Personally i prefer to physically cross off and mark my task on paper for a better representation of how much ive accomplish and what more there is 

![Trello Board ](docs/P1.png)
![Trello Board ](docs/P2.png)
![Trello Board ](docs/P3.png)
![Trello Board ](docs/P4.png)
![Trello Board ](docs/P5.png)
![Trello Board ](docs/P6.png)
![Trello Board ](docs/P7.png)
![Trello Board ](docs/P8.png)
![Trello Board ](docs/P9.png)
![Trello Board ](docs/P10.png)    