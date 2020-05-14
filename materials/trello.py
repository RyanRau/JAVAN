import requests
import json
import time

from config import *
from materials.models import *


########################################################################################
# Creates/Updates & Populates Trello Cards
def create_and_populate(order_id, url, self_filled):
    card_id = create_card(order_id, url)
    check_id = create_checklist(card_id, "Items")
    fill_list(order_id, check_id, self_filled)
    return card_id


def update_and_populate(order_id, url, self_filled):
    update_card(order_id, url)
    order = Order.objects.get(pk=order_id)
    timestamp = time.strftime("%m-%d-%Y")
    check_id = create_checklist(order.trello_id, "Updated Items (" + timestamp + ")")
    fill_list(order_id, check_id, self_filled)


########################################################################################
# Creates Card
def create_card(pk, url):
    trello_url = "https://api.trello.com/1/cards"
    order = Order.objects.get(pk=pk)

    card_name = "Order: " + str(order.number)
    description = str(create_description(pk, url))

    querystring = {"name": card_name, "idList": materials_list_id, "keepFromSource": "all",
                   "desc": description,
                   "due": str(order.pickup_date) + " " + str(order.pickup_time),
                   "key": trello_key,
                   "token": trello_token}

    response = requests.request("POST", trello_url, params=querystring)

    json_data = json.loads(response.text)
    card_id = json_data['id']
    return card_id


# Updates card
def update_card(pk, url):
    order = Order.objects.get(pk=pk)

    trello_url = "https://api.trello.com/1/cards/" + order.trello_id

    card_name = "Order: " + str(order.number)

    querystring = {"name": card_name,
                   "desc": create_description(pk, url),
                   "due": str(order.pickup_date) + " " + str(order.pickup_time),
                   "key": trello_key,
                   "token": trello_token}

    requests.request("PUT", trello_url, params=querystring)


########################################################################################
# Helper Functions
# Generates card descriptions based given order and url
def create_description(pk, url):
    order = Order.objects.get(pk=pk)
    members = OrderMember.objects.filter(order=order)

    # TODO: Add optional info about lesson start/end time

    order_num = str(order.number)

    member_names = []
    member_emails = []
    for member in members:
        member_names.append(str(member.order_member.first_name))
        member_emails.append(str(member.order_member.email))

    filled_url = "http://" + url + "/materials/order/" + order_num + "/status/4/0"
    # updated_url = "http://" + url + "/materials/order/" + order_num + "/status/3/0"
    out_url = "http://" + url + "/materials/order/" + order_num + "/status/6/0"
    returned_url = "http://" + url + "/materials/order/" + order_num + "/status/7/0"
    emptied_url = "http://" + url + "/materials/order/" + order_num + "/status/8/0"

    description = "Course Information: " + order.course.name + order.course.teacher.first_name + " " + \
                  order.course.teacher.last_name + "\n" \
                  "Student Name(s): " + ', '.join(member_names) + "\n" \
                  "Student Email(s): " + ', '.join(member_emails) + "\n" \
                  "[FILL](" + filled_url + ") [OUT](" + out_url + ") " \
                  "[RETURNED](" + returned_url + ") [EMPTIED](" + emptied_url + ")"

    return description


# Creates checklist given checklist id & name; returns checklist id
def create_checklist(card_id, checklist_name):
    url = "https://api.trello.com/1/cards/" + card_id + "/checklists"
    querystring = {"name": checklist_name,
                   "key": trello_key,
                   "token": trello_token
                   }
    response = requests.request("POST", url, params=querystring)

    json_data = json.loads(response.text)
    check_id = json_data['id']
    return check_id


# Fills checklist given order, checklist id and whether order is self fill
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


# Deletes all labels from a card given the order
def delete_labels(pk):
    card_id = Order.objects.get(pk=pk).trello_id

    url = "https://api.trello.com/1/cards/" + card_id + "/idLabels"
    querystring = {"key": trello_key,
                   "token": trello_token
                   }
    response = requests.request("GET", url, params=querystring)
    labels = json.loads(response.text)

    for label in labels:
        url = "https://api.trello.com/1/cards/" + card_id + "/idLabels/" + label
        requests.request("DELETE", url, params=querystring)


# Creates label on card given order along with name and color of label
def add_label(pk, name, color):
    card_id = Order.objects.get(pk=pk).trello_id

    url = "https://api.trello.com/1/cards/" + card_id + "/labels"
    querystring = {"color": color,
                   "name": name,
                   "key": trello_key,
                   "token": trello_token
                   }
    requests.request("POST", url, params=querystring)


# Moves card position within list (top, bottom, etc...)
def move_card(pk, pos):
    order = Order.objects.get(pk=pk)

    url = "https://api.trello.com/1/cards/" + order.trello_idd

    querystring = {"idList": materials_archive_list_id,
                   "pos": pos,
                   "key": trello_key,
                   "token": trello_token}

    requests.request("PUT", url, params=querystring)


# Moves card to archive board
def archive(pk):
    order = Order.objects.get(pk=pk)

    url = "https://api.trello.com/1/cards/" + order.trello_id

    querystring = {"idList": materials_archive_list_id,
                   "idBoard": archive_board_id,
                   "key": trello_key,
                   "token": trello_token}

    requests.request("PUT", url, params=querystring)
