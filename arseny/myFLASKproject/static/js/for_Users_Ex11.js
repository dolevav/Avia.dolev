console.log('users_exc11');

function getUsers(){
    console.log('clicked');
    fetch('').then(
        response => response.json()
    ).then(
        response_obj => put_users_inside_html(response_obj.data)
    ).catch(
        err => console.log(err)
    )
}

function put_users_inside_html(response_obj_data){

    // console.log(response_obj_data);

    const curr_main = document.querySelector("main");
    for (let user of response_obj_data) {
        const section = document.createElement('section');
        section.innerHTML = `
        <div>
            <span>${user.id} </span>  
            <span>${user.name} </span>
            <br>
            <a href="mailto:${user.age}">Age</a>
        </div>
        `;
        curr_main.appendChild(section);
    }
}