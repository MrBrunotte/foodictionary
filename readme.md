# **FOODictionary**

**FOODictionary** - Your personalized cookbook for all your recipes!

The idea for this cookbook is to let the user build their own cookbook with thier favorite recipes. The user can also find other recipes that other users have added. There is a random recipe section when the user want a quick inspiration for a meal to cook. There is a favorite section where user can store their favorite recipes.

FOODictionary uses the CRUD functions for the recipes:

    1) Create a recipe
    2) Read a recipe
    3) Update a recipe
    4) Delete a recipe

## **Database**

This project use [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) to create and store the values. The aim of this project was to use the CRUD functions to let the user interact with the database on the website.

The database schema consists of one Cluster with a Database named Foodictionary. 

The database Foodictionary consists of the five collections:

    1) allergens
    2) recipeCategory
    3) recipes
    4) skillLevel
    5) users

See the database schema for [Foodictionary](https://github.com/MrBrunotte/foodictionary/blob/master/planning/database_schema.jpg) here! 

## **UX**

This website is for anyone that likes to cook and want to have all their recipes in order in one place. The website have a simple layout with a navigation bar at the top where you can reach all the different sections. One can use the website as a registered user on a non-registered user. When one becomes registered there are additional feature for the user. The user can save recipes to a favorite section, add, edit or delete their own recipes.

The typical user is anyone that loves to cook and have their recipes in one place on the web.

### **Fonts**

The website uses two differnt fonts to create typographic harmony.
1) **[Lora](https://fonts.google.com/specimen/Lora)** - Headings
2) **[Ubuntu](https://fonts.google.com/specimen/Ubuntu)** - Body and buttons

### **Wireframe & Mockup**

I have used [AdobeXD](https://www.adobe.com/se/products/xd.html) as my tool for the mockup.

#### **Desktop & Mobile**

Link to [FOODictionary Mockup](https://xd.adobe.com/view/a0007d73-1f7d-4b10-765c-7b6cc300c5c0-d631/)

**When you have followed the link, click on FOODictionary at the top left corner to see all the mockups for desktop and mobile.**

## **FEATURES**

FOODictionary is build to be userfriendly and easy to use. The user is able to both register as a user with a personal section or the user can choose to use the site as a guest user. The guest user will only be able to look at recipes and find random recipes. The registered user will be able to interact with the site and save, edit and delete recipes. The logged in user will also be able to save recipes to a favorite section for quick and easy access.

### **Existing features**

#### **Navigation**

The navigation consistst of logged in navigation and a "guest" navigation.
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

[Home](https://foodictionary.herokuapp.com/home)

When the user is on the landing page they can search for recipes by tags, keywords or categories.

#### **Random Recipe**

The "Random Recipe" navigation takes the user to the "Random Recipe Generator": 

[RandomRecipe](https://foodictionary.herokuapp.com/random_meal) 

The user clicks on the "Generate Meal" button and is taken to a random recipe with written instructions and a video on how to prepare the meal. If the user wants another recipe they just click on the button again and a new random recipe will load.

#### **Recipe Category**

The "Recipe Category" navigation lets the user click on one of the six categories:

1) **[Brakfast](https://foodictionary.herokuapp.com/browse_recipes/Breakfast/1)**
2) **[Starter](https://foodictionary.herokuapp.com/browse_recipes/Starter/1)**
3) **[Lunch](http://foodictionary.herokuapp.com/browse_recipes/Lunch/1)**
4) **[MainCourse](https://foodictionary.herokuapp.com/browse_recipes/Main-Course/1)**
5) **[Dessert](https://foodictionary.herokuapp.com/browse_recipes/Dessert/1)**
6) **[Snack](https://foodictionary.herokuapp.com/browse_recipes/Snack/1)**

If the user clicks on [Lunch](http://foodictionary.herokuapp.com/browse_recipes/Lunch/1) the user is reredirected to the "Lunch" page where the user can browse all the "lunch" recipes. The recipes are paginated and up to six recipes are displayed on each page, the user can easily navigate through the pages by clicking on "prev" or "next".

The user can also view an indiviual recipe by clicking on the image or "View Recipe" in each recipe card. The user is taken to the "Recipe" page where all the information for the specific recipe is shown. 

The user can also click on the different recipe tags to get reredirected to recipes with the specific tag.

There is also an "ADD TO FAVORITE'S" button. If the user is a guest and not logged in the user will be redirected to a page where the user is asked to either log in or register to add the recipe to their favorites.

#### Login

If the user clicks on [Login/Register](https://foodictionary.herokuapp.com/login) the user is redirected to a login page where the user is able to log in or register as a new user.

When the user is logged in or Registered he/she is reredirected back to the landing page and greated with a "toast" message that welcomes the user back.

#### My Account

When the user is logged in or registered the user is able to access the "My Account" section where the user is able to navigate to:

1) Add Recipe
2) My Recipes
3) My Favorite Recipes
4) Logout

In this section the user is able to manage their own recipes. The user can add, update och delete a specific recipe. The user can also add a recipe to its list of favorite recipes that is located in the subsection "My Favorite Recipes"

This is also where the user logs out from the website.

### **Planning**

#### **MongoDB**

MongoDB is the database used in this project. 
I have created a database called "foodictionary" with the collections:

**[DatabaseSchema](https://github.com/MrBrunotte/foodictionary/blob/master/planning/database_schema.jpg)**

<!-- TODO MORE IN THIS SECTION!!!! -->

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

### **Manual testing**

The manual testing on the website was conducted by testing each individual section on every page. The testing was conducted as a "new" user and also as an "old - registered" user with a username.

#### **Navigation**

Testing the navigation from each page and verify that it is working correctly and directing the user to the correct pages.

    1) Click on "Home" and verify that the user is reredirected back to the home page.
    2) Click on the "Random Recipe" and verify the the user is redirected to the random meal page.
    3) Click on the "Recipe Category" and verify that all categories redirect to its corresponding and correct category.
    4) Click on "Login/Register" and verfy that the user is taken to the login form. Click on "Register Here!" and verify that a new user is redirected to the register form.

