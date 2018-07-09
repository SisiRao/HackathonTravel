<template>
  <div id="second">
    <div id="title-box">
      <h1>travelGo行程规划</h1>
      <el-button size="medium" @click="handleBtnClick">跳转至实时规划</el-button>
    </div>
    <div style="height: 700px">
      <vue-googlemap id="googlemap" :center='center'
                     :zoom='zoom'
                     :controls='controls'>
        <vue-googlemap-marker :position='center'
                              draggable
                              events='events'
                              label="NewYork">
        </vue-googlemap-marker>
        <vue-googlemap-marker :position='[40.689249,-74.0445]'
                              draggable
                              label="A"
                              v-if="showA">
        </vue-googlemap-marker>
        <vue-googlemap-marker :position='[40.779437,-73.963244]'
                              draggable
                              label="B"
                              v-if="showB">
        </vue-googlemap-marker>
        <vue-googlemap-marker :position='[40.759011,-73.9844722]'
                              draggable
                              label="C"
                              v-if="showC">
        </vue-googlemap-marker>
        <vue-googlemap-marker :position='[40.7828647,-73.9653551]'
                              draggable
                              label="D"
                              v-if="showD">
        </vue-googlemap-marker>
        <vue-googlemap-marker :position='[40.7484405,-73.9856644]'
                              draggable
                              label="E"
                              v-if="showE">
        </vue-googlemap-marker>
        <vue-googlemap-marker :position='[36.1314583,-95.9664237]'
                              draggable
                              label="F"
                              v-if="showF">
        </vue-googlemap-marker>

        <vue-googlemap-infoWindow :position='center'
                                  draggable
                                  ref='window'
        ></vue-googlemap-infoWindow>
      </vue-googlemap>
    </div>
    <div id="checkbox">
      <h2>选择你想去的地方</h2>
      <div id="user-select">
        <el-checkbox-group v-model="checkList">
          <el-checkbox label="A" @change="changeA">Statue of Liberty</el-checkbox>
          <el-checkbox label="B" @change="changeB">The Metropolitan Museum of Art</el-checkbox>
          <el-checkbox label="C" @change="changeC">Times Square</el-checkbox>
          <br>
          <el-checkbox label="D" @change="changeD">Central Park</el-checkbox>
          <el-checkbox label="E" @change="changeE">Empire State Building</el-checkbox>
          <el-checkbox label="F" @change="changeF">Fifth Avenue</el-checkbox>
        </el-checkbox-group>
        <div id="time-select">
          <el-time-select
            placeholder="起始时间"
            v-model="startTime"
            :picker-options="{
          start: '08:30',
          step: '00:15',
          end: '18:30'
        }">
          </el-time-select>
          <el-time-select
            placeholder="结束时间"
            v-model="endTime"
            :picker-options="{
          start: '08:30',
          step: '00:15',
          end: '17:30',
          minTime: startTime
        }">
          </el-time-select>
          <el-button type="primary" @click="submit(endTime)">submit</el-button>
        </div>

      </div>

    </div>
    <!--返回来的table-->
    <div class="table" v-if="showTable1">
          <el-table
          :data="tableData"
          style="width: 100%">
            <el-table-column
              prop="schema"
              label="序号"
              >
            </el-table-column>
            <el-table-column
              prop="starttime"
              label="出发时间">
            </el-table-column>
            <el-table-column
              prop="t1"
              label="行程时间">
            </el-table-column>
            <el-table-column
              prop="p1"
              label="景点1(游玩时间)">
            </el-table-column>
            <el-table-column
              prop="t2"
              label="行程时间">
            </el-table-column>
            <el-table-column
              prop="p2"
              label="景点2(游玩时间)">
            </el-table-column>
            <el-table-column
              prop="endtime"
              label="结束时间">
            </el-table-column>
          </el-table>
    </div>

    <div class="table" v-if="showTable2">
      <el-table
        :data="tableData2"
        style="width: 100%">
        <el-table-column
          prop="schema"
          label="序号"
        >
        </el-table-column>
        <el-table-column
          prop="starttime"
          label="出发时间">
        </el-table-column>
        <el-table-column
          prop="t1"
          label="行程时间">
        </el-table-column>
        <el-table-column
          prop="p1"
          label="景点1(游玩时间)">
        </el-table-column>
        <el-table-column
          prop="t2"
          label="行程时间">
        </el-table-column>
        <el-table-column
          prop="p2"
          label="景点2(游玩时间)">
        </el-table-column>
        <el-table-column
          prop="t3"
          label="行程时间">
        </el-table-column>
        <el-table-column
          prop="p3"
          label="景点3(游玩时间)">
        </el-table-column>
        <el-table-column
          prop="endtime"
          label="结束时间">
        </el-table-column>
      </el-table>
    </div>
  </div>

