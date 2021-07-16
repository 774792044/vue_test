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
                >搜索</el-button
              >
            </div>
          </el-col>
        </el-row>
      </el-header>
      <el-main>
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
          style="margin-top: 20px"
          :gutter="20"
          type="flex"
          justify="center"
          v-for="i in 2"
          :key="i"
        >
          <el-col :span="4" v-for="o in 6" :key="o">
            <el-card shadow="hover" :body-style="{ padding: '0px' }">
              <img
                src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png"
                class="image"
              />
              <div style="padding: 14px">
                <span>好吃的汉堡</span>
                <!-- <div class="bottom clearfix">
                  <el-button type="text" class="button">操作按钮</el-button>
                </div> -->
              </div>
            </el-card>
          </el-col>
        </el-row>
      </el-main>
      <!-- <el-footer>Footer</el-footer> -->
    </el-container>
  </div>
</template>
<script >
export default {
  data () {
    return {
      input: '',
      select: '',
      activeIndex: '1',
      activeIndex2: '1',
    }
  },
  methods: {
    handleSelect (key, keyPath) {
      console.log(key, keyPath)

    },
    send_url: function (url) {
      //发送 post 请求
      this.$axios.post('/user', {
        firstName: 'Fred',
        lastName: 'Flintstone'
      })
        .then(function (response) {
          console.log(response)
        })
        .catch(function (error) {
          console.log(error)
        })
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


