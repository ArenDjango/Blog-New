function loginDialog(){
      $('#login_system').removeClass('nonelogsystem');
      if($('#register_system').is(':visible')){
        $('#register_system').addClass('nonelogsystem');
      }
}
function regDialog(){
      $('#register_system').removeClass('nonelogsystem');
      if($('#login_system').is(':visible')){
        $('#login_system').addClass('nonelogsystem');
      }
}

	function closeModalLogin(){
 	  $('#login_system').addClass('nonelogsystem');
    $('#errorlogin').html('');
    $('#textLogin').val('');
    $('#textPassword').val('');
	}


$('.registeropenlog').click(function(event){
  event.preventDefault()

    $('#login_system').addClass('nonelogsystem');
    $('#errorlogin').html('');
    $('#textLogin').val('');
    $('#textPassword').val('');

    $('#register_system').removeClass('nonelogsystem');

});

function closeReg(){
   $('#register_system').addClass('nonelogsystem');
    
    $('.errorregister').html('');
    $('.textlogReg').val('');
    $('.textMailReg').val('');
    $('.textpassReg').val('');
    $('.textpassRegTwo').val('');
    $('#textName').val('');
    $('#textLastName').val('');

}


function fadeRegTOvXOD(){
   $('#errorlogin').html('');
    $('.textlogReg').val('');
    $('.textMailReg').val('');
    $('.textpassReg').val('');
    $('.textpassRegTwo').val('');
     $('#textName').val('');
    $('#textLastName').val('');
   $('#register_system').addClass('nonelogsystem');
   $('#login_system').removeClass('nonelogsystem');
}




	function searchOpen(){
	  $('.dropSearch').removeClass('closeSearchDiv');
	}

	$(document).mouseup(function (e) {
      var container = $(".formSearch");
      if (container.has(e.target).length === 0){
          $('.dropSearch').addClass('closeSearchDiv');
      }
	});

	function closeSM(){
  	  $('.fsearchMobile').toggleClass('hideMobileSearch');
 	  $('.logo').toggleClass('hideMobileSearch');
  	  $('.righthomelog').show();
 	  $('.btnSearchMobile').show()
	}

	function btnMbS(){
      $('.fsearchMobile').toggleClass('hideMobileSearch');
	  $('.logo').toggleClass('hideMobileSearch');
 	  $('.righthomelog').hide();
 	  $('.btnSearchMobile').hide()
	}


	$(document).ready(function() {
      $('.btnSearch').attr('disabled','disabled');
      $('.textSearch').keyup(function() {
        if($(this).val() != '') {
           $('.btnSearch').removeAttr('disabled');
        }
        else {
        $('.btnSearch').attr('disabled','disabled');
        }
     });
 	});



	function openMenuBig(){
		$('#allblogs').toggleClass('margin-right-blogs');
		$('#testMenu').addClass('display-none');
		$('#testMenuBig').removeClass('display-none');
	}
	function closeMenuBig(){
		$('#allblogs').toggleClass('margin-right-blogs');
		$('#testMenu').removeClass('display-none');
		$('#testMenuBig').addClass('display-none');
	}


	function ok(){
 		$('#menumain').toggleClass('noneblock');
 		var d = $('#open').html()

 		if(d == '<i class="fas fa-times"></i>'){
 			$('#open').html('<i class="fas fa-bars"></i>')
 		}
 		else{
 			$('#open').html('<i class="fas fa-times"></i>')
 		}
	}



$(".showReply").click(function(event){
	 event.preventDefault();

	$(this).next(".replyCommentUl").fadeToggle();

})

$(".addReply").click(function(event){
	event.preventDefault();

	$(".addReplyDiv").show(300);
})

$(document).ready(function() {
      $('.replyBtn').attr('disabled','disabled');
      $('#replyText').keyup(function() {
        if($(this).val() != '') {
           $('.replyBtn').removeAttr('disabled');
        }
        else {
        $('.replyBtn').attr('disabled','disabled');
        }
     });
 	});

$(".otmenaReply").click(function(event){
	event.preventDefault();
	$(".addReplyDiv").hide(300);
})

$(document).ready(function() {
      $('.CommentBtn').attr('disabled','disabled');
      $('#commentText').keyup(function() {
        if($(this).val() != '') {
           $('.CommentBtn').removeAttr('disabled');
        }
        else {
        $('.CommentBtn').attr('disabled','disabled');
        }
     });
 	});

	$("#dropIProfile").click(function(event){
		event.preventDefault();

  $(".dropdownProfile").toggleClass('noneReply');

})



$('.textSearch').keyup(function(){
  if( $('.textSearch').val() != ''){
    $.ajax({
      type: "POST",
      url: "/search/",
      data: {'search_text': $('.textSearch').val()},
      success: function(data){
        $('.dropSearchUl').html(data);
      }
    });
  }
  else{
  $('.dropSearchUl').html('');
  }
});



