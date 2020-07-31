var query = ""
var category = []

getItems("");

function filter(input){
    getItems(input.term.value);
    return false;
}

function change(val) {
    query = val;
    getItems();
}

function checkboxChange(){
    var checked = [];

    $("input[name='category[]']:checked").each(function () {
        checked.push($(this).val());
    });

    category = checked;
    getItems();
}

function getItems(){
    $.ajax({
        type: 'GET',
        data: {query: query,
               category: category},
        url: '/library/checkouts',

    success: function(resp) {
        $("#content-list").html(resp);
    },
    error: function() {
    //      TODO: Add some error handling
    }
    });
}