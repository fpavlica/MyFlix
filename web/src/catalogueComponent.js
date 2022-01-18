const catalogueComponent = {
    template: `
    <h1>MyFlix catalogue</h1>

    <ul v-cloak id="list_of_films">
        <li v-for="film in films">
            {{ film.name }}
            <br>
            <router-link v-bind:to="'/view_film/' + film._id">view film link</router-link>
            <br>
            {{ film.vlink }}
            <br>
            {{ film.credit }}
            <br>
            <br> <!-- temp spacing-->
            <br>
        </li>
    </ul>
    `,
    data() {
        return {
            // api_url: "http://localhost:5000/api",
            api_url: 'http://34.76.189.193/api',

            category: "all",
            films: [],
        }
    },
    created() {
        console.log("created catalogueComponent");
        this.fetchFilms();
    },
    methods: {
        fetchFilms() {
            console.log("in ff");

            fetch(this.api_url + "/db/list_films/" + this.category)
            .then((response) => {
                console.log(response);
                // const data = await response.json();
                console.log(response.status);
                console.log(response.statusText);
                response.json().then((data) => {
                    console.log(data);
                    this.films = data;
                })
            }).catch((error) => {
                console.log("network error:");
                console.error(error);
                // this.add_film_status = "network_error";
            });
        }
    }
};