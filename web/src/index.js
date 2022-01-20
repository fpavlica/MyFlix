//requires catalogueComponent, loginComponent, viewFilmComponent.

const router = VueRouter.createRouter({
    history: VueRouter.createWebHashHistory(),
    routes:[
        {path: '/view_film/:id', component: viewFilmComponent},
        {path: '/catalogue', component: catalogueComponent},
        {path: '', component: loginComponent},
    ],
})

const app = Vue.createApp( {

}).use(router).mount('#app')