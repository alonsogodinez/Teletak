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
    })


});





