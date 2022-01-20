const app = Vue.createApp({
    data() {
        return {
            // api_url: "http://localhost:5000/api",
            // api_url: 'http://34.76.189.193/api',

            filmname: "",
            vlink: "",
            vcredit: "",
            categories: "",
            thumblink: "",
            add_film_status: "none",
        }
    },
    methods: {
        async add_film() {
            console.log("addfilmbutton.");
            
            categories = this.categories.split(',').map(x=>x.trim());
            

            fetch(api_url + "/db/add_film", {
                method: "POST",
                headers: {"Content-Type":"application/json"},
                body: JSON.stringify({
                    filmname: this.filmname,
                    vlink: this.vlink,
                    credit: this.vcredit,
                    categories: categories,
                    thumblink: this.thumblink,
                })
            }).then((response) => {
                console.log(response);

                if (response.ok){
                    this.add_film_status = "response_ok";
                    this.filmname = "";
                    this.vlink = "";
                    this.vcredit = "";
                    this.categories = "";
                    this.thumblink = "";
                } else {
                    this.add_film_status = "response_not_ok";
                }
            }).catch((error) => {
                this.add_film_status = "network_error";
            });
        },

        clear_add_film_confirmation() {
            this.add_film_status= "none";
        },
    }
});

app.mount('#app');