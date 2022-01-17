const viewFilmComponent = {
    template: `
    <h1>{{film.name}}</h1>
    <video v-bind:src="film.vlink" controls=""></video>
    <p> {{ film.credit ? 'credit: ' + film.credit : '' }} </p>
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
        this.fetchFilmInfo();
    },
    methods: {
        fetchFilmInfo() {
            console.log("in ffi");

            fetch(this.api_url + "/db/get_film_by_id/" + this.$route.params.id)
            .then((response) => {
                console.log(response);
                // const data = await response.json();
                console.log(response.status);
                console.log(response.statusText);
                response.json().then((data) => {
                    console.log(data);
                    this.film = data;
                    // this.film = {name: data.name, vlink: data.vlink}
                })
            }).catch((error) => {
                console.log("network error:");
                console.error(error);
                // this.add_film_status = "network_error";
            });
        }
    }
};