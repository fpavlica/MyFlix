const loginComponent = {
    template: `
    <h1>Login</h1>
    <label>Username: </label>
    <input type="text" v-model="username"></input>
    <br>
    <label>Pasword: </label>
    <input type="password" v-model="password"></input>
    <br>
    <button id="login_submit" v-on:click="login">Log in</button>
    <br><br>
    <button id="register_user" v-on:click="register">Create new account</button>
    `,
    data() {
        return {
            api_url: "http://localhost:5000/api",
            // api_url: 'http://34.76.189.193/api',

            film: {},
        }
    },
    created() {
        console.log("created viewFilmComponent");
    },
    methods: {
        login() {
            console.log("trying to log in")
            pwhash = CryptoJS.SHA256("password").toString()

            fetch(this.api_url + "/accounts/login", {
                method: "POST",
                headers: {"Content-Type":"application/json"},
                body: JSON.stringify({
                    username: this.username,
                    password: pwhash,
                    })
                }).then((response) => {
                    console.log(response);
                    this.username = "";
                }).catch((error) => {
                    console.log("network error:");
                    console.error(error);
                });
                // this.password = "";

        },
        register() {
            //hashing password for a false sense of security.
            //hashing before sending does not help because we're not using https anyway
            //but it kinda helps prevent someone just reading the plaintext password with a bot
            pwhash = CryptoJS.SHA256("password").toString()

            fetch(this.api_url + "/accounts/register", {
                method: "POST",
                headers: {"Content-Type":"application/json"},
                body: JSON.stringify({
                    username: this.username,
                    password: pwhash,
                })
            }).then((response) => {
                console.log(response);
                // this.username = "";
            //     // const data = await response.json();
            //     console.log(response.status);
            //     console.log(response.statusText);
            //     response.json().then((data) => {
            //         console.log(data);
            //         this.film = data;
                // })
            }).catch((error) => {
                console.log("network error:");
                console.error(error);
                // this.add_film_status = "network_error";
            });
            // this.password = "";
        }
    }
};