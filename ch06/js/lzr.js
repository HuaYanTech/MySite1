$(function() {
	$('#btn1').click(function() {
		$('div').show(1000);
	});
	$('#btn2').click(function() {
		$('div').text('Hello World!')
	})
	
	// var lis=document.getElementsByTagName('li')
	
	$('li:even').css('backgroundColor','pink')
	$('li:odd').css('backgroundColor','hotpink')
	// var lis=$('li');
	// for (var i=0; i<lis.length;i++){
	// 	if (i%2==0){
	// 		lis[]'pink'
	// 	}
	// 	else{
	// 		lis[i].style.backgroundColor='hotpink'
	// 	}
	// }
	
	
})
