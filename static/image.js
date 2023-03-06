window.addEventListener('load', () => {
    console.log('load')
    $('input[type="text"]').keydown(function(e) {
      if (e.keyCode === 13) {
        e.preventDefault();
      };
    });
  
    var imageInput = document.querySelector('input[name="init_image"]')
    imageInput.addEventListener('change', (e)=> {
      console.log('preview image')
      var imgSrc = e.target.value
      var previewImg = document.querySelector('#preview_init_image')
      previewImg.src = imgSrc
    })
  
    
  var button = document.querySelector('#img-to-img')
    button.addEventListener('click', (e) => {
      console.log('click')
      var form = $('#stable_image-form')
      var serializeArray = form.serialize()
      var ajax_options = {
        url: '/stable-diffusion-image',
        method: 'POST',
        data: serializeArray,
        statusCode: {
          200: function(data, status) {
            var imgSrc = data[0]
            var resultImg = document.createElement('img')
            var resultImg = document.querySelector('#result-img')
            resultImg.src = imgSrc
            document.querySelector('body').appendChild(resultImg)
          },
          400: function(data, status) {
            console.log(data)
            alert(data['message'])
          },
          500: function(xhr, status) {
            alert("서버에서 오류가 발생했습니다")
          }
        }
      }
      $.ajax(ajax_options);
  })
  })