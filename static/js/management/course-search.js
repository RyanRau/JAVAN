var query = "";

function change(val) {
    query = val;
    getCourses();
}

function refreshCourses() {
    getCourses();
}

function getCourses(){
    $.ajax({
        type: 'GET',
        data: {
            query: query,
        },
        url: '/management/courses/api/course-search',

    success: function(resp) {
        $("#content-list").html(resp);
    },
    error: function() {
    //      TODO: Add some error handling
    }
    });
}

