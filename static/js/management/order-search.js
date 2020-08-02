var query = "";

function change(val) {
    query = val;
    getOrders();
}

function refreshOrders() {
    getOrders();
}

function getOrders(){
    $.ajax({
        type: 'GET',
        data: {
            query: query,
        },
        url: '/management/orders/api/order-search',

    success: function(resp) {
        $("#content-list").html(resp);
    },
    error: function() {
    //      TODO: Add some error handling
    }
    });
}

