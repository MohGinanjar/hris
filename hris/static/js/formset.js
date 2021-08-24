

function updateElementIndex(el, prefix, ndx) {
  var id_regex = new RegExp('(' + prefix + '-\\d+-)');
  var replacement = prefix + '-' + ndx + '-';
  if ($(el).attr("for")) $(el).attr("for", $(el).attr("for").replace(id_regex,
    replacement));
  if (el.id) el.id = el.id.replace(id_regex, replacement);
  if (el.name) el.name = el.name.replace(id_regex, replacement);
}





function addForm(btn, prefix) {
  var formCount = parseInt($('#id_' + prefix + '-TOTAL_FORMS').val());
  if (formCount < 10) {
    // Clone a form (without event handlers) from the first form
    var row = $(".item:last").clone(false).get(0);

    // Insert it after the last form
    $(row).removeAttr('id').hide().insertAfter(".item:last").slideDown(300);


    // Remove the bits we don't want in the new row/form
    // e.g. error messages
    $(".errorlist", row).remove();
    $(row).children().removeClass("error");

    // Relabel or rename all the relevant bits
    $(row).find('.formset-field').each(function () {
      updateElementIndex(this, prefix, formCount);
      $(this).val('');
      $(this).removeAttr('value');
      $(this).prop('checked', false);

    });

    $(row).find('.date-picker.formset-field').each(function (i, value) {
      $(value).datepicker({
        autoclose: true,
        todayHighlight: true
      });
    });


    $(row).find('.selecttype_trip.formset-field').each(function (i, value) {
      $(value).select2({
        allowClear: true,
      });
    });


    $(".selecttype_trip.formset-field").last().next().next().remove();

    $(row).find('.selecttype_city.formset-field').each(function (i, value) {
      $(value).select2({
        allowClear: true,
      });
    });


    $(".selecttype_city.formset-field").last().next().next().remove();

    $(row).find(".selectinputfile.formset-field").last().next().remove();

    $(row).find('.selectinputfile.formset-field').each(function (i, value) {
      $(value).ace_file_input({
        style: 'well',
        btn_choose: 'Invoice Input Here|.jpg',
        btn_change: null,
        no_icon: 'ace-icon fa fa-cloud-upload',
        droppable: true,
        thumbnail: 'small',
        onchange: null,
        maxSize: 1000000, //~100 MB
        allowExt: ['jpg', 'jpeg', 'png', 'gif', 'tif', 'tiff', 'bmp'],//large | fit
        //,icon_remove:null//set null, to hide remove/reset button
        /**,before_change:function(files, dropped) {
          //Check an example below
          //or examples/file-upload.html
          return true;
        }*/
        /**,before_remove : function() {
          return true;
        }*/

        preview_error: function (filename, error_code) {
          //name of the file that failed
          //error_code values
          //1 = 'FILE_LOAD_FAILED',
          //2 = 'IMAGE_LOAD_FAILED',
          //3 = 'THUMBNAIL_FAILED'
          //alert(error_code);
        }

      }).on('change', function () {
        console.log($(this).data('ace_input_files'));
        console.log($(this).data('ace_input_method'));
      });
    });

    

    $(row).on('keyup', function (ev) {
      var price = $('#start_km').val();
      var qty = $('#end_km').val();
      var gst = $('#bdl_perkm').val();
      var reeta = qty - price;
      var tot_price = reeta * gst;
      $('#total_bdl_perkm').val(tot_price);
    });


    // Add an event handler for the delete item/form link
    $(row).find(".delete").click(function () {
      return deleteForm(this, prefix);
    });
    // Update the total form count
    $("#id_" + prefix + "-TOTAL_FORMS").val(formCount + 1);

  } // End if

  return false;
}


function deleteForm(btn, prefix) {
  var formCount = parseInt($('#id_' + prefix + '-TOTAL_FORMS').val());
  if (formCount > 1) {
    // Delete the item/form
    var goto_id = $(btn).find('input').val();
    if (goto_id) {
      $.ajax({
        url: "/" + window.location.pathname.split("/")[1] + "/formset-data-delete/" + goto_id + "/?next=" + window.location.pathname,
        error: function () {
          console.log("error");
        },
        success: function (data) {
          $(btn).parents('.item').remove();
        },
        type: 'GET'
      });
    } else {
      $(btn).parents('.item').remove();
    }

    var forms = $('.item'); // Get all the forms
    // Update the total number of forms (1 less than before)
    $('#id_' + prefix + '-TOTAL_FORMS').val(forms.length);
    var i = 0;
    // Go through the forms and set their indices, names and IDs
    for (formCount = forms.length; i < formCount; i++) {
      $(forms.get(i)).find('.formset-field').each(function () {
        updateElementIndex(this, prefix, i);
      });
    }
  } // End if

  return false;


}





$("body").on('click', '.remove-form-row', function () {
  deleteForm($(this), String($('.add-form-row').attr('id')));
});

$("body").on('click', '.add-form-row', function () {
  return addForm($(this), String($(this).attr('id')));
});





