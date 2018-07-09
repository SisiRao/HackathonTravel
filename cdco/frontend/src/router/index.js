import Vue from 'vue'
import Router from 'vue-router'
import first from '../page/first'
import second from '../page/second'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path:'/',
      redirect:'/second'
    },
    {
      path: '/first',
      component: first
    },
    {
      path: '/second',
      component: second
    }
  ]
})
