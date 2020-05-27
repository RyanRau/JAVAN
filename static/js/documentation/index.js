// On load... Renders TOC
$.ajax({
    type: 'GET',
    url: '/documentation/extras/toc',
    success: function(resp) {
        document.getElementById("toc").innerHTML = resp;
    },
    error: function() {
        // TODO: Add some error handling
    }
});

files = []

function setFiles(param){
    files = param;
    console.log(files)
}

function getDocumentByPath(path, anchor){
    const id = files.indexOf(path);

    if (id > 0){
        getDocument(id);
        window.location.href = "#"+anchor;
    } else {
        console.log("File not found")
    }
}

function getDocument(id){
    $.ajax({
        type: 'GET',
        url: '/documentation/documents/' + id,
        success: function(resp) {
            document.getElementById("content").innerHTML = resp;
        },
        error: function() {
            // TODO: Add some error handling
        }
    });
}



