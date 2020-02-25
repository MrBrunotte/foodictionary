# **FOODictionary**

![alt text](https://github.com/AnthonyNicklin/meat-free/blob/master/app/static/images/white_logo.png "Meat Free Logo")

**FOODictionary - Your personalized cookbook!**

Foodictionary lets the user personalize their own special cookbook!

The idea for this website is to let the user build their own personalized cookbook. The registered user is able to add, edit and delete their own recipes they are also able to add their favorite recipes to a favoriets section.

The guest user is able to browse and search for recipes but to be able to use all the websites functionalities they need to become a registered user.

To get the best experiance and understanding of all features of the website, please register as a user and add some recipes. When you have registered and logged in you will be able to test all features of FOODictionary.

## **Database**

[MongoDB Atlas](https://www.mongodb.com/cloud/atlas) was used to create and store the values. 

FOODictionary uses the CRUD functions for the recipes, which was a requriement for this project:

* Create a recipe
* Read a recipe
* Update a recipe**
* Delete a recipe**

The database schema consists of a Database named Foodictionary with five collections: 

* allergens
* recipeCategory
* recipes
* skillLevel
* users

See the Schema here: **[DatabaseSchema](https://github.com/MrBrunotte/foodictionary/blob/master/planning/database_schema.jpg)**

See the Collections here: **[DatabaseCollections](https://github.com/MrBrunotte/foodictionary/blob/master/planning/collections.png)** 


## **UX**

This website is for anyone that likes to cook and want to have all their recipes in order in one place. The website have a simple layout with a navigation bar at the top where you can reach all the different sections. One can use the website as a registered user or as a non-registered user. 

When a user registers additional feature are unlocked for the user. The user will also have access to "My Account" where they can:

* Add a recipe
* Edit a recipe
* See thier favoriet recipes
* Logout

The typical user is anyone that loves to cook and want to have their recipes in one place on the web.

### **Fonts**

The website uses two differnt fonts to create typographic harmony.
1) **[Lora](https://fonts.google.com/specimen/Lora)** - For headings
2) **[Ubuntu](https://fonts.google.com/specimen/Ubuntu)** - For body and buttons

### **Wireframe & Mockup**

I have used [AdobeXD](https://www.adobe.com/se/products/xd.html) as my tool for the mockup.

#### **Desktop & Mobile**

See the [FOODictionary Mockup](https://xd.adobe.com/view/a0007d73-1f7d-4b10-765c-7b6cc300c5c0-d631/grid)



## **FEATURES**

FOODictionary is build to be user friendly and easy to use. The site can be used both by as a "guest" or "registered" user.

The "registered" user will have access to more features than the "guest" user.

The guest user will only be able to:

* search for recipes
* find a random meal suggestion.

The registered user will be able to:

* add a recipe
* edit a recipe 
* add their own recipes to a "favorite recipe's" list

### **Existing features**

#### **Navigation**

The navigation consist of a "logged in" navigation and a "guest" navigation.
The difference between the two is that when the user is logged in they will be able to reach the "my account" section.

There is a navigation row for larger screens and a "hamburger" menu for smaller screens.

The "guest" navigation consists of:

1) Home
2) Random Recipe
3) Recipe Category
4) Login/Register

When the user logs in, the "Login" navigation changes to "My Account" where the logged in user can reach:

5) Add Recipe
6) My Recipes
7) My Favorite Recipes
8) Logout

#### **Home**

The "home" navigation takes the user to the landing page:

When the user is on the landing page they can search for recipes by tags, keywords or categories.

#### **Random Recipe**

The "Random Recipe" navigation takes the user to the "Random Recipe Generator"

The user clicks on the "Generate Meal" button and is taken to a random recipe with written instructions and a video on how to prepare the meal. If the user wants another recipe they just click on the button again and a new random recipe will load.

#### **Recipe Category**

The "Recipe Category" navigation lets the user click on one of the six categories:

1) **Breakfast**
2) **Starter**
3) **Lunch**
4) **MainCourse**
5) **Dessert**
6) **Snack**

If the user clicks on **Lunch** the user is reredirected to the "Lunch" page where the user can browse all the "lunch" recipes. The recipes are paginated and up to six recipes are displayed on each page, the user can easily navigate through the pages by clicking on "prev" or "next".

The user can also view an indiviual recipe by clicking on the image or "View Recipe" in each recipe card. The user is taken to the "Recipe" page where all the information for the specific recipe is shown. 

The user can also click on the different recipe tags to get reredirected to recipes with the specific tag.

There is also an "ADD TO FAVORITE's" button of the user is logged in. If the user is a guest and not logged they will not see the "ADD TO FAVORITE's" button. The user can only add their own recipes to favorites.

#### Login

If the user clicks on **Login/Register** the user is redirected to a login page where the user is able to log in or register as a new user.

