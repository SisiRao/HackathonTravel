// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import axios from 'axios'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import vueGooglemap from 'vue2-googlemap'


Vue.config.productionTip = false
Vue.use(axios)
Vue.use(ElementUI)
Vue.use(vueGooglemap)
Vue.use(router)

vueGooglemap.initGooglemap({
  key: 'AIzaSyAPSy-Javi3MIG6XVekj0harxkpr3wuNio',
  language: 'zh-CN',
  v: '3',
})


new Vue({
  el: '#app',
  router,
  components:{App},
  template:'<App/>'
})
