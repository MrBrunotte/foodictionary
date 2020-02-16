# Resources  https://docs.python.org/3/library/unittest.html ----------#

# Import pre-requisites -----------------------------------------------#

import os
import pymongo
import math
import random
import unittest
from app import app
from flask import Flask, render_template, redirect, request, url_for, request, session, g, abort, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash


# Connect to external MongoDB database through URI variable hosted on app server.------------------------#

app.config['DEBUG'] = False
app.config['TESTING'] = True
app.config['WTF_CSRF_ENABLED'] = False
app.secret_key = '9893869affbf35907d0e7f0f20a72bc9'

mongo = PyMongo(app)

# VARIABLES -----------------------------------------------#
recipes = mongo.db.recipes
recipeCategory = mongo.db.recipeCategory
allergens = mongo.db.allergens
skillLevel = mongo.db.skillLevel
userDB = mongo.db.users


# Testing App Routes (for tests to run the name needs to start with test_ ---------------#
class TestApp(unittest.TestCase):

    def setUp(self):
        self.mongo = app.test_client()

    def test_routes(self):
        # Test Homepage
        page = self.mongo.get('/home')
        self.assertEqual(page.status_code, 200)

        # Test Random recipe page
        page = self.mongo.get('/random_meal')
        self.assertEqual(page.status_code, 200)

        # Test Register Page
        page = self.mongo.get('/register')
        self.assertEqual(page.status_code, 200)

        # Test Signup Page
        #page = self.mongo.get('/signup')
        #self.assertEqual(page.status_code, 200)

        # Test Login Page
        #page = self.mongo.get('/signin')
        #self.assertEqual(page.status_code, 200)

        # Test Key-Searchword page
        page = self.mongo.get('/keyword_search')
        self.assertEqual(page.status_code, 200)

        # Test Tag-Search page
        page = self.mongo.get('/tag_search')
        self.assertEqual(page.status_code, 200)

        # Test 404 Error Page
        page = self.mongo.get('/test')
        self.assertEqual(page.status_code, 404)

        print('All the tests passed')


# Testing Registering a User and Removing the user -----------------------------------------------#

    def test_successful_registration(self):
        response = self.mongo.post('/signup', data=dict(author_name='Author Name', username='testuser',
                                                        password='password', recipes_rated='1234'), follow_redirects=True)
        data = response.data.decode('utf-8')
        find_user = userDB.find_one({'username': 'testuser'})
        self.assertIsNotNone(find_user)
        print('User Found. Preparing for Deletion')
        delete_user = userDB.delete_one({'username': 'testuser'})
        print('User Deleted.')


# Testing Deleting a Recipe -----------------------------------------------#

    def test_deleting_a_recipe(self):
        response = self.mongo.post('/delete_recipe/5cff8ed42d609f1b9f4aa059')
        recipe = recipes.find_one(
            {'_id': ObjectId('5cff8ed42d609f1b9f4aa059')})
        self.assertIsNone(recipe)

        print('Recipe Deleted')


# Tidy Up after test -----------------------------------------------#

    def tearDown(self):
        sign_out = self.mongo.get('/logout')


# Run Tests -----------------------------------------------#
# Three ways to run the tests:
# 1) run with: python test_unittest.py
# 2) run in the terminal with "run code"
# 3) python -m unittest test_unittest.py


if __name__ == '__main__':
    unittest.main()
