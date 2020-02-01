from flask import Flask
from flask_bootstrap import Bootstrap
import click
from flask import Flask
from flask.cli import AppGroup
from flask import current_app, render_template
from flask_restful import reqparse
from flask import jsonify
import json
import random
import requests
from app import sort
from app.inverted_index import InvertedIndex
from app.sort import get_random_digits, get_random_in_range
from app import search
from app import inverted_index

app = Flask(__name__)
user_cli = AppGroup('do')
ts = sort.TestSort()
parser = reqparse.RequestParser()
search = search.Search()

def get_page(args):
    if args.page is None:
        page = int(1)
    else:
        page = int(args.page)
        if not isinstance(page, int):
            page = int(1)
    return page


def get_pagesize(args):
    if args.pagesize is None:
        pagesize = int(15)
    else:
        pagesize = int(args.pagesize)
        if not isinstance(pagesize, int):
            pagesize = int(15)
    return pagesize


@app.route('/')
@app.route('/index')
def index():
    list_size = ts.list_size
    unsorted_list = [random.randrange(-1*list_size*50, list_size*50, 1) for i in range(list_size)]
    str_return = f'There are {ts.len_list} items:<br/>{unsorted_list} <br/>'
    sorted_list = ts.do_test(unsorted_list, True)
    str_return = str_return + f'Sorted list:<br/>{sorted_list}'

    return str_return


@app.cli.command('sort_list')
# @click.argument('test_val')
def sort_list():
    print(ts.s.selection_sort_2(get_random_digits(1000, 1000)))


@app.cli.command('bsearch_list')
@click.argument('find_me')
def bsearch_list(find_me):
    print(f'{find_me}')
    find_me = int(find_me)
    search_list_rand = get_random_digits(50, 50)
    generate_random_index = get_random_in_range(0, 50)
    search_list_rand[generate_random_index] = find_me
    sorted_list = ts.s.selection_sort_2(search_list_rand)
    print(f'Looking for {find_me} in {sorted_list}')
    return_tuple = search.binary_search_2(sorted_list, find_me, True)
    print(f'{return_tuple[0]},{return_tuple[1]}')

@app.cli.command('inverted_index')
@click.argument('find_me')
def inverted_index(find_me):
    i = InvertedIndex(['test_files/bible.txt'])
    dict_index_entry = i.search_index(find_me)
    if dict_index_entry is not None:
        # print(f'Found {find_me} {dict_index_entry[0].get_num_times_found()} times. Top location: {index_entry[0].get_top_location()}')
        print(f'Length {len(dict_index_entry)}')
    else:
        print(f'{find_me} was not found.')

Bootstrap(app)
app.cli.add_command(user_cli)
