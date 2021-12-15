function send_input() {
    var form = new FormData();
    form.append('nickname', document.getElementById('nickname').value);
    form.append('message', document.getElementById('message').value);
    form.append('image', document.getElementById('image').files[0]);
    axios({
        method:'post',
        url:'/profiles/',
        data: form,
        headers:{
            Authorization: decodeURIComponent(getCookie('drf_token'))
        },
    })
        .then(function (response) {
            console.log(response);
            window.location.href = 'accounts/retrieve_template/'+response.data['owner']['id'];
        })
        .catch(function (error) {
            console.log(error);
            document.getElementById('alert_box').innerHTML
                = "<div class='btn btn-danger rounded-pill px-5'>프로필 작성에 실패했습니다</div>"
        });
}