getItems("");

function filter(input){
    getItems(input.term.value);
    return false;
}

function change(val) {
    getItems(val);
}

function getItems(input){
    $.ajax({
        type: 'GET',
        data: {query: input},
        url: '/materials/items',

    success: function(resp) {
        $("#item-list").html(resp);
    },
    error: function() {
    //      TODO: Add some error handling
    }
    });
}

