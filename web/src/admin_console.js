const app = Vue.createApp({
    data() {
        return {
            // api_url: "http://localhost:5000/api",
            api_url: 'http://34.76.189.193/api',

            filmname: "",
            vlink: "",
            vcredit: "",
            add_film_status: "none",
        }
    },
    methods: {
        async add_film() {
            console.log("addfilmbutton.");
            // console.log(this.filmname);
            // console.log(this.vlnk);

            // const response = await 
            fetch(this.api_url + "/db/add_film", {
                method: "POST",
                headers: {"Content-Type":"application/json"},
                body: JSON.stringify({
                    filmname: this.filmname,
                    vlink: this.vlink,
                    credit: this.vcredit,
                })
            }).then((response) => {
                console.log(response);
                // const data = await response.json();
                console.log(response.status);
                console.log(response.statusText);

                this.filmname = "";
                this.vlink = "";
                this.vcredit = "";

                if (response.ok){
                    this.add_film_status = "response_ok";
                } else {
                    this.add_film_status = "response_not_ok";
                }
            }).catch((error) => {
                // console.log("network error");
                this.add_film_status = "network_error";
            });
        },

        clear_add_film_confirmation() {
            this.add_film_status= "none";
        },
    }
});

app.mount('#app');