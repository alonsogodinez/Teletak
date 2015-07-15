$(document).ready(function() {

//    function centerModals(){
//  $('.modal').each(function(i){
//    var $clone = $(this).clone().css('display', 'block').appendTo('body');
//    var top = Math.round(($clone.height() - $clone.find('.modal-content').height()) / 2);
//    top = top > 0 ? top : 0;
//    $clone.remove();
//    $(this).find('.modal-content').css("margin-top", top);
//  });
//}
//$('.modal').on('show.bs.modal', centerModals);
//$(window).on('resize', centerModals);

    //delete modal content after close
    $('body').on('hidden.bs.modal', '.modal', function () {
        $(this).removeData('bs.modal');
      });

    $(function() {
        $('form .formset').formset();
    });


    $('#id_devolucion').change(function () {
        $('#id_nodo').prop("disabled", this.checked);
    }).change()

    //Choidec Dinamicos
    $(".c-almacen").change(function(){
        var r = /\d+/;
        var s = $(this).attr("id");
        num = s.match(r);
        $.ajax({
                url : "/operaciones/getproducto/"+ $(this).val() +"/",
                type : "GET",
                dataType: "json",
                async: true,
                success : function(j) {
                    var options = '<option value="0">---------- </option>';
                    for (var i = 0; i < j.length; i++) {
                        options += '<option value="' + parseInt(j[i].codigo) + '">' + j[i].nombre + '</option>';
                    }
                    nextid = "#id_formset-"+num+"-codigo_producto";
                    $(nextid).html(options);
                    $(nextid + " option:first").attr('selected', 'selected');
                    $(nextid).attr('disabled', false);

                    /*$("#id_form-"+ num +"-codigo_producto").html(options);
                    $("#id_form-"+ num +"-codigo_producto option:first").attr('selected', 'selected');
                    $("#id_form-"+ num +"-codigo_producto").attr('disabled', false);*/
                },
                error : function(xhr,errmsg,err) {
                    alert(xhr.status + ": " + xhr.responseText);
                }
        });
    });
    $(".c-producto").change(function(){
        var r = /\d+/;
        var s = $(this).attr("id");
        num = s.match(r);
        almacen = $("#id_formset-"+ num + "-id_almacen").val();
        $.ajax({
                url : "/operaciones/getcantidad/" + almacen + "/"+ $(this).val() +"/",
                type : "GET",
                dataType: "json",
                async: true,
                success : function(j) {
                    nextid = "#id_formset-" + num + "-cantidad";
                    //alert(nextid);
                    for (var i = 0; i < j.length; i++) {
                        $(nextid).attr( "max", parseInt(j[i].max_value));
                        $(nextid).attr( "value", parseInt(j[i].max_value));
                    }
                    $(nextid).attr('disabled', false);
                },
                error : function(xhr,errmsg,err) {
                    alert(xhr.status + ": " + xhr.responseText);
                }
        });
    });



});