When the user is logged in or Registered he/she is redirected back to the landing page and greated with a "toast" message that welcomes the user back.

#### My Account

When the user is logged in or registered the user is able to access the "My Account" section where the user is able to navigate to:

1) Add Recipe
2) My Recipes
3) My Favorite Recipes
4) Logout

In this section the user is able to manage their own recipes. The user can add, update och delete a specific recipe. The user can also add a recipe to its list of favorite recipes that is located in the subsection "My Favorite Recipes"

This is also where the user logs out from the website.

#### **Future features**

*   **Personal account** - Where the user can update or change passwords, upload an personal image.
*   **Ineraction between users** - A blog section that lets the registered users blog about thier recipes, cooking etc.
*   **Reviews & Comments** - Let the registered users comment on other users recipes.
*   **Undo delete** - Let the user undo a deletion of a recipe by saving the deleted recipes in a "deleted_recipes" collection in the database.


## **TECHNOLOGIES USED**

This website is designed and runs using the technologies below:

   1) **[HTML](https://en.wikipedia.org/wiki/HTML)**
   2) **[CSS](https://www.w3schools.com/css/css_intro.asp)**
   3) **[JavaScript](https://en.wikipedia.org/wiki/JavaScript)**
   4) **[Python](https://www.python.org/)**
   5) **[Flask](https://flask.palletsprojects.com/en/1.1.x/)**
   6) **[MongoDB Atlas](https://www.mongodb.com/cloud/atlas)**
   7) **[jQuery](https://en.wikipedia.org/wiki/JQuery)**
   8) **[Materilize ver 1.0.0](https://materializecss.com/)**
   9) **[Google Fonts](https://fonts.google.com/)**
   10) **[Flaticon Freepik](https://www.flaticon.com/)**
   11) **[Visual Studio code](https://code.visualstudio.com/)**
   12) **[AdobeXd](https://www.adobe.com/products/xd.html?promoid=PYPVQ3HN&mv=other)**


## **TESTING**

### **Unittesting**

Automated testing was conducted by using Pythons built-in [Unit Testing Framework](https://docs.python.org/3/library/unittest.html). 

The "test case" was used which is the indivdual unit of testing. The "test case" checks for a specific response to a particular set of inputs.

I used three tests:

    1) Testing the routes:
        "Testing the routes" checked if the routes responded with "200 - route OK" and the correct response for my error route "404 - route not found".
    2) Register a user:
        "Registering a user" registered a "test-user", searched for the "test-user" and finally deleted the "test-user"
    3) Deleting a recipe: 
        "Deleting a recipe" deleted a hard-coded recipe and deleted it.

The test_unittest.py file started with a setUp() method that the testing framwork call for every single test that is run. The file then ends with a tearDown() method that tides up after the test method has been run.

### **Responsivness testing**

To test the responsivness of my sight I used the developer tool in both FireFox and Chrome. The responsive testing for mobile screens were made on:

* Iphone 5/SE IOS 10.3.1
* Iphnoe X/XS IOS 12
* Galaxy S9/S9+ Android 7.0

Responsive testing for mobile screens were made for both landscape and portrait.

### **Manual testing - User testing**

The manual testing on the website was conducted by testing each individual section on every page. The testing was conducted as a "new" user and also as an "old - registered" user with a username.

#### Navigation

Testing the navigation from each page and verify that it is working correctly and directing the user to the correct pages.

    1) Click on "Home" and verify that the user is reredirected back to the home page.
    2) Click on the "Random Recipe" and verify the the user is redirected to the random meal page.
    3) Click on the "Recipe Category" and verify that all categories redirect to its corresponding and correct category.
    4) Click on "Login/Register" and verfy that the user is taken to the login form. Click on "Register Here!" and verify that a new user is redirected to the register form.

#### Home

Home page features testing

    1) Click on tags to verify that the user is redirected to the correct recipes with the corresponding tag. Check that 20 random tags are loaded when home page is updated.
    2) Type search word in the search field and verify that the user is redirected to the correct category for that specific search word.
    3) Click on each catergory and verify that the user is taken to the correct category that corresponds with the anchor link (image). 

See the test flowchart: [Testpath Home](https://github.com/MrBrunotte/foodictionary/blob/master/testing/testpath_homePageFunctions.png)

#### Random Recipe

    1) Click on the "Generate Meal" button.
    2) Click on the video and verify that it runs properly.