</template>
<script>
  import router from 'vue-router'
  export default {
    name: 'second',
    data(){
      return{
        center: [40.689249, -74.0445],
        zoom:11,
        controls: ['zoom', 'streetView'],
        events: {
          click(o) {
            console.log(o)
          }
        },
        checkList:[],
        startTime: '',
        endTime: '',
        showA:false,
        showB:false,
        showC:false,
        showD:false,
        showE:false,
        showF:false,
        showTable1:false,
        showTable2:false,
        tableData:[
          {
            schema:1,
            starttime:'10:00 am',
            t1:'11min',
            p1:'The Metropolitan Museum of Art(150min)',
            t2:'12min',
            p2:'Central Park(120min)',
            endtime:'12:53 pm'
          },
          {
            schema:2,
            starttime:'10:00 am',
            t1:'12min',
            p1:'Central Park(120min)',
            t2:'11min',
            p2:'The Metropolitan Museum of Art(150min)',
            endtime:'12:23 pm'
          },
          {
            schema:3,
            starttime:'10:00 am',
            t1:'12min',
            p1:'Central Park(120min)',
            t2:'17min',
            p2:'Statue of Liberty(240min)',
            endtime:'12:28 pm'
          }
        ],
        tableData2:[

          {
            schema:1,
            starttime:'10:00 am',
            t1: '11min',
            p1: 'The Metropolitan Museum of Art(150min)',
            t2: '12min',
            p2: 'Central Park(120min)',
            t3: '16min',
            p3: 'Statue of Liberty(240min)',
            endtime:'19:09 pm'
          },
          {
            schema:2,
            starttime:'10:00 am',
            t1: '11min',
            p1: 'Central Park(120min)',
            t2: '17min',
            p2: 'Statue of Liberty(240min)',
            t3: '13min',
            p3: 'The Metropolitan Museum of Art(150min)',
            endtime:'19:11 pm'
          },
          {
            schema:3,
            starttime:'10:00 am',
            t1: '11min',
            p1: 'The Metropolitan Museum of Art(150min)',
            t2: '17min',
            p2: 'Statue of Liberty(240min)',
            t3: '13min',
            p3: '(Danger)Central Park(120min)',
            endtime:'19:11 pm'
          },
        ]
      }
    },
    methods:{
      handleBtnClick(){
        this.$router.push('/')
      },
      changeA(show){
        if(this.showA){
          this.showA=false
        }else{
          this.showA=true
        }
      },
      changeB(show){
        if(this.showB){
          this.showB=false
        }else{
          this.showB=true
        }
      },
      changeC(){
        if(this.showC){
          this.showC=false
        }else{
          this.showC=true
        }
      },
      changeD(){
        if(this.showD){
          this.showD=false
        }else{
          this.showD=true
        }
      },
      changeE(){
        if(this.showE){
          this.showE=false
        }else{
          this.showE=true
        }
      },
      changeF(){
        if(this.showF){
          this.showF=false
        }else{
          this.showF=true
        }
      },
      submit(endTime){
        if (endTime!="19:30") {
          this.showTable1=true
        } else {
          this.showTable2=true
        }
      }

    }

  }
</script>
<style>
  #user-select{
    display: flex;
    justify-content: space-around;

  }
</style>
