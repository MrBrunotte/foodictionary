# DEPENDENCIES --------------------------------------------#
import os
import pymongo
import math  # remove?
import random  # remove?
from flask import Flask, flash, render_template, redirect, request, url_for, request, session, g, abort
from flask_toastr import Toastr
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash

# CONNECT TO MONGODB DATABASE -----------------------------#

app = Flask(__name__)
toastr = Toastr(app)
app.config['MONGO_DBNAME'] = 'foodictionary'
# app.config['MONGO_URI'] = os.getenv('MONGO_URI', 'mongodb://localhost')
app.config['MONGO_URI'] = 'mongodb+srv://mrbrunotte:mrUSERbrunotte@foodictionary-gckbp.mongodb.net/foodictionary?retryWrites=true&w=majority'
app.secret_key = '9893869affbf35907d0e7f0f20a72bc9'
# Add secret key:   app.secret_key = os.getenv('SECRET', 'randomstring123')

mongo = PyMongo(app)

# VARIABLES -----------------------------------------------#
recipes = mongo.db.recipes
recipeCategory = mongo.db.recipeCategory
allergens = mongo.db.allergens
skillLevel = mongo.db.skillLevel
userDB = mongo.db.users


# HOMEPAGE ------------------------------------------------#
@app.route('/')
@app.route('/home')
def home():
    tags = recipes.distinct('recipe_tags')
    random.shuffle(tags)
    username = session.get('username')
    return render_template('home.html', recipes=recipes.find().sort('date_time',pymongo.DESCENDING), 
    recipeCategory=recipeCategory.find(), page=1, tags=tags)


@app.route('/get_recipes')
def get_recipes():
    return render_template('get_recipes.html', recipes = recipes.find().sort('date_time',pymongo.DESCENDING), 
                            recipeCategory=recipeCategory.find())


# RANDOM MEAL PAGE ----------------------------------------#
@app.route('/random_meal')
def random_meal():
    return render_template('random_meal.html')

# USER LOGIN AND REGISTRATION -----------------------------#
@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/signup', methods=['POST'])
def signup():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=30)
    author_name = request.form.get('author_name')
    username = request.form.get('username').lower()
    password = generate_password_hash(request.form.get('password'))
    session['username'] = username
    user = userDB.find_one({'username': username})

    if user is None:
        userDB.insert_one({
            'author_name': author_name,
            'username': username,
            'password': password
        })
        session['logged_in'] = True
        flash('Welcome to FOODictionary ' + author_name + '!', 'success')
        return render_template('home.html')
    else:
        session['logged_in'] = False
        flash('Username already exists, please try again.', 'warning')
    return register()


@app.route('/login')
def login():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('base.html')


@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username'].lower()
    password = request.form['password']
    session['username'] = username
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=30)
    user = userDB.find_one({'username': username})

    if not user:
        session['logged_in'] = False
        flash('User ' + session['username'] +
              ' is not registered. Please try again.', 'warning')
        return signin()
    elif not check_password_hash(user['password'], password):
        session['logged_in'] = False
        flash('Wrong Password, please try again.', 'warning')
        return signin()
    else:
        session['logged_in'] = True
        flash('Welcome back ' +
              user['author_name'].capitalize() + '!', 'success')
        return render_template('home.html')  # if login ok redirect to home


@app.route('/logout', methods=['GET'])
def logout():
    session['logged_in'] = False
    flash('You are now logged out!', 'success')
    return render_template('home.html')


# RECIPES SECTION #

# BROWSE RECIPE CATEGORIES --------------------------------#
# To find the different categories in the nav menu. #
@app.route('/browse_recipes/<recipe_category_name>/<page>', methods=['GET'])
def browse_recipes(recipe_category_name, page):
    tags = recipes.distinct("recipe_tags")
    random.shuffle(tags)
    # Count the number of recipes in the Database
    all_recipes = recipes.find({'recipe_category_name': recipe_category_name}).sort([('date_time', pymongo.DESCENDING),
                                                                                     ('_id', pymongo.ASCENDING)])
    count_recipes = all_recipes.count()

    # Variables for Pagination
    offset = (int(page) - 1) * 6
    limit = 6

    recipe_pages = recipes.find({'recipe_category_name': recipe_category_name}).sort([("date_time", pymongo.DESCENDING),
                                                                                      ("_id", pymongo.ASCENDING)]).skip(offset).limit(limit)
    total_no_of_pages = int(math.ceil(count_recipes/limit))

    return render_template('browse_recipes.html',
                           recipes=recipe_pages, recipeCategory=recipeCategory.find(), count_recipes=count_recipes, total_no_of_pages=total_no_of_pages,
                           page=page, recipe_category_name=recipe_category_name, tags=tags)


