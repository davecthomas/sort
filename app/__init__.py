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

app = Flask(__name__)
user_cli = AppGroup('admin')
ts = sort.TestSort()
parser = reqparse.RequestParser()


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


@app.cli.command('import_experts')
@click.argument('test_val')
def admin_import_experts(test_val):
    message = {
        'message': 'OK'
    }

    test = test_val == "true"
    print(f'Test mode: {test}')
    dict_return = {
        "sort_list": []
    }
    message["message"] = json.dumps(dict_return)

    return jsonify(message)

Bootstrap(app)
app.cli.add_command(user_cli)
