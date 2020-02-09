# **FOODictionary**

**FOODictionary** - Your personalized cookbook where you keep all your recipes!

The idea for this cookbook is to let you build your own cookbook with your favorite recipes. You can alos find other recipes that other users have added. There is a random recipe section when you want a quick inspiration for a meal to cook. There is a favorite section where you can store your favorite recipes.

## **UX**

This website is for anyone that likes to cook and want to have all their recipes in order in one place. The website have a simple layout with a navigation bar at the top where you can reach all the different sections. One can use the website as a registered user on a non-registered user. When one becomes registered there are additional feature for the user. The user can save recipes to a favorite section, add, edit or delete their own recipes.

The typical user is anyone that loves to cook and have their recipes in one place on the web.

### **FONTS**

The website uses two differnt fonts to create typographic harmony.
1) **[Lora](https://fonts.google.com/specimen/Lora)** - Headings
2) **[Ubuntu](https://fonts.google.com/specimen/Ubuntu)** - Body and buttons

### **WIREFRAME & MOCKUP**

I have used [AdobeXD](https://www.adobe.com/se/products/xd.html) as my tool for  the wireframe and mockup.

#### **Desktop**

#### **Mobile**

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

If the user clicks on [Lunch](http://foodictionary.herokuapp.com/browse_recipes/Lunch/1) the user is redirected to the "Lunch" page where the user can browse all the "lunch" recipes. The recipes are paginated and up to six recipes are displayed on each page, the user can easily navigate through the pages by clicking on "prev" or "next".

The user can also view an indiviual recipe by clicking on the image or "View Recipe" in each recipe card. The user is taken to the "Recipe" page where all the information for the specific recipe is shown. 

The user can also click on the different recipe tags to get redirected to recipes with the specific tag.

There is also an "ADD TO FAVORITE'S" button. If the user is a guest and not logged in the user will be directed to a page where the user is asked to either log in or register to add the recipe to their favorites.

#### Login

If the user clicks on [Login/Register](https://foodictionary.herokuapp.com/login) the user is directed to a login page where the user is able to log in or register as a new user.

When the user is logged in or Registered he/she is redirected back to the landing page and greated with a "toast" message that welcomes the user back.

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
