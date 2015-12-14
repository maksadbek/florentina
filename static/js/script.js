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