$(document).ready(function() {
      $('#btnLogin').attr('disabled','disabled');
      $('#textLogin').keyup(function() {
        if($('#textLogin').val() != '' && $('#textPassword').val() != '') {
           $('#btnLogin').removeAttr('disabled');
        }
        else {
        $('#btnLogin').attr('disabled','disabled');
        }
     });
       $('#textPassword').keyup(function() {
        if($('#textLogin').val() != '' && $('#textPassword').val() != '') {
           $('#btnLogin').removeAttr('disabled');
        }
        else {
        $('#btnLogin').attr('disabled','disabled');
        }
     });
  });




$('#formLogin').on('submit', function(event){
    event.preventDefault();

    $.ajax({
        url : '/login/',
        type : 'POST',
        data : { 
          'login': $('#textLogin').val(),
          'password': $('#textPassword').val()
        },

        success : function(json){
            window.location.assign("/")
            $('#textLogin').val('');
            $('#textPassword').val('');
        },
        error : function(){
            $('#login_system').removeClass('nonelogsystem');
            $('body').children().not('#login_system').addClass('opacityclasslog');
            $('#errorlogin').html('<li>Неправильный <br> логин или пароль!</li>');
            $('#textLogin').val('');
            $('#textPassword').val('');
        }
    });
});




$('#formRegister').on('submit', function(event){
  event.preventDefault();
  var pass1 = $('.textpassReg').val()
  var pass2 = $('.textpassRegTwo').val()
  var name = $('#textName').val()
  var lastname = $('#textLastName').val()
  if($('.textlogReg').val() == ''){
    $('.errorregister').html('<li>Логин не может <br> быть пустым</li>');
  }
  else if(name == '' || lastname == ''){
    $('.errorregister').html('<li>Имя или Фамилия <br> не могут быть пустым</li>');
  }
  else if($('.textMailReg').val() == ''){
    $('.errorregister').html('<li>Mail не может <br> быть пустым</li>');
  }
  else if (pass1 == '' || pass2 == ''){
    $('.errorregister').html('<li>Пароли не могут быть пустым</li>');
  }
  else if(pass1 != pass2){
    $('.errorregister').html('<li>Пароли не совпадают</li>');
  }
 
  else{

    var username = $('.textlogReg').val()
    var password = $('.textpassReg').val()
    var passwordtwo = $('.textpassRegTwo').val()
    var email = $('.textMailReg').val()
    var firstname = $('#textName').val()
    var lastname = $('#textLastName').val()
    
    $.ajax({
        url : '/registeruser/',
        type : 'POST',
        data : { 
          'username': username,
          'firstname': firstname,
          'lastname': lastname,
          'mail': email,
          'password': password,
          'passwordtwo': passwordtwo,
        },

        success : function(json){
            $('.errorregister').html('');
            $('.textlogReg').val('');
            $('#textName').val('');
            $('#textLastName').val('');
            $('.textMailReg').val('');
            $('.textpassReg').val('');
            $('.textpassRegTwo').val('');
            $('.succesregister').html('<li>Регистрация <br> успешно выполнено!</li>');
            setTimeout(closeRegreg, 4500);
            function closeRegreg(){
              $('#register_system').addClass('nonelogsystem');
              $('.succesregister').html('');
            }
        },
        error : function(){
            $('.errorregister').html('');
            $('.textlogReg').val('');
            $('#textName').val('');
            $('#textLastName').val('');
            $('.textMailReg').val('');
            $('.textpassReg').val('');
            $('.textpassRegTwo').val('');
            $('#register_system').addClass('nonelogsystem');
           alert('Ошибка сервера')
        }
    });
  }
});

$('#addvideop').click(function(event){
  event.preventDefault()

  $('.myPostsAnd').fadeToggle();
  $('#addvideoform').fadeToggle();
});


// $('#addvideoform').on('submit', function(event){
//   event.preventDefault();
//   $('.erroraddvideo').val('');
//     var title = $('#addtitlevideo').val()
//     var opisaniye = $('#opisaniye').val()
//     //var img = document.forms['#addvideoform']['image'].files[0];
//     //var video = document.forms['#addvideoform']['video'].files[0];
//     var img = $('#addimagevideo');
//     var video = $('#addvideovideo');
//     $.ajax({
//       url: '/accounts/kabinet/addvideo/',
//       type: 'POST',
//       data: {
//         'title': title,
//         'opisaniye': opisaniye,
//         'img': img.value,
//         'video': video.value
//       },
//       success : function(json){
//         alert('Ok')
//       },
//       error : function(){
//         alert('No')
//       }

//     });
// });

$('#title').keyup(function(){
$('.titleDetail').text($('#title').val());
});

$('#opisaniye').keyup(function(){
$('.opisaniyepp').text($('#opisaniye').val());
});




function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});