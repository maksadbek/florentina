$("input[type=number]").numberfield();

var signUpBtn = ".signup",
	signInBtn = ".signin";

$(signUpBtn+","+signInBtn).on('click', function ( e ) {
    var link = $(this).attr("href");
    Custombox.open({
        target: link,
        effect: 'blur'
    });
    e.preventDefault();
});

$(".buy_row select").selectBox();

$(".modal form").bind("submit", function(e){
	e.preventDefault();
	$.ajax({
		url: $(this).attr("action"),
		type: $(this).attr("method"),
		data: $(this).serialize(),
		beforeSend:function(){
			$("div.errors").text("");
		},
		success:function(data){
			if(typeof data == "object"){
				if(data.errors){
					for(i in data.errors){
						$("input[name="+i+"]").after("<div class='errors'>"+data.errors[i][0]+"</div>");
					}
				}else{
					$("div.errors").text(data.error);
				}
			}else{
				window.location.reload();
			}
		}
	});
});

$("form.buy_form").bind("submit", function(e){
	e.preventDefault();
	var form = $(this);
	$.ajax({
		type: form.attr("method"),
		url: form.attr("action"),
		data: form.serialize(),
		success:function(data){
			if(typeof data == "object"){
				$(".signed .counter").html(data.cart_items);
			}
		}
	});
});
