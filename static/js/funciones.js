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




    $("#id_form-0-id_almacen ").change(function(){
        alert("cambio de opcion");
        $.getJSON("operaciones/almacen/"+$(this).val()+"/", function(j) {
            var options = '<option value="">---------- </option>';
            alert("hola");
            for (var i = 0; i < j.length; i++) {
              options += '<option value="' + parseInt(j[i].pk) + '">' + j[i].fields['longname'] + '</option>';
            }
            $("#id_form-0-codigo_producto").html(options);
            $("#id_form-0-codigo_producto option:first").attr('selected', 'selected');
            $("#id_form-0-codigo_producto").attr('disabled', false);
        });
        $("#id_form-0-codigo_producto").attr('selected', 'selected');
    })
   /* $("#id_form-0-id_almacen ").change(function(){
        alert("cambio de ipcion");
        jQuery.ajax({
             type: "GET",
             url: "operaciones/almacen/"+$(this).val()+"/",
             dataType: "json",
             cache:false,
             success: function(result) {
                alert(result);
             }
         });
    });*/


    //FUNCIONES DE PRUEBA PARA SALIDAS - NO HACER CASO SORR


    $('#generarsalida').click(function() {
        $.ajax({
            url: $('#ajaxform').attr('action'),
            type: 'POST',
            data: $('#ajaxform').serialize(),
            dataType: 'json',
            success: function(response) {
                if(response.success){
                    $('#ajaxform')[0].reset();
                    $('.form-error').remove();
                    $('#comments').prepend(response.fields.message);

                } else {
                    $('.form-error').remove();
                    for(var error in response.errors.fields) {
                        $('#ajaxform #id_' + error).before('<div class="form-error">' + response.errors.fields[error] + '</div>');
                    }
                }
            }
        });
    });


	/*$('#generarsalida').on('click', function(){
		var almacen = $('#id_id_almacen').val();
		var usuario = $('#id_dni_usuario').val();
		var nodo = $('#id_nodo').val();
		var devolucion = $('#id_devolucion').val();
        var datos = "{'id_almacen':'" + almacen + "', 'dni_usuario':'" + usuario + "', 'devolucion':'" + devolucion + "' , 'nodo' :'"+nodo+"'}";
        alert(datos);
		if(almacen.length>0 && usuario.length>0 && nodo.length>0 && devolucion.length>0 ){
			$.ajax({
				type: 'POST',
				data: datos,
				url: $('#ajaxform').serialize(),
				dataType : 'json',
				success: function(data){
					if(data == 'existe'){
						$('#mensaje').html('<p class="alert alert-danger">Espere!!, este codigo de registro ya fue ingresado anteriormente, ingrese otro porfavor.</p>');
					}else{
					}
				}
			});
		}else{
			$('#mensaje
').html('<p class="alert alert-warning">Espere!!, tiene que ingresar todos los datos.</p>');
		}
	});}*/
	/*$('#generarsalida').on('click',function(){
            var almacen = $('#id_id_almacen').val();
            var usuario = $('#id_dni_usuario').val();
            var nodo = $('#id_nodo').val();
            var devolucion = $('#id_devolucion').val();
            var token = $('#ajaxform input[name^=csrfmiddlewaretoken] ').val();
            var data_json = '{ "csrfmiddlewaretoken" : "' + token + '" , "id_almacen" : ' + almacen + ' , "dni_usuario" : ' + usuario + ', "devolucion": "' + devolucion + '" , "nodo" : "' + nodo + '"}';
            var data_serializer = $("#ajaxform").serialize();
	        $.ajax({
            url : "salidas/api", // the endpoint
            type : "POST", // http method
            data : data_serializer, // data sent with the post request
            dataType: 'json',
            // handle a successful response
            success : function(json) {
                $('#post-text').val(''); // remove the value from the input
                console.log(json); // log the returned json to the console
                console.log("success"); // another sanity check
            },
            // handle a non-successful response
            error : function(xhr,errmsg,err) {
                $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                    " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
	});*/

});

function desbloquear()
{
    $('#nombEstudiante').attr('disabled');
    $('#regEstudiante').attr('disabled');
    $('#id_id_almacen').removeAttr('disabled','disabled');
    $('#id_dni_usuario').removeAttr('disabled','disabled');
    $('#id_devolucion').removeAttr('disabled','disabled');
    $('#id_nodo').removeAttr('disabled','disabled');
    $('#generarsalida').removeAttr('disabled','disabled');
}


function bloquear()
{
    $('#nombEstudiante').removeAttr('disabled').focus();
    $('#regEstudiante').removeAttr('disabled');
    $('#id_id_almacen').attr('disabled','disabled');
    $('#id_dni_usuario').attr('disabled','disabled');
    $('#id_devolucion').attr('disabled','disabled');
    $('#id_nodo').attr('disabled','disabled');
    $('#generarsalida').attr('disabled','disabled');
}


