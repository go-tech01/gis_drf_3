function send_input() {
    axios.post('/accounts/create/', {
        username: document.getElementById('username').value,
        password: document.getElementById('password').value,
    })
        .then(function (response) {
            console.log(response);
            document.getElementById('alert_box').innerHTML
                = "<div class='btn btn-primary rounded-pill px-5'>로그인이 성공했습니다</div>"
            document.cookie='drf2_token=Token'+response.data['token']
//            window.location.href = '/accounts/hello_world_template/'
        })
        .catch(function (error) {
            console.log(error);
            document.getElementById('alert_box').innerHTML
                = "<div class='btn btn-danger rounded-pill px-5'>로그인이 실패했습니다</div>"
        });
}