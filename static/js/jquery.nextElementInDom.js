(function( $ ){
    $.fn.nextElementInDom = function(selector, options) {
        var defaults = { stopAt : 'body' };
        options = $.extend(defaults, options);

        var parent = $(this).parent();
        var found = parent.find(selector);

        switch(true){
            case (found.length > 0):
                return found;
            case (parent.length === 0 || parent.is(options.stopAt)):
                return $([]);
            default:
                return parent.nextElementInDom(selector);
        }
    };
})( jQuery );