See the test flowchart: [Testpath RandomRecipe](https://github.com/MrBrunotte/foodictionary/blob/master/testing/testpath_randomRecipe.png)

#### Recipe Category

Click on the "Recipe Category" dropdown and verify that all the categories are redirected to the correct category page.

When redirected to each category, verify that the category is matched with the correct category from the dropdown menu. 

    1) Check catergory name
    2) Check number of recipes
    3) Check pagingation and that it works when more than one page of recipes.
    4) Check visually that all recipes are displayed correctly.

    5) Click on the image to verify that the user is redirected to the corresponding recipe page.
    6) Click on the flashing plus-sign ("add to favorite recipes") and make sure that the "new" user is taken to the info page where the user can choose to register and then add the recipe to his/her favorite recipes.
    7) Click on "View recipe" and verify that the user is redirected to the correct recipe.

See the test flowchart: [Testpath RecipeCategory](https://github.com/MrBrunotte/foodictionary/blob/master/testing/testpath_category.png)

#### Login/Register

##### Register

    1) Verify that the user is redirected to the "Register form" when clicking on the "Register Here!" link.
    2) Verify that all fields are required in the form.
    3) Test register a new user and confirm that the user is registered and redirected to the "Landing Page"

##### Login

    1) Verify that the user is redirected to the "landing page" and greated by a toast message "Welcome Back "username" ".
    2) Verify that all navigation links, tags, search field and categories work.

See the test flowchart: [Testpath LoginRegister](https://github.com/MrBrunotte/foodictionary/blob/master/testing/testpath_loginRegister.png)

#### My account

Click on the "My account" dropdown menu and verify that the user is greeted with "Hello "username" "

##### Add recipe

   1) Click on "Add recipe" and fill in the form, all fields are required.
   2) Verify that the "Recipe Category", "Allergens" and "Difficulty" dropdown menues work.
   3) Verify that teh "Next Ingredient" and "Next Step" works.
   4) Verify that tags are working.
   5) Verify that the user can add the recipe to his/her favorite recipes.
   6) Verify that the recipe is added when submitting the recipe with the "Add Reciepe" button.
   7) Verify that the user is redirected to "My Reciepes".
   8) Verify that the added recipes is displayed correctly.

##### My recipes

   1) Verify the number of reciepes and pages match.
   2) verify that pagination work.
   3) Verify the layout of the page, that every recipe lines up properly.
   4) Verify that the "Add to favourite" plus-sign works and adds the recipe to "favorite recipes" when clicked.
   5) Confirm that only recipes added by the user is displayed.
   6) Click on an individual recipe and verify that the user is redirected to the correct recipe.
   7) Test the "Edit Recipe", "Add to favorite", "Delete Recipe" and tags and verify that they redirect correctly and work.

##### My favorite recipes

   1) Verify the number of reciepes and pages match.
   2) verify that pagination work.
   3) Verify the layout of the page, that every recipe lines up properly.
   4) Verify that the "Add to favourite" plus-sign works and adds the recipe to "favorite recipes" when clicked.
   5) Confirm that only recipes added by the user is displayed.
   6) Click on an individual recipe and verify that the user is redirected to the correct recipe.
   7) Test the "Edit Recipe", "Add to favorite", "Delete Recipe" and tags and verify that they redirect correctly and work.


##### Logout

    1) click on logout and verify that the user is logged out, redirected to the landingpage and a toas message "You are now logged out!" appears.

See the test flowchart: [testPath MyAccount](https://github.com/MrBrunotte/foodictionary/blob/master/testing/testpath_myAccount.png)

#### Error pages - 404, 405, 500

    1) Confirmed that the "Back to homepage" link worked and redirected the user back to the landingpage.

#### Issues found and fixes implemented

* **Issue:** images on some larger screensizes are a bit wide depending on the image source. 
* **Fix:** Not able to fix this problem.



## **DEPLOYMENT**

