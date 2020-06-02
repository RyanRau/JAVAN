var query = "";
var category = [];
var flag;

function setFlag(val) {
    flag = val;
    console.log(flag)
}

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
               category: category,
               flag: flag
              },
        url: '/materials/items',

    success: function(resp) {
        $("#item-list").html(resp);
    },
    error: function() {
    //      TODO: Add some error handling
    }
    });
}

