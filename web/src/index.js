const router = VueRouter.createRouter({
    history: VueRouter.createWebHashHistory(),
    routes:[
        // {path: '/view_film/:id', component: {template: '<h3>temp {{$route.params.id}}</h3>'}},
        {path: '/view_film/:id', component: viewFilmComponent},
        // {path: '/view_film/', component: view_film_comp},
        {path: '', component: catalogueComponent},
        // {path: '/view_film', component: tempcomp},
        // {path: '/view_film/', component: Vue.component('hello-world', {
        //     template: '#hello-world-template'
        //   })},
    ],
})

const app = Vue.createApp( {

}).use(router).mount('#app')