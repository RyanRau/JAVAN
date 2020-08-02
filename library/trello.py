import requests
import json
import time

from config import *
from library.models import *


def create_and_populate_chk(checkout_id, url):
    card_id = create_card_chk(checkout_id, url)
    return card_id


def create_card_chk(pk, url):
    trello_url = "https://api.trello.com/1/cards"
    checkout = Checkout.objects.get(pk=pk)

    card_name = "Checkout: " + checkout.book.title
    description = str(create_description_chk(pk, url))
    querystring = {
        "name": card_name,
        "idList": library_list_id,
        "keepFromSource": "all",
        "desc": description,
        "due": checkout.return_date,
        "key": trello_key,
        "token": trello_token
    }
    response = requests.request("POST", trello_url, params=querystring)

    json_data = json.loads(response.text)
    card_id = json_data['id']
    return card_id


def create_description_chk(pk, url):
    checkout = Checkout.objects.get(pk=pk)

    checkin_url = "http://" + url + "/library/checkouts"

    description = "Book Title: " + checkout.book.title + \
                  "\nChecked out by: " + checkout.user_checkout.first_name + \
                  checkout.user_checkout.last_name + \
                  "\nCheck out date: " + str(checkout.checkout_date) + \
                  "\nDue date: " + str(checkout.return_date) + \
                  "\nEmail: " + checkout.user_checkout.email + \
                  "\nCheck in: " + checkin_url
    return description


def archive_chk(pk):
    checkout = Checkout.objects.get(pk=pk)

    url = "https://api.trello.com/1/cards/" + checkout.trello_id
    querystring = {
        "idList": library_archive_list_id,
        "idBoard": archive_board_id,
        "key": trello_key,
        "token": trello_token
    }
    requests.request("PUT", url, params=querystring)
