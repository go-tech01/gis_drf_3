function initialize(pk) {
    axios.get('/accounts/' + pk )
        .then(function (response) {
            // handle success
            console.log(response);
            document.getElementById('image').src = response.data['profile']['image'];
            document.getElementById('nickname').innerHTML = response.data['profile']['nickname'];
            document.getElementById('message').innerHTML = response.data['profile']['message'];
//            document.getElementById('date_joined').innerHTML = response.data['date_joined'];
        })
        .catch(function (error) {
            // handle error
            console.log(error);
        })
        .then(function () {
            // always executed
        });
}