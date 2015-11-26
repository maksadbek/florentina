var defaults = {
	min:1,
	max: 99
}
$.fn.numberfield = function(options){
	var settings = $.extend(defaults, options),
		wrapper = $("<div class='numberfield' />");

	return this.each(function(){
		var $this = $(this);
		$this.wrap(wrapper);
		$this.after("<a href='#' class='minus'></a><a href='#' class='plus'></a>")
		$this.bind("keyup", function(e){
			var val = parseInt($(this).val()) || settings.min;
			val = val < settings.min ? settings.min : val;
			val = val > settings.max ? settings.max : val;
			$(this).val(val);
		});
		$this.siblings("a").bind("click", function(e){
			e.preventDefault();
			if($(this).hasClass("minus")){
				decrement($this);
			}else{
				increment($this);
			}
		});
	});
	function decrement(obj){
		var val = parseInt(obj.val()) || settings.min;
		val--;
		val = val < settings.min ? settings.min : val;
		val = val > settings.max ? settings.max : val;
		obj.val(val);
	}
	function increment(obj){
		var val = parseInt(obj.val()) || settings.min;
		val++;
		val = val < settings.min ? settings.min : val;
		val = val > settings.max ? settings.max : val;
		obj.val(val);
	}
}