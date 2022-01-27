const catalogueComponent = {
    template: `
    <h1>MyFlix catalogue</h1>

    <div v-cloak id="category-select">
        Category:
        <select v-model="category" v-on:change="catSelectChange();" style="display:inline;">
            <option v-for="category in categories_list">
                {{ category }}
            </option>
        </select>
    </div>

    <ul v-cloak id="list_of_films">
        <li v-for="film in films">
        <div style="width:90%;height:300px;">
            <router-link v-bind:to="'/view_film/' + film._id">
                <img v-bind:src="film.thumblink" style="width:360px;height:240px;float:left;">
            </router-link>
            <div style="float:left;margin:20px;">
                <router-link v-bind:to="'/view_film/' + film._id">
                    <h2> {{ film.name }}</h2>
                    view film
                </router-link>
                <br>
                Category: {{ film.categories_readable }}
            </div>
        </div>
        </li>
    </ul>
    `,
    data() {
        return {
            category: "all",
            films: [],
            categories_list: ["all"],
        }
    },
    created() {
        console.log("created catalogueComponent");
        this.fetchCategoriesList();
        this.fetchFilms();
    },
    methods: {
        fetchFilms() {
            console.log("in ff");

            fetch(api_url + "/db/list_films/" + this.category)
            .then((response) => {
                console.log(response);
                response.json().then((data) => {
                    console.log(data);
                    data.forEach(e => {
                        if(e.categories) {
                            e.categories_readable = e.categories.join(", ")
                        }
                    });
                    this.films = data;
                })
            }).catch((error) => {
                console.log("network error:");
                console.error(error);
            });
        },

        fetchCategoriesList() {
            console.log("in fcl");

            fetch(api_url + "/db/list_categories")
            .then((response) => {
                console.log(response);
                response.json().then((data) => {
                    console.log(data);
                    this.categories_list = ["all"].concat(data);
                })
            }).catch((error) => {
                console.log("network error:");
                console.error(error);
            });
        },

        catSelectChange() {
            this.fetchFilms();
        }
    }
};