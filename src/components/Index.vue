<template>
  <div id="app">
    <el-container>
      <el-header style="back">
        <el-row :gutter="20">
          <el-col :span="8" :offset="7">
            <div>
              <el-input
                :offset="-1"
                placeholder="请输入URL"
                v-model="input"
                class="input-with-select"
              >
                <el-select
                  v-model="select"
                  slot="prepend"
                  placeholder="http://"
                >
                  <el-option label="http://" value="http"></el-option>
                  <el-option label="https://" value="https"></el-option>
                </el-select>
                <!-- <el-button type="primary" slot="append" icon="el-icon-search"></el-button> -->
              </el-input>
            </div>
          </el-col>
          <el-col :span="1" :offset="0">
            <div style="position: absulute">
              <el-button
                type="primary"
                icon="el-icon-search"
                v-on:click="send_url"
                >搜索
              </el-button>
              <button @click="add()">Add A</button>
            </div>
          </el-col>
        </el-row>
      </el-header>
      <el-main>
        <!-- 菜单栏 -->
        <el-menu
          :default-active="activeIndex"
          class="el-menu-demo"
          mode="horizontal"
          @select="handleSelect"
        >
          <el-menu-item index="1" style="margin-left: 15%">class1</el-menu-item>
          <el-menu-item index="2">class2</el-menu-item>
          <el-menu-item index="3">class3</el-menu-item>
          <el-menu-item index="4">class4</el-menu-item>
          <el-menu-item index="5">class5</el-menu-item>
          <el-menu-item index="6">class6</el-menu-item>
          <el-menu-item index="7">class7</el-menu-item>
          <el-menu-item index="8">class8</el-menu-item>
          <el-menu-item index="9">class9</el-menu-item>
          <el-menu-item index="10">class10</el-menu-item>
        </el-menu>
        <el-row
          id="row1"
          style="margin-top: 20px"
          :gutter="20"
          type="flex"
          justify="center"
          v-for="item in items.length"
          :key="item"
        >
          <el-col :span="4" v-for="url in items[item - 1]" :key="url">
            <p>{{ url }}</p>
            <el-card shadow="hover" :body-style="{ padding: '0px' }">
              <img :src="url" class="image" />
              <!-- <img src="../../images/1.jpeg" class="image" /> -->
              <!-- <img src="images/1.jpeg" class="image" /> -->
              <div style="padding: 14px">
                <span>{{ item.text }}</span>
              </div>
            </el-card>
          </el-col>
        </el-row>
      </el-main>
      <el-footer>Footer</el-footer>
    </el-container>
  </div>
</template>
<script >
import Vue from 'vue'

var AComponent = Vue.extend({
  props: ['text'],
  template: '<li>A Component: {{ text }}</li>'
})

var BComponent = Vue.extend({
  props: ['image_path'],
  template:
    '< el - col : span="4" v-for= "o in row_image_number" : key = "o" > \
      <el-card shadow="hover" : body-style="{ padding: "0px" }"> \
        <img src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png" class="image" /> \
        <div style="padding: 14px"> \
          <span>好吃的汉堡</span> \
        </div> \
      </el-card> \
    </el - col > '
})

export default {
  components: {
    // eslint-disable-next-line vue/no-unused-components
    'a-component': AComponent,
  },
  data: function () {
    return {
      input: '',
      select: '',
      activeIndex: '1',
      activeIndex2: '1',
      items: [],
      row_image_number: 6,
      image_dir: '/home/zhuozj/project/vue_test/images',
      have_get_image_number: 0,
    }
  },
  methods: {
    handleSelect (key, keyPath) {
      console.log(key, keyPath)
    },
    add () {
      this.items.push([require("/images/1.jpeg"), require("/images/2.jpeg")])
      console.log(this.items)
    },
    show_image () {
      let image_path_list = []
      // this.$axios({
      //   method: 'GET',
      //   url: `http://127.0.0.1:5000/get_image_path?path=${this.image_dir}`,
      //   async: false,
      //   // headers: {
      //   //   'Accept': '*/*',
      //   //   'Content-Type': 'application/x-www-form-urlencoded'
      //   // }
      // }).then(function (response) {
      //   image_number = response.data['image_path_list'].length
      //   console.log('1 image number: ', image_number)
      // })

      this.$jquery.ajax({
        url: `http://127.0.0.1:5000/get_image_path?path=${this.image_dir}`,
        type: 'GET', //GET
        async: false, //或false,是否异步
        success: function (response, textStatus, jqXHR) {
          image_path_list = response['image_path_list']
        },
        complete: function () {
        }
      })

      let image_number = image_path_list.length

      if (image_number > this.have_get_image_number) {
        let not_get_image_number = image_number - this.have_get_image_number
        for (var i = 0; i < not_get_image_number; i++) {
          let index = this.have_get_image_number + i
          console.log(index)
        }
      }
      /*
      if (image_number > this.have_get_image_number) {
        let not_get_image_number = image_number - this.have_get_image_number
        // 数量整除部分
        for (var i = 0; i < parseInt(not_get_image_number / this.row_image_number); i++) {
          for (var j = 0; j < this.row_image_number; j++) {
            let index = this.have_get_image_number + i * this.row_image_number + j
            // console.log('index', index)
 
          }
        }
 
        let yushu = not_get_image_number % this.row_image_number
        // 数量余数部分
        for (var i = 0; i < yushu; i++) {
          let index = image_number - (yushu - i)
          console.log('index', index)
        }
      }*/
      this.have_get_image_number = image_number

      clearInterval(this.timer)
      this.timer = null
    },
    send_url (url) {
      // TODO  发送爬取图片请求
      /*
      this.$jquery.ajax({
        url: `http://127.0.0.1:5000/get_image_path?path=${this.image_dir}`,
        type: 'GET', //GET
        async: false, //或false,是否异步
        success: function (response, textStatus, jqXHR) {
          image_path_list = response['image_path_list']
        },
        complete: function () {
        }
      })*/

      // 启动扫描文件夹定时器
      if (this.timer == null) {
        this.timer = setInterval(() => {
          this.show_image()
        }, 1000)
      }
    },
  }
}
</script>
<style>
.el-col {
  border-radius: 4px;
}

.bg-purple-dark {
  background: #99a9bf;
}

.bg-purple {
  background: #d3dce6;
}

.bg-purple-light {
  background: #e5e9f2;
}

.grid-content {
  border-radius: 4px;
  min-height: 36px;
}

.row-bg {
  padding: 10px 0;
  background-color: #f9fafc;
}

.el-select {
  width: 130px;
}

.el-select .el-input {
  width: 130px;
}

.input-with-select .el-input-group__prepend {
  background-color: #fff;
}

.el-menu-item {
  width: 7%;
}

.image {
  width: 100%;
  display: block;
}

.clearfix:before,
.clearfix:after {
  display: table;
  content: '';
}

.clearfix:after {
  clear: both;
}
</style>