# ADD RECIPE's --------------------------------------------#
@app.route('/add_recipe')
def add_recipe():
    return render_template('add_recipe.html', recipes=recipes.find(), recipeCategory=recipeCategory.find(),
                           skillLevel=skillLevel.find(), allergens=allergens.find(), userDB=userDB.find())


@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    username = session.get('username')
    user = userDB.find_one({'username': username})
    # Request Recipe tags and split into array based on comma
    recipe_tags = request.form.get('recipe_tags')
    recipe_tags_split = [x.strip() for x in recipe_tags.split(',')]
    complete_recipe = {
        'recipe_name': request.form.get('recipe_name'),
        'recipe_description': request.form.get('recipe_description'),
        'recipe_category_name': request.form.get('recipe_category_name'),
        'allergen_type': request.form.getlist('allergen_type'),
        'recipe_prep_time': request.form.get('recipe_prep_time'),
        'recipe_cook_time': request.form.get('recipe_cook_time'),
        'recipe_serves': request.form.get('recipe_serves'),
        'recipe_difficulty': request.form.get('recipe_difficulty'),
        'recipe_image': request.form.get('recipe_image'),
        'recipe_ingredients':  request.form.getlist('recipe_ingredients'),
        'recipe_method':  request.form.getlist('recipe_method'),
        'date_time': datetime.now(),
        'author_name': user['username'],
        'ratings': [
            {'overall_ratings': 0.0,
             'total_ratings': 0,
             'no_of_ratings': 0
             }
        ],
        'recipe_tags': recipe_tags_split
    }
    recipes.insert_one(complete_recipe)
    return redirect(url_for('add_recipe'))


# MY RECIPE's (see my recipes.html) --------------------------------------------#
# Collects my recipes from DB #

@app.route('/my_recipes/<page>', methods=['GET'])
def my_recipes(page):
    username = session.get('username')
    user = userDB.find_one({'username': username})

    # Count the number of recipes in the Database
    all_recipes = recipes.find({'author_name': username}).sort(
        [('date_time', pymongo.DESCENDING), ('_id', pymongo.ASCENDING)])
    count_recipes = all_recipes.count()
    # Variables for Pagination
    offset = (int(page) - 1) * 6
    limit = 6
    total_no_of_pages = int(math.ceil(count_recipes/limit))
    recipe_pages = recipes.find({'author_name': username}).sort([("date_time", pymongo.DESCENDING),
                                                                 ("_id", pymongo.ASCENDING)]).skip(offset).limit(limit)

    return render_template('my_recipes.html',
                           recipes=recipe_pages.sort('date_time', pymongo.DESCENDING), count_recipes=count_recipes,
                           total_no_of_pages=total_no_of_pages, page=page, author_name=username, recipeCategory=recipeCategory.find())


# MY RECIPE (see my individual recipe in recipe.html) --------------------------------------------#
# Collects my individual recipe from DB #

@app.route('/recipe_page/<recipe_id>', methods=['GET'])
def recipe_page(recipe_id):
    username = session.get('username')
    logged_in = session.get('logged_in')
    user = userDB.find_one({'username': username})
    if not user:
        return render_template('recipe.html', recipe=recipes.find_one({'_id': ObjectId(recipe_id)}), recipeCategory=recipeCategory.find(), recipe_id=recipe_id,  page=1)
    else:
        return render_template('recipe.html', recipe=recipes.find_one({'_id': ObjectId(recipe_id)}),
                               recipeCategory=recipeCategory.find(), recipe_id=recipe_id,
                               user=user, page=1, page_title='FOODictionary - Recipe')


# EDIT RECIPE  --------------------------------------------#

@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    return render_template('edit_recipe.html', recipeCategory=recipeCategory.find(), 
            allergens=allergens.find(), skillLevel=skillLevel.find(), page=1, 
            page_title='Edit Recipe on Lemon & Ginger, Recipe Finder',
            recipes=recipes.find_one({'_id': ObjectId(recipe_id)}))
            
