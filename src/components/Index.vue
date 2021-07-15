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
      </el-main>
      <el-footer>Footer</el-footer>
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
      activeIndex2: '1'
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
    }
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
</style>


