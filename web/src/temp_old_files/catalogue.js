// const tempcomp = { template: '#tempid'}
const tempcomp = { template: '#view_film_template'}

const router = VueRouter.createRouter({
    history: VueRouter.createWebHashHistory(),
    routes:[
        // {path: '/view_film/:id', component: {template: '<h3>temp {{$route.params.id}}</h3>'}},
        {path: '/view_film/', component: tempcomp},
        // {path: '/view_film', component: tempcomp},
        // {path: '/view_film/', component: Vue.component('hello-world', {
        //     template: '#hello-world-template'
        //   })},
    ],
})

const app = Vue.createApp({
    data() {
        return {
            api_url: "http://localhost:5000/api",
            // api_url: 'http://34.76.189.193/api',

            category: "all",
            films: [],
        }
    },
    created() {
        console.log("created");
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
}).use(router).mount('#app');