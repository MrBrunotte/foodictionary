# Resources  https://docs.python.org/3/library/unittest.html ----------#
# To run the test: python test_unittest.py

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
os.getenv('SECRET_KEY', 'randomstring123')

mongo = PyMongo(app)

# VARIABLES -----------------------------------------------#
recipes = mongo.db.recipes
recipeCategory = mongo.db.recipeCategory
allergens = mongo.db.allergens
skillLevel = mongo.db.skillLevel
userDB = mongo.db.users


# Testing App Routes ---------------#
class TestApp(unittest.TestCase):

    def setUp(self):
        self.mongo = app.test_client()

# for tests to run the name needs to start with test_
    def test_that_routes_work_properly(self):
        # Test Homepage
        page = self.mongo.get('/home')
        self.assertEqual(page.status_code, 200)

        # Test Login
        page = self.mongo.get('/login')
        self.assertEqual(page.status_code, 200)

        # Test Register Page
        page = self.mongo.get('/register')
        self.assertEqual(page.status_code, 200)

        # Test Random recipe page
        page = self.mongo.get('/random_meal')
        self.assertEqual(page.status_code, 200)

        # Test 404 Error Page
        page = self.mongo.get('/test')
        self.assertEqual(page.status_code, 404)

        print('test-routes PASSED')


# Testing Registering a User and Removing the user -----------------------------------------------#


    def test_that_registration_works(self):
        response = self.mongo.post('/signup', data=dict(author_name='Author Name', username='test-user',
                                                        password='password', recipes_rated='1234'), follow_redirects=True)
        data = response.data.decode('utf-8')
        find_user = userDB.find_one({'username': 'test-user'})
        self.assertIsNotNone(find_user)
        print('test-user FOUND')
        delete_user = userDB.delete_one({'username': 'test-user'})
        print('test-user DELETED')


# Testing Deleting a Recipe -----------------------------------------------#


    def test_that_the_user_can_delete_a_recipe(self):
        response = self.mongo.post('/delete_recipe/5cff8ed42d609f1b9f4aa059')
        recipe = recipes.find_one(
            {'_id': ObjectId('5cff8ed42d609f1b9f4aa059')})
        self.assertIsNone(recipe)

        print('Recipe Deleted')


# Tidy Up after test -----------------------------------------------#


    def tearDown(self):
        sign_out = self.mongo.get('/logout')


# Run Tests -----------------------------------------------#

if __name__ == '__main__':
    unittest.main()
