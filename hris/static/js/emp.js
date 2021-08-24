$(function () {
    var loadForm = function () {
      var btn = $(this);
      $.ajax({
        url: btn.attr("data-url"),
        type: 'get',
        dataType: 'json',
        beforeSend: function () {
          $("#modal-emp .modal-content").html("");
          $("#modal-emp").modal("show");
        },
        success: function (data) {
          $("#modal-emp .modal-content").html(data.html_form);
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
            $("#emp-table tbody").html(data.html_emp_list);
            $("#modal-emp").modal("hide")
          }
          else {
            $("#modal-emp .modal-content").html(data.html_form);
          }
        }
      });
      return false;
    };

    // Create emp
  $(".show-form").click(loadForm);
  $("#modal-emp").on("submit", ".js-emp-create-form", saveForm);

  // Update emp
  $("#emp-table").on("click", ".show-form-update", loadForm);
  $("#modal-emp").on("submit", ".js-emp-update-form", saveForm);

  // Delete book
$("#emp-table").on("click", ".show-form-delete", loadForm);
$("#modal-emp").on("submit", ".js-book-delete-form", saveForm);


// Update Doc
$("#emp-table").on("click", ".show-form-update-doc", loadForm);
$("#modal-emp").on("submit", ".js-book-update-doc-form", saveForm);

});