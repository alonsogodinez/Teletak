$(document).ready(function() {
    //delete modal content after close
    $('body').on('hidden.bs.modal', '.modal', function () {
        $(this).removeData('bs.modal');
      });


});







