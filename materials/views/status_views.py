########################################################################################
# Changes status of order from Trello card

# Imports
from django.shortcuts import render, redirect, get_object_or_404

from materials.flows import *
from materials.trello import *
# from materials.txt_logger import *


########################################################################################
# order-status .../order/<int:pk>/status/<int:status_id>/<int:redir>/
def order_status(request, pk, status_id, redir):
    # order = Order.objects.get(pk=pk)
    url = request.META['HTTP_HOST']
    order_status_change(pk, status_id, url)

    if redir == 0:
        return render(request, 'materials/dead.html')
    elif redir == 1:
        return redirect('kiosk')
    elif redir == 2:
        return redirect('materials-index')
    else:
        return redirect('materials-index')


# Changes the label and status of an order, accounting for DONE/EMPTIED conditions
def order_status_change(order_id, status_id, url):
    statuses = ['ASSIGNED', 'STARTED', 'PLACED', 'UPDATED', 'FILLED', 'SELF-FILLED', 'OUT', 'RETURNED', 'EMPTIED',
                'DONE']

    order = get_object_or_404(Order, pk=order_id)
    current_status = order.status
    if order.status is not statuses[status_id]:
    # 2 Placed
        if status_id is 2:
            # Trello Card Creation
            card_id = create_and_populate(order_id, url, False)
            order.trello_id = card_id
    # 3 Updated
        if status_id is 3:
            update_and_populate(order_id, url, False)
            delete_labels(order_id)
            add_label(order_id, "UPDATED", "purple")
    # 4 Filled
        if status_id is 4:
            delete_labels(order_id)
            add_label(order_id, "FILLED", "yellow")
            sendEmail(str(order.owner.email),
                      "Your Order has been Filled!",
                      email_filled_message)
            if order.co_owner:
                sendEmail(str(order.co_owner.email),
                          "Your Order has been Filled!",
                          email_filled_message)
    # 5 Self Filled
        if status_id is 5:
            if current_status <= 1:  # Checks if order has been placed yet
                # Trello Card Creation
                card_id = create_and_populate(order_id, url, True)
                add_label(order_id, "SELF-FILLED", "yellow", card_id)
                order.trello_id = card_id
            else:
                update_and_populate(order_id, url, True)
                delete_labels(order_id)
                add_label(order_id, "SELF-FILLED", "yellow")
    # 6 Out
        if status_id is 6:
            delete_labels(order_id)
            add_label(order_id, "OUT", "orange")
    # 7 Returned
        if status_id is 7:
            delete_labels(order_id)
            add_label(order_id, "RETURNED", "red")
    # 8 Emptied
        # Once order is emptied it waits to be reactivated for the next teaching week, done will reset order status
        # and prepare order for reservations
        if status_id is 8:
            delete_labels(order_id)
            add_label(order_id, "EMPTIED", "black")
    # 9 Done
        if status_id is 9:


            delete_labels(order_id)
            add_label(order_id, "OUT", "orange")

        # # Checks if Order is ready to be marked as done
        # if (order.status is 'EMPTIED' and statuses[status_id] is 'DONE') or \
        #    (order.status is 'DONE' and statuses[status_id] is 'EMPTIED'):
        #     # Clears Order Content
        #     OrderContent.objects.filter(order=order).delete()
        #     log_append('Order ' + str(order.number) + ' has been cleared', 0)
        #
        #     delete_labels(order_id)
        #     create_label(order_id, "DONE", "blue")
        #
        #     # Archives card
        #     archive(order_id)
        #
        #     order.status = "ASSIGNED"
        #     order.trello_card = " "
        #     order.save()

        order.status = status_id
        order.save()

    # log_append('Order ' + str(order.number) + ': ' + statuses[status_id], 1)