The web application was created using [VScode](https://code.visualstudio.com/), and the web application is deployed using Heroku. Git was used for version control and pushed to a remote repository hosted on GitHub.

See repository: [FOODictionary repository](https://github.com/MrBrunotte/foodictionary)

See Heroku app: [FOODictionary Heroku App](https://foodictionary.herokuapp.com/)

There are no differences between the deployed version and the development version.

### **How to deploy the code locally**

If you wish to run this code locally then please follow the instructions below.

1. Download the code from the Github repository from [here](https://github.com/MrBrunotte/foodictionary).
2. Click on _"Clone"_ or _"download then Download ZIP"_. This will download the code into a ZIP folder locally on your computer.
3. Uncompress the ZIP folder.
4. Create a virtual environment. Tutorial of how to create a virtual environment can be found 
[here](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/). 
5. Activate the virtual environment.
6. Install the necessary Python packages in the requirements.txt file.
    * ````pip freeze --local > requirements.txt````
7. [Create a secret key](https://miniwebtool.com/password-generator/) and set as environment variable.
    * MacOS and Linux ````export SECRET_KEY=<secret key>````
    * Windows ````set SECRET_KEY=<secret key>````
8. Tell Flask how to import the app.
    * MacOS and Linux ````export FLASK_APP=app.py````
    * Windows ````set FLASK_APP=app.py````
9. Connect your MongoDB database to the application. If you have not created a MongoDB database please follow the 
instructions under the heading [Create a MongoDB account](https://github.com/AnthonyNicklin/meat-free#create-a-mongodb-account).
    * Set MongoDB URI as environment variable.
        * MacOS and Linux ````export MONGO_URI=<mongo_uri>````
        * Windows ````set MONGO_URI=<mongo_uri>````
    * Create a database and five collections. Called:
      * **allergens**
      * **recipeCategory**
      * **recipes**
      * **skillLevel**
      * **users**

    * Set MongoDB database name as environment variable.
        * MacOS and Linux ````export MONGO_DBNAME=<mongo_DBNAME>````
        * Windows ````set MONGO_DBNAME=<mongo_DBNAME>````
1.  Open up a terminal and run ````flask run````.
2.  Navigate to the address the terminal returns to view **FOODictionary**.

### **Deploy to Heroku**

This project was deployed to Heroku and uses Heroku for its production environment. Instructions are below on how to 
deploy this web application to a production environment in Heroku.


*Git must be installed onto your computer. Instructions for installing Git can be found 
[here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

**Heroku CLI must be installed in order to deploy to Heroku using these instructions. Please follow the instructions 
here to download and install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli).

***You must have a MongoDB account and database setup with five collections.
Follow the instructions under the heading **create-a-mongodb-account** below.

1. Open up Heroku and navigate to your dashboard.
2. Select _New_ > _Create New App_ and fill out the details required then hit _Create App_.
3. Select _Settings_ > _Reveal Config Vars_
    * Enter in the following environment variables:
        * SECRET_KEY: the generated key
        * MONGO_URI: starts with: **mongodb+srv://**
        * MONGO_DBNAME: foodictionary
        * FLASK_APP: app.py
        * IP: 0.0.0.0
        * PORT:	5000
4. Download the code from the Github repository [here](https://github.com/MrBrunotte/foodictionary).
5. Click on _Clone_ or _download then Download ZIP_. This will download the code into a ZIP folder locally on your computer.
6. Uncompress the ZIP folder.
7. Open up a terminal or cmd prompt and login into Heroku CLI.
    * ````heroku login````
8. Check the app is present.
    * ````heroku apps````
9. A Procfile have already been created for this project but make sure that it is present. If for some 
reason it is not then follow the steps below to create it.
    
    * Procfile
        * In a terminal make sure you are in the root directory of the project then run ````echo web: python app.py > Procfile````.
        * Add the following text to the Procfile **web: python app.py runserver 0.0.0.0:5000**.
1.  Add a new git remote for Heroku.
    * ````git remote add heroku git@heroku.comYOUR_APP_NAME.git````
2.  Push to Heroku.
    * ````git push heroku master````
3.  Give Heroku a few minutes to get it all set up and then check the activity logs under Activity tab in your Heroku 
dashboard. 
13. Once the build is complete click on **open app** top right to see FOODictionary in action.

#### Create a MongoDB Account

The database used for this application is MongoDB Atlas and a free account can be created [here](https://www.mongodb.com/cloud/atlas).

1. Click on _Try Free_ top right
2. In the right hand panel complete the fields and complete verification steps required
3. Click on _Build a New Cluster_.
    * Select your preferred Cloud provider.
    * Select the region you wish to host and be sure to check the region is in the free tier.  
    * Select a Cluster Tier. Again be careful to select a free one if you wish to host this for free.
    * Select any additional settings you wish to set.
    * Give the Cluster a name.
    * Check settings then once happy select _Create Cluster_.
4. Click on _Collections_ > _Create Database_.
    * Give it a name (remember this as you will need the database name for import settings when deploying the code).
5. Click on _Create Collection_.  
    * Create five collections:
      * **allergens**
      * **recipeCategory**
      * **recipes**
      * **skillLevel**
      * **users**
6. Click on the _Overview_ tab then _Connect_.
    * Click on _Connect Your Application_.
    * Select the correct drive and version.
    * Copy and past the Connection String and keep this safe as you will need it for your MONGO_URI variable to deploy 
    the code.


## **CREDITS**

## Content

* All recipes and images are from [Allrecipes](https://www.allrecipes.com/)

* The random meal database is from [TheMealDB](https://www.themealdb.com/)
* Toastr JavaScript library from [Toastr](https://codeseven.github.io/toastr/)


## Acknowledgments

I would like to thank my good friend Niklas Lind for his support and guidance during the development of this project. 

I would also like to thank my mentor Maranatha Ilesanmi and the tutors at Code Institute for their help.


## Contact

Created by [Stefan Brunotte](mrbrunotte@gmail.com)
