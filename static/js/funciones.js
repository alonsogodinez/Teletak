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

    $(".chosen-select").chosen({no_results_text: "No se encontró coincidencias con :",
                                width: '100%' });
 //
    $('#detalle').modal('show');

    $('#id_devolucion').change(function () {
        $('#id_nodo').prop("disabled", this.checked);
    }).change();

    $(".c-almacen").click(function(){
        //Obteniendo el nro de form del formset
        var r = /\d+/;
        var s = $(this).attr("id");
        num = s.match(r);
        almacen_actual = $(this).val();
        //Llenando el array producto con los productos ya seleccionados
        var productos = [ $(this).val() ];
        $(".c-producto").each(function() {
            var g = $(this).attr("id");
            numero = g.match(r);
            fila_actual = "id_formset-"+num+"-codigo_producto";
            item_actual = String($(this).attr("id"));
            console.log(item_actual + " - " + fila_actual);
            if( $(this).val() > 0 && $("#id_formset-"+ numero + "-id_almacen").val() == almacen_actual)
            {
                if(fila_actual != item_actual)
                    productos.push($(this).val());
            }
        });
        //transformado la data a json
        data = '{"almacen":';
        for(var i=0;i<productos.length;i++)
        {
            if(i==0)
            {
                data += productos[i] + ',"productos":[';
            }
            else
            {
                if(i==productos.length-1)
                    data += productos[i];
                else
                    data += productos[i]+",";
            }
        }
        data += "]}";
        console.log(data);
        if ($(this).val() > 0)
        {
            $.ajax({
                url: "/operaciones/getproducto/",
                type: "POST",
                data:  data,
                dataType: "json",
                async: true,
                success: function (j) {
                    var options = '<option value="0">Escoja un Producto</option>';
                    for (var i = 0; i < j.length; i++) {
                        options += '<option value="' + parseInt(j[i].codigo) + '">' + j[i].nombre + '</option>';
                    }
                    nextid = "#id_formset-" + num + "-codigo_producto";
                    $(nextid).html(options);
                    $(nextid + " option:first").attr('selected', 'selected');
                    $(nextid).attr('disabled', false);
                    $("#id_formset-"+ num +"-cantidad").attr('disabled', true);
                },
                error: function (xhr, errmsg, err) {
                    alert(xhr.status + ": " + xhr.responseText);
                }
            });
        }
        else
        {
            $("#id_formset-"+ num +"-codigo_producto").attr('disabled', true);
            $("#id_formset-"+ num +"-cantidad").attr('disabled', true);
        }
    });


    $(".c-producto").change(function(){
        var r = /\d+/;
        var s = $(this).attr("id");
        num = s.match(r);
        almacen = $("#id_formset-"+ num + "-id_almacen").val();
        if (almacen > 0) {
            $.ajax({
                url: "/operaciones/getcantidad/" + almacen + "/" + $(this).val() + "/",
                type: "GET",
                dataType: "json",
                async: true,
                success: function (j) {
                    nextid = "#id_formset-" + num + "-cantidad";
                    //alert(nextid);
                    for (var i = 0; i < j.length; i++) {
                        $(nextid).attr("max", parseInt(j[i].max_value));
                        $(nextid).attr("value", parseInt(j[i].max_value));
                    }
                    $(nextid).attr('disabled', false);
                },
                error: function (xhr, errmsg, err) {
                    alert(xhr.status + ": " + xhr.responseText);
                }
            });
        }
    });



    $("#registrartrabajador").click(function(e){
        var password =$("#id_password");
        var dni = $('#id_dni');

        if($("#id_password2").val()!=password.val()){
            e.preventDefault();

            if($("#error_password").length==0){
                password
                    .parent()
                    .parent()
                    .prepend('<ul id="error_password" class="errorlist">' +
                                '<li> Las constraseñas ingresadas no coinciden</li></ul>');
            }

        }

        if(dni.val().length!=8){
            if($("#error_dni").length==0) {
                dni
                    .parent()
                    .parent()
                    .prepend('<ul id="error_dni" class="errorlist">' +
                    '<li> Este campo tiene que ser de 8 caracteres</li></ul>');
            }

        }
        else{
            var error_password =$("#error_password");
            if(error_password.length>0) alert("existe error");
            e.submit();
        }



    });

    var datatable = {

        "oLanguage": {
            "oAria": {
                "sSortAscending": " - ordenar de forma ascendente",
                "sSortDescending": " - ordenar de forma descendente",
                "sInfoEmpty": "No hay información para mostrar",
                "sLengthMenu": "Mostrar _MENU_ registros",
                "sSearch": "Buscar :",
                "sZeroRecords": "No hay ningún registro",

            },
            "oPaginate": {
                "sFirst": "Primera página",
                "sLast": "Última página",
                "sNext": "Página siguiente",
                "sPrevious": "Página anterior"
            },

            "sEmptyTable": "Esta tabla no tiene datos",
            "sInfo": "Mostrando  _START_ - _END_ de _TOTAL_ registros",
            "sInfoEmpty": "Mostrando 0 entradas",
            "sInfoFiltered": "(filtrados de _MAX_  registros en total)",
            "sLengthMenu": "Motrar _MENU_ registros",
            "sSearch": "Buscar :",
            "sZeroRecords": "No se encontraron coincidencias"

        }
    };

    $('#datatable').DataTable(datatable);
    $('#reporte').DataTable(datatable);

    var datatableresponsive = datatable;

    datatableresponsive.responsive = true;

    $('#datatable-responsive').DataTable(datatableresponsive);

    $("#btnExport").click(function () {

        var uri =$("#tblExport").battatech_excelexport({
            containerid: "reporte",
            datatype: 'table',
            returnUri: true
        });
        var today = new Date();
        $(this).attr('download', 'ReporteFinal'+'.xls').attr('href', uri);
    });



});





