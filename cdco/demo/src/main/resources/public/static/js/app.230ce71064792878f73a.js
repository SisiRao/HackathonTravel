webpackJsonp([1],{"5fQj":function(e,t){},"8NY4":function(e,t){},NHnr:function(e,t,o){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var a=o("7+uW"),i={data:function(){return{center:[40.6,-74],zoom:11,controls:["zoom","streetView"],events:{click:function(e){console.log(e)}},show_table:!1,myLocation:"",retrievedSites:[{place:"Statue of Liberty",distance:"3",taxiHour:"Times ",tourHour:3,openingHour:"9:30-15:30"},{place:"The Metropolitan Museum of Art",distance:"8",taxiHour:"Times ",tourHour:4,openingHour:"10:00-21:00"},{place:"Times Square",distance:"5",taxiHour:"Times ",tourHour:2,openingHour:"0:00-23：59"},{place:"Central Park",distance:"8",taxiHour:"Times ",tourHour:4,openingHour:"6:00-23：59"},{place:"Empire State Building",distance:"9",taxiHour:"Times ",tourHour:2,openingHour:"8:00-23：59"},{place:"Fifth Avenue",distance:"10",taxiHour:"Times ",tourHour:2,openingHour:"0:00-23：59"}]}},methods:{clickTwo:function(){this.$router.push("/second")},handleBtnClick:function(){this.$ajax({method:"post",url:"/plan",data:this.myLocation,success:function(){this.show_table=!0}})}}},n={render:function(){var e=this,t=e.$createElement,o=e._self._c||t;return o("div",{attrs:{id:"app"}},[o("div",{attrs:{id:"title-box"}},[o("h1",[e._v("travelGo")]),e._v(" "),o("el-button",{attrs:{size:"medium"},on:{click:e.clickTwo}},[e._v("跳转至行程规划")])],1),e._v(" "),o("div",{staticClass:"flex-container"},[o("div",{staticStyle:{height:"700px"}},[o("vue-googlemap",{staticStyle:{width:"800px",heigtht:"400px"},attrs:{id:"googlemap",center:e.center,zoom:e.zoom,controls:e.controls}},[o("vue-googlemap-marker",{attrs:{position:e.center,draggable:"",events:"events",label:"NewYork"}}),e._v(" "),o("vue-googlemap-marker",{attrs:{position:[41,-74],draggable:"",label:"A"}}),e._v(" "),o("vue-googlemap-marker",{attrs:{position:[40.8,-73],draggable:"",label:"B"}}),e._v(" "),o("vue-googlemap-infoWindow",{ref:"window",attrs:{position:e.center,draggable:""}})],1)],1),e._v(" "),o("div",[o("el-input",[e._v("searchNearby\n        "),o("el-button",{attrs:{slot:"append"},on:{click:e.handleBtnClick},slot:"append"},[e._v("GO")])],1),e._v(" "),e.show_table?o("el-table",{staticStyle:{width:"100%"},attrs:{data:e.retrievedSites,border:"true"}},[o("el-table-column",{attrs:{prop:"place",label:"景点名",width:"160%"}}),e._v(" "),o("el-table-column",{attrs:{prop:"distance",label:"距离/km",width:"100%"}}),e._v(" "),o("el-table-column",{attrs:{prop:"taxiHour",label:"行驶时间",width:"100%"}}),e._v(" "),o("el-table-column",{attrs:{prop:"tourHour",label:"游览时间/h",width:"100%"}}),e._v(" "),o("el-table-column",{attrs:{prop:"openingHour",label:"开放时间",width:"150%"}})],1):e._e()],1)])])},staticRenderFns:[]};var r=o("VU/8")(i,n,!1,function(e){o("jIZi")},null,null).exports,l=o("/ocq"),s={data:function(){return{center:[40.6,-74],zoom:11,controls:["zoom","streetView"],events:{click:function(e){console.log(e)}},show_table:!1,myLocation:"",retrievedSites:[{place:"Statue of Liberty",distance:"3",taxiHour:"Times ",tourHour:3,openingHour:"9:30-15:30"},{place:"The Metropolitan Museum of Art",distance:"8",taxiHour:"Times ",tourHour:4,openingHour:"10:00-21:00"},{place:"Times Square",distance:"5",taxiHour:"Times ",tourHour:2,openingHour:"0:00-23：59"},{place:"Central Park",distance:"8",taxiHour:"Times ",tourHour:4,openingHour:"6:00-23：59"},{place:"Empire State Building",distance:"9",taxiHour:"Times ",tourHour:2,openingHour:"8:00-23：59"},{place:"Fifth Avenue",distance:"10",taxiHour:"Times ",tourHour:2,openingHour:"0:00-23：59"}]}},methods:{clickTwo:function(){this.$router.push("/second")},handleBtnClick:function(){this.$ajax({method:"post",url:"/plan",data:this.myLocation,success:function(){this.show_table=!0}})}}},c={render:function(){var e=this,t=e.$createElement,o=e._self._c||t;return o("div",{attrs:{id:"app"}},[o("div",{attrs:{id:"title-box"}},[o("h1",[e._v("travelGo")]),e._v(" "),o("el-button",{attrs:{size:"medium"},on:{click:e.clickTwo}},[e._v("跳转至行程规划")])],1),e._v(" "),o("div",{staticClass:"flex-container"},[o("div",{staticStyle:{height:"700px"}},[o("vue-googlemap",{staticStyle:{width:"800px",heigtht:"400px"},attrs:{id:"googlemap",center:e.center,zoom:e.zoom,controls:e.controls}},[o("vue-googlemap-marker",{attrs:{position:e.center,draggable:"",events:"events",label:"NewYork"}}),e._v(" "),o("vue-googlemap-marker",{attrs:{position:[41,-74],draggable:"",label:"A"}}),e._v(" "),o("vue-googlemap-marker",{attrs:{position:[40.8,-73],draggable:"",label:"B"}}),e._v(" "),o("vue-googlemap-infoWindow",{ref:"window",attrs:{position:e.center,draggable:""}})],1)],1),e._v(" "),o("div",[o("el-input",[e._v("searchNearby\n        "),o("el-button",{attrs:{slot:"append"},on:{click:e.handleBtnClick},slot:"append"},[e._v("GO")])],1),e._v(" "),e.show_table?o("el-table",{staticStyle:{width:"100%"},attrs:{data:e.retrievedSites,border:"true"}},[o("el-table-column",{attrs:{prop:"place",label:"景点名",width:"160%"}}),e._v(" "),o("el-table-column",{attrs:{prop:"distance",label:"距离/km",width:"100%"}}),e._v(" "),o("el-table-column",{attrs:{prop:"taxiHour",label:"行驶时间",width:"100%"}}),e._v(" "),o("el-table-column",{attrs:{prop:"tourHour",label:"游览时间/h",width:"100%"}}),e._v(" "),o("el-table-column",{attrs:{prop:"openingHour",label:"开放时间",width:"150%"}})],1):e._e()],1)])])},staticRenderFns:[]};var u=o("VU/8")(s,c,!1,function(e){o("8NY4")},null,null).exports,p={data:function(){return{center:[40.689249,-74.0445],zoom:11,controls:["zoom","streetView"],events:{click:function(e){console.log(e)}},checkList:[],startTime:"",endTime:"",showA:!1,showB:!1,showC:!1,showD:!1,showE:!1,showF:!1}},methods:{handleBtnClick:function(){this.$router.push("/first")},changeA:function(e){this.showA?this.showA=!1:this.showA=!0},changeB:function(e){this.showB?this.showB=!1:this.showB=!0},changeC:function(){this.showC?this.showC=!1:this.showC=!0},changeD:function(){this.showD?this.showD=!1:this.showD=!0},changeE:function(){this.showE?this.showE=!1:this.showE=!0},changeF:function(){this.showF?this.showF=!1:this.showF=!0}}},h={render:function(){var e=this,t=e.$createElement,o=e._self._c||t;return o("div",{attrs:{id:"second"}},[o("div",{attrs:{id:"title-box"}},[o("h1",[e._v("travelGo行程规划")]),e._v(" "),o("el-button",{attrs:{size:"medium"},on:{click:e.handleBtnClick}},[e._v("跳转至实时规划")])],1),e._v(" "),o("div",{staticStyle:{height:"700px"}},[o("vue-googlemap",{attrs:{id:"googlemap",center:e.center,zoom:e.zoom,controls:e.controls}},[o("vue-googlemap-marker",{attrs:{position:e.center,draggable:"",events:"events",label:"NewYork"}}),e._v(" "),e.showA?o("vue-googlemap-marker",{attrs:{position:[40.689249,-74.0445],draggable:"",label:"A"}}):e._e(),e._v(" "),e.showB?o("vue-googlemap-marker",{attrs:{position:[40.779437,-73.963244],draggable:"",label:"B"}}):e._e(),e._v(" "),e.showC?o("vue-googlemap-marker",{attrs:{position:[40.759011,-73.9844722],draggable:"",label:"C"}}):e._e(),e._v(" "),e.showD?o("vue-googlemap-marker",{attrs:{position:[40.7828647,-73.9653551],draggable:"",label:"D"}}):e._e(),e._v(" "),e.showE?o("vue-googlemap-marker",{attrs:{position:[40.7484405,-73.9856644],draggable:"",label:"E"}}):e._e(),e._v(" "),e.showF?o("vue-googlemap-marker",{attrs:{position:[36.1314583,-95.9664237],draggable:"",label:"F"}}):e._e(),e._v(" "),o("vue-googlemap-infoWindow",{ref:"window",attrs:{position:e.center,draggable:""}})],1)],1),e._v(" "),o("div",{attrs:{id:"checkbox"}},[o("h2",[e._v("选择你想去的地方")]),e._v(" "),o("div",{attrs:{id:"user-select"}},[o("el-checkbox-group",{model:{value:e.checkList,callback:function(t){e.checkList=t},expression:"checkList"}},[o("el-checkbox",{attrs:{label:"A"},on:{change:e.changeA}},[e._v("Statue of Liberty")]),e._v(" "),o("el-checkbox",{attrs:{label:"B"},on:{change:e.changeB}},[e._v("The Metropolitan Museum of Art")]),e._v(" "),o("el-checkbox",{attrs:{label:"C"},on:{change:e.changeC}},[e._v("Times Square")]),e._v(" "),o("br"),e._v(" "),o("el-checkbox",{attrs:{label:"D"},on:{change:e.changeD}},[e._v("Central Park")]),e._v(" "),o("el-checkbox",{attrs:{label:"E"},on:{change:e.changeE}},[e._v("Empire State Building")]),e._v(" "),o("el-checkbox",{attrs:{label:"F"},on:{change:e.changeF}},[e._v("Fifth Avenue")])],1),e._v(" "),o("div",{attrs:{id:"time-select"}},[o("el-time-select",{attrs:{placeholder:"起始时间","picker-options":{start:"08:30",step:"00:15",end:"18:30"}},model:{value:e.startTime,callback:function(t){e.startTime=t},expression:"startTime"}}),e._v(" "),o("el-time-select",{attrs:{placeholder:"结束时间","picker-options":{start:"08:30",step:"00:15",end:"18:30",minTime:e.startTime}},model:{value:e.endTime,callback:function(t){e.endTime=t},expression:"endTime"}}),e._v(" "),o("el-button",{attrs:{type:"primary"}},[e._v("submit")])],1)],1)]),e._v(" "),e.showTable?o("div",{attrs:{id:"table"}},[o("el-table",[o("el-table-column")],1)],1):e._e()])},staticRenderFns:[]};var d=o("VU/8")(p,h,!1,function(e){o("5fQj")},null,null).exports;a.default.use(l.a);var v=new l.a({routes:[{path:"/",name:"firstPage",component:u},{path:"/second",component:d}]}),g=o("mtWM"),m=o.n(g),b=o("zL8q"),_=o.n(b),w=(o("tvR6"),o("eaGg")),f=o.n(w);a.default.config.productionTip=!1,a.default.use(m.a),a.default.use(_.a),a.default.use(f.a),a.default.use(v),f.a.initGooglemap({key:"AIzaSyAPSy-Javi3MIG6XVekj0harxkpr3wuNio",language:"zh-CN",v:"3"}),new a.default({el:"#app",router:v,components:{App:r},template:"<App/>"})},jIZi:function(e,t){},tvR6:function(e,t){}},["NHnr"]);
//# sourceMappingURL=app.230ce71064792878f73a.js.map