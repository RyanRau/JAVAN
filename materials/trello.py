import requests
import json
import time

from config import *
from materials.models import *


def create_description(pk, url):
    order = Order.objects.get(pk=pk)
    members = OrderMember.objects.filter(order=order)

    # TODO: Add optional info about lesson start/end time

    order_num = str(order.number)
    order_owner = str(order.owner.first_name)

    if order.co_owner:
        order_co_owner = str(order.co_owner.first_name)
        card_name = "Order: " + str(order.number) + " - " + order_owner + " & " + order_co_owner
    else:
        card_name = "Order: " + str(order.number) + " - " + order_owner

    filled_url = "http://" + url + "/materials/order/" + order_num + "/status/4/0"
    # updated_url = "http://" + url + "/materials/order/" + order_num + "/status/3/0"
    out_url = "http://" + url + "/materials/order/" + order_num + "/status/6/0"
    returned_url = "http://" + url + "/materials/order/" + order_num + "/status/7/0"
    emptied_url = "http://" + url + "/materials/order/" + order_num + "/status/8/0"

    description = "Student Name: " + str(order.owner.first_name) + "\n" \
                  "Student Email: " + str(order.owner.email) + "\n" \
                  "Class: \n" \
                  + lesson_time + \
                  "[FILL](" + filled_url + ") [OUT](" + out_url + ") " \
                  "[RETURNED](" + returned_url + ") [EMPTIED](" + emptied_url + ")"
def create_checklist(pk, checklist_name):
    card_id = Order.objects.get(pk=pk).trello_card

    url = "https://api.trello.com/1/cards/" + card_id + "/checklists"
    querystring = {"name": checklist_name,
                   "key": trello_key,
                   "token": trello_token
                   }
    response = requests.request("POST", url, params=querystring)

    json_data = json.loads(response.text)
    check_id = json_data['id']
    return check_id

def fill_list(pk, check_id, self_fill):
    order = Order.objects.get(pk=pk)
    contents = OrderContent.objects.filter(order=order)

    for content in contents:
        if self_fill:
            checked = True
        else:
            checked = content.self_filled

        # adds item
        item = str(content.quantity) + " - " + content.item + " (" + content.location + "); "
        if content.other_notes:
            item = item + content.other_notes

        url = "https://api.trello.com/1/checklists/" + check_id + "/checkItems"
        querystring = {"name": item,
                       "pos": "bottom",
                       "checked": str(checked).lower(),
                       "key": trello_key,
                       "token": trello_token
                       }
        requests.request("POST", url, params=querystring)

def delete_labels(pk):
    card_id = Order.objects.get(pk=pk).trello_card

    url = "https://api.trello.com/1/cards/" + card_id + "/idLabels"
    querystring = {"key": trello_key,
                   "token": trello_token
                   }
    response = requests.request("GET", url, params=querystring)
    labels = json.loads(response.text)

    for label in labels:
        url = "https://api.trello.com/1/cards/" + card_id + "/idLabels/" + label
        requests.request("DELETE", url, params=querystring)

def add_label(pk, name, color):
    card_id = Order.objects.get(pk=pk).trello_card

    url = "https://api.trello.com/1/cards/" + card_id + "/labels"
    querystring = {"color": color,
                   "name": name,
                   "key": trello_key,
                   "token": trello_token
                   }
    requests.request("POST", url, params=querystring)
