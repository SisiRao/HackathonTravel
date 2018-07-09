<template>
  <div id="app">
    <img src="./assets/logo-min.png" >


    <!--<div id="title-box">-->
      <!--<h1>travelGo</h1>-->
      <!--<el-button size="medium" @click="clickTwo">跳转至行程规划</el-button>-->
    <!--</div>-->
    <!--<div class="flex-container">-->
      <!--<div style="height: 700px">-->
        <!--<vue-googlemap id="googlemap" :center='center'-->
                       <!--:zoom='zoom'-->
                       <!--:controls='controls'-->
                       <!--style="width: 800px; heigtht:400px">-->
          <!--<vue-googlemap-marker :position='center'-->
                                <!--draggable-->
                                <!--events='events'-->
                                <!--label="NewYork">-->
          <!--</vue-googlemap-marker>-->
          <!--<vue-googlemap-marker :position='[41,-74]'-->
                                <!--draggable-->
                                <!--label="A">-->
          <!--</vue-googlemap-marker>-->
          <!--<vue-googlemap-marker :position='[40.8,-73]'-->
                                <!--draggable-->
                                <!--label="B">-->
          <!--</vue-googlemap-marker>-->

          <!--<vue-googlemap-infoWindow :position='center'-->
                                    <!--draggable-->
                                    <!--ref='window'-->
          <!--&gt;</vue-googlemap-infoWindow>-->
        <!--</vue-googlemap>-->
      <!--</div>-->
      <!--<div>-->
        <!--<el-input>searchNearby-->
          <!--<el-button slot="append" @click="handleBtnClick">GO</el-button>-->
        <!--</el-input>-->
        <!--&lt;!&ndash;<el-autocomplete&ndash;&gt;-->
        <!--&lt;!&ndash;class="inline-input"&ndash;&gt;-->
        <!--&lt;!&ndash;v-model="myLocation"&ndash;&gt;-->
        <!--&lt;!&ndash;placeholder="请输入当前位置"&ndash;&gt;-->
        <!--&lt;!&ndash;@select="handleSelect">&ndash;&gt;-->
        <!--&lt;!&ndash;<el-button slot="append">GO</el-button>&ndash;&gt;-->
        <!--&lt;!&ndash;</el-autocomplete>&ndash;&gt;-->

        <!--<el-table :data="retrievedSites" style="width: 100%;" border="true" v-if="show_table">-->
          <!--&lt;!&ndash;<div v-for="item in retrievedSites">&ndash;&gt;-->
          <!--<el-table-column-->
            <!--prop="place" label="景点名" width="160%">-->
          <!--</el-table-column>-->
          <!--<el-table-column-->
            <!--prop="distance" label="距离/km" width="100%">-->
          <!--</el-table-column>-->
          <!--<el-table-column-->
            <!--prop="taxiHour" label="行驶时间" width="100%" >  &lt;!&ndash;乘坐taxi时间（预计）&ndash;&gt;-->
          <!--</el-table-column>-->
          <!--<el-table-column-->
            <!--prop="tourHour" label="游览时间/h" width="100%">-->
          <!--</el-table-column>-->
          <!--<el-table-column-->
            <!--prop="openingHour" label="开放时间" width="150%">-->
          <!--</el-table-column>-->
          <!--&lt;!&ndash;</div>&ndash;&gt;-->
        <!--</el-table>-->
      <!--</div>-->
    <!--</div>-->
    <router-view></router-view>
  </div>
</template>

<script>
  import axios from 'axios'
export default {
  data:{
    name:'app'
    // return {
    //   center: [40.6, -74],
    //   zoom: 11,
    //   controls: ['zoom', 'streetView'],
    //   events: {
    //     click(o) {
    //       console.log(o)
    //     }
    //   },
    //   show_table: false,
    //   myLocation:'',
    //   retrievedSites:[
    //     {
    //       place: 'Statue of Liberty',
    //       distance:'3',
    //       taxiHour:'Times ',
    //       tourHour:3,
    //       openingHour:'9:30-15:30'
    //     },
    //     {
    //       place: 'The Metropolitan Museum of Art',
    //       distance:'8',
    //       taxiHour:'Times ',
    //       tourHour:4,
    //       openingHour:'10:00-21:00'
    //     },
    //     {
    //       place: 'Times Square',
    //       distance:'5',
    //       taxiHour:'Times ',
    //       tourHour:2,
    //       openingHour:'0:00-23：59'
    //     },
    //     {
    //       place: 'Central Park',
    //       distance:'8',
    //       taxiHour:'Times ',
    //       tourHour:4,
    //       openingHour:'6:00-23：59'
    //     },
    //     {
    //       place: 'Empire State Building',
    //       distance:'9',
    //       taxiHour:'Times ',
    //       tourHour:2,
    //       openingHour:'8:00-23：59'
    //     },
    //     {
    //       place: 'Fifth Avenue',
    //       distance:'10',
    //       taxiHour:'Times ',
    //       tourHour:2,
    //       openingHour:'0:00-23：59'
    //     },
    //
    //   ]
    // }
  }

  // methods:{
  //   clickTwo(){
  //     this.$router.push('/second')
  //   },
  //   // retrieve(){
  //   //   var site = this.$ajax({
  //   //     method: 'get',
  //   //     url: '/plan',
  //   //   })
  //   //   console.log(a)
  //   // },
  //   handleBtnClick(){
  //     // this.$ajax({
  //     //   method:'post',
  //     //   url: '/plan',
  //     //   data: this.myLocation,
  //     //   success:function () {
  //     //     this.show_table=true
  //     //   }
  //     // })
  //
  //     axios.post("/plan", {
  //       location : this.myLocation
  //     })
  //       .then(function(data) {
  //         console.log(data);
  //       })
  //
  //
  //   }
  // }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
 .flex-container{
   display: flex;
   justify-content:space-between;
 }


</style>
