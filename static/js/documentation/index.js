// On load... Renders TOC
$.ajax({
    type: 'GET',
    url: '/documentation/extras/toc',
    success: function(resp) {
        document.getElementById("toc").innerHTML = resp;
    },
    error: function() {
    //      TODO: Add some error handling
    }
});

function getDocument(id){
    $.ajax({
    type: 'GET',
    url: '/documentation/documents/' + id,
    success: function(resp) {
        document.getElementById("content").innerHTML = resp;
    },
    error: function() {
    //      TODO: Add some error handling
    }
    });
    console.log(id)
}