@app.route('/update_recipe/<recipe_id>', methods=['POST'])
def update_recipe(recipe_id):
    recipe_tags = request.form.get('recipe_tags')
    recipe_tags_split = [x.strip() for x in recipe_tags.split(',')]
    recipes.update( {'_id': ObjectId(recipe_id)},
        { 
            '$set':{
            'recipe_name': request.form.get('recipe_name'),
            'recipe_description': request.form.get('recipe_description'),
            'recipe_category_name': request.form.get('recipe_category_name'),
            'allergen_type': request.form.getlist('allergen_type'),
            'recipe_prep_time': request.form.get('recipe_prep_time'),
            'recipe_cook_time': request.form.get('recipe_cook_time'),
            'recipe_serves': request.form.get('recipe_serves'),
            'recipe_difficulty': request.form.get('recipe_difficulty'),
            'recipe_image' : request.form.get('recipe_image'),            
            'recipe_ingredients':  request.form.getlist('recipe_ingredients'),
            'recipe_method':  request.form.getlist('recipe_method'),
            'featured_recipe':  request.form.get('featured_recipe'),
            'recipe_tags': recipe_tags_split
            }
        })    
    return redirect(url_for('my_recipes',page=1, page_title='My Recipes at Lemon & Ginger, Recipe Finder'))       



# DELETE RECIPE  --------------------------------------------#

@app.route('/delete_recipe/<recipe_id>', methods=['POST'])
def delete_recipe(recipe_id):
    recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('my_recipes',page=1, page_title='My Recipes at Lemon & Ginger, Recipe Finder'))


# SEARCH KEYWORD  --------------------------------------------#

@app.route('/search_keyword', methods=['POST'])
def receive_keyword():
    return redirect(url_for('search_keyword', keyword=request.form.get('keyword'), page=1)) 
    
    
@app.route('/search_keyword/<keyword>/<page>', methods=['GET'])
def search_keyword(keyword, page):
    recipes.create_index([('recipe_name', 'text'), ('recipe_ingredients', 'text'), ('recipe_category_name','text')])        
    
    #Count the number of recipes in the Database
    all_recipes = recipes.find({'$text': {'$search': keyword}}).sort([('date_time', pymongo.DESCENDING), ('_id', pymongo.ASCENDING)]) 
    count_recipes = all_recipes.count()
    
    #Variables for Pagination
    offset = (int(page) - 1) * 6
    limit = 6
    total_no_of_pages = int(math.ceil(count_recipes/limit))
    
    recipe_pages = recipes.find({'$text': {'$search': keyword}}).sort([("date_time", pymongo.DESCENDING), 
                    ("_id", pymongo.ASCENDING)]).skip(offset).limit(limit)
                    
    return render_template('keyword_search.html', keyword=keyword, 
        search_results = recipe_pages.sort('date_time',pymongo.DESCENDING), 
        recipeCategory=recipeCategory.find(), count_recipes=count_recipes, 
        total_no_of_pages=total_no_of_pages, page=page, page_title='Search Results, Lemon & Ginger, Recipe Finder')


# SEARCH TAG  --------------------------------------------#

@app.route('/search_tag', methods=['GET'])
def receive_tag():
    return redirect(url_for('search_tag', keyword=request.form.get('tag'), page=1)) 
    
    
@app.route('/search_tag/<tag>/<page>', methods=['GET'])
def search_tag(tag, page):
    recipes.create_index([('recipe_tags', pymongo.ASCENDING)])
    #Count the number of recipes in the Database
    all_recipes = recipes.find({'recipe_tags': tag}).sort([('date_time', pymongo.DESCENDING), ('_id', pymongo.ASCENDING)]) 
    count_recipes = all_recipes.count()
    
    #Variables for Pagination
    offset = (int(page) - 1) * 6
    limit = 6
    total_no_of_pages = int(math.ceil(count_recipes/limit))
    
    recipe_pages = recipes.find({'recipe_tags': tag}).sort([("date_time", pymongo.DESCENDING), 
                    ("_id", pymongo.ASCENDING)]).skip(offset).limit(limit)
                    
    return render_template('tag_search.html', tag=tag, 
        search_results = recipe_pages.sort('date_time',pymongo.DESCENDING), 
        recipeCategory=recipeCategory.find(), count_recipes=count_recipes, 
        total_no_of_pages=total_no_of_pages, page=page)  

#-------------#
# Error Pages
#-------------#


# @app.errorhandler(404)
# def page_not_found(error):
#    return render_template('404.html',recipeCategory=recipeCategory.find(), page=1, page_title='404 Error Page, FOODictionary'), 404
# @app.errorhandler(500)
# def something_wrong(error):
# return render_template('500.html',recipeCategory=recipeCategory.find(), page=1, page_title='500 Error Page, FOODictionary'), 500
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=(os.environ.get('PORT')),
            debug=True)  # change to False when finished!
