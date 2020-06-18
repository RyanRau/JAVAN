var query = "";
var category = [];
var flag;

<!-- flag 0: order add list -->
<!-- flag 1: admin list -->
<!-- flag else: view only list -->
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

function refreshItems() {
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
        $("#content-list").html(resp);
    },
    error: function() {
    //      TODO: Add some error handling
    }
    });
}

