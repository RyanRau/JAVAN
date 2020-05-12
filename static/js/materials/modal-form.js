// Credit to https://github.com/sibtc/simple-ajax-crud
// https://simpleisbetterthancomplex.com/tutorial/2016/11/15/how-to-implement-a-crud-using-ajax-and-json.html

$(function () {
    var loadForm = function () {
      var btn = $(this);
      $.ajax({
        url: btn.attr("data-url"),
        type: 'get',
        dataType: 'json',
        beforeSend: function () {
          $("#modal-form .modal-content").html("");
          $("#modal-form").modal("show");
        },
        success: function (data) {
          $("#modal-form .modal-content").html(data.html_form);
        }
      });
    };

    var saveForm = function () {
      var form = $(this);
      $.ajax({
        url: form.attr("action"),
        data: form.serialize(),
        type: form.attr("method"),
        dataType: 'json',
        success: function (data) {
          if (data.form_is_valid) {
            // $("#book-table tbody").html(data.html_book_list);
            $("#modal-form").modal("hide");

            // Only redirects if available
            if (data.redirect_url !== undefined && data.redirect_url) {
              window.location.replace(data.redirect_url);
            }
          }
          else {
            $("#modal-form .modal-content").html(data.html_form);
          }
        }
      });
      return false;
    };

    // Updates list and save form
    var list_saveForm = function () {
      var form = $(this);
      $.ajax({
        url: form.attr("action"),
        data: form.serialize(),
        type: form.attr("method"),
        dataType: 'json',
        success: function (data) {
          if (data.form_is_valid) {
            $("#content-table tbody").html(data.html_content_list);
            $("#modal-form").modal("hide");

            // Only redirects if available
            if (data.redirect_url !== undefined && data.redirect_url) {
              window.location.replace(data.redirect_url);
            }
          }
          else {
            $("#modal-form .modal-content").html(data.html_form);
          }
        }
      });
      return false;
    };


/////////////////////// Modal Form Triggers //////////////////////////////////
  // Generic Form
    $(".js-form-load").click(loadForm);
    $("#modal-form").on("submit", ".js-form", saveForm);

    $("#modal-form").on("submit", ".js-form-listed", list_saveForm);


///////////////////////// Order Content Triggers ///////////////////////////////////
  // Add Listed Item
    $(".js-form-listed").click(loadForm);
    $("#modal-form").on("submit", ".js-listed-add-form", list_saveForm);
  // Add Unlisted Item
    $(".js-unlisted-add").click(loadForm);
    $("#modal-form").on("submit", ".js-unlisted-add-form", list_saveForm);

    // Generic Add form
    $(".js-generic-add").click(loadForm);
    $("#modal-form").on("submit", ".js-generic-add-form", list_saveForm);

  // Edit Item
    $("#content-table").on("click", ".js-content-edit", loadForm);
    $("#modal-form").on("submit", ".js-content-edit-form", list_saveForm);
  // Delete Item
    $("#content-table").on("click", ".js-content-delete", loadForm);
    $("#modal-form").on("submit", ".js-content-delete-form", list_saveForm);

});
