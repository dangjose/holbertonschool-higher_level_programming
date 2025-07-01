#!/usr/bin/python3
"""Task 2. Consuming and processing data from an API using Python"""

import requests
import csv


def fetch_and_print_posts():
    '''
        Fetches all posts from JSONPlaceholder and prints them.
    '''

    response = requests.get('https://jsonplaceholder.typicode.com/posts')

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])


def fetch_and_save_posts():
    '''
        Fetches all posts from JSONPlaceholder and saves them.

        Return:
            Structured list of dictionaries.
    '''

    response = requests.get('https://jsonplaceholder.typicode.com/posts')

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        data = response.json()
        post_dict = []
        for post in data:
            posts = {
                'id': post['id'],
                'title': post['title'],
                'body': post['body']
            }
            post_dict.append(posts)

        with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(post_dict)

        return post_dict