#### **Home**

Home page features testing

    1) Click on tags to verify that the user is redirected to the correct recipes with the corresponding tag. Check that 20 random tags are loaded when home page is updated.
    2) Type search word in the search field and verify that the user is redirected to the correct category for that specific search word.
    3) Click on each catergory and verify that the user is taken to the correct category that corresponds with the anchor link (image). 

[Testpath_Home](https://github.com/MrBrunotte/foodictionary/blob/master/planning/testpath_homePageFunctions.png)

#### **Random Recipe**

    1) Click on the "Generate Meal" button.
    2) Click on the video and verify that it runs properly.

[Testpath_RandomRecipe](https://github.com/MrBrunotte/foodictionary/blob/master/planning/testpath_randomRecipe.png)

#### **Recipe Category**

Click on the "Recipe Category" dropdown and verify that all the categories are redirected to the correct category page.

When redirected to each category, verify that the category is matched with the correct category from the dropdown menu. 

    1) Check catergory name
    2) Check number of recipes
    3) Check pagingation and that it works when more than one page of recipes.
    4) Check visually that all recipes are displayed correctly.

    5) Click on the image to verify that the user is redirected to the corresponding recipe page.
    6) Click on the flashing plus-sign ("add to favorite recipes") and make sure that the "new" user is taken to the info page where the user can choose to register and then add the recipe to his/her favorite recipes.
    7) Click on "View recipe" and verify that the user is redirected to the correct recipe.

[Testpath_RecipeCategory](https://github.com/MrBrunotte/foodictionary/blob/master/planning/testpath_category.png)

#### **Login/Register**

##### Register

    1) Verify that the user is redirected to the "Register form" when clicking on the "Register Here!" link.
    2) Verify that all fields are required in the form.
    3) Test register a new user and confirm that the user is registered and redirected to the "Landing Page"

##### Login

    1) Verify that the user is redirected to the "landing page" and greated by a toast message "Welcome Back "username" ".
    2) Verify that all navigation links, tags, search field and categories work.

[Testpath_LoginRegister](https://github.com/MrBrunotte/foodictionary/blob/master/planning/testpath_loginRegister.png)

#### **My account**

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

[testPath_MyAccount](https://github.com/MrBrunotte/foodictionary/blob/master/planning/testpath_myAccount.png)
