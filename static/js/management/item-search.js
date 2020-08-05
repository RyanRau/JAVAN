//TODO: generalize or combine all these js files...
var query = "";

function change(val) {
    query = val;
    getItems();
}

function refreshCourses() {
    getItems();
}

function getItems(){
    $.ajax({
        type: 'GET',
        data: {
            query: query,
        },
        url: '/management/items/api/items-search',

    success: function(resp) {
        $("#content-list").html(resp);
    },
    error: function() {
    //      TODO: Add some error handling
    }
    });
}

