const loginComponent = {
    template: `
    <h1>Login</h1>
    <label>Username: </label>
    <input type="text" v-model="username">
    <br>
    <label>Pasword: </label>
    <input type="password" v-model="password">
    <br>
    <button id="login_submit" v-on:click="login">Log in</button>
    <br><br>
    <button id="register_user" v-on:click="register">Create new account</button>
    <br>
    <p v-cloak v-if="(register_status!='')"> {{ register_status }}</p>
    `,
    data() {
        return {
            // api_url: "http://localhost:5000/api",
            // api_url: 'http://34.76.189.193/api',

            film: {},
            register_status: "",
            username: "",
            password: "",
        }
    },
    created() {
        console.log("created viewFilmComponent");
    },
    methods: {
        login() {
            this.register_status = "";
            console.log("trying to log in")
            pwhash = CryptoJS.SHA256("password").toString()

            fetch(api_url + "/accounts/login", {
                method: "POST",
                headers: {"Content-Type":"application/json"},
                body: JSON.stringify({
                    username: this.username,
                    password: pwhash,
                    })
                }).then((response) => {
                    console.log(response);
                    if (response.status == 200) {
                        //should save the received token cookie
                        //but a token cookie is still to be implemented
                        //instead just redirect for now
                        this.$router.push('/catalogue');

                    }
                }).catch((error) => {
                    this.register_status = "Network error."
                    console.error(error);
                });

        },
        register() {
            this.register_status = "";
            //hashing password for a false sense of security.
            //hashing before sending does not help because we're not using https anyway
            //but it kinda helps prevent someone just reading the plaintext password with a bot
            pwhash = CryptoJS.SHA256("password").toString()

            fetch(api_url + "/accounts/register", {
                method: "POST",
                headers: {"Content-Type":"application/json"},
                body: JSON.stringify({
                    username: this.username,
                    password: pwhash,
                })
            }).then((response) => {
                console.log(response);
                if (response.status == 201) {
                    this.register_status = "Registered successfully. You may log in.";
                } else if (response.status == 409) {
                    this.register_status = "Registration failed, username already exists.";
                }
                else {
                    this.register_status = "Registration failed.";
                }
            }).catch((error) => {
                this.register_status = "network error:";
                console.error(error);
            });
        }
    }
};