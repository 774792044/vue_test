<template>
  <div id="app">
    <el-container>
      <el-header style="back">
        <el-row :gutter="20">
          <el-col :span="8" :offset="8" >
            <div>
              <el-input :offset="-1" placeholder="请输入URL" v-model="input" class="input-with-select">
                <el-select v-model="select" slot="prepend" placeholder="http://">
                  <el-option label="http://" value="http"></el-option>
                  <el-option label="https://" value="https"></el-option>
                </el-select>
                <!-- <el-button type="primary" slot="append" icon="el-icon-search"></el-button> -->
              </el-input>
            </div>
          </el-col>
          <el-col :span="1" :offset="0">
            <div style="position:absulute">
              <el-button type="primary" icon="el-icon-search">搜索</el-button>
            </div>
          </el-col>
        </el-row>
      </el-header>
      <el-main>
      <el-divider></el-divider> 
        main
        <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
  <el-menu-item index="1">处理中心</el-menu-item>
  <el-submenu index="2">
    <template slot="title">我的工作台</template>
    <el-menu-item index="2-1">选项1</el-menu-item>
    <el-menu-item index="2-2">选项2</el-menu-item>
    <el-menu-item index="2-3">选项3</el-menu-item>
    <el-submenu index="2-4">
      <template slot="title">选项4</template>
      <el-menu-item index="2-4-1">选项1</el-menu-item>
      <el-menu-item index="2-4-2">选项2</el-menu-item>
      <el-menu-item index="2-4-3">选项3</el-menu-item>
    </el-submenu>
  </el-submenu>
  <el-menu-item index="3" disabled>消息中心</el-menu-item>
  <el-menu-item index="4"><a href="https://www.ele.me" target="_blank">订单管理</a></el-menu-item>
</el-menu>
      </el-main>
      <el-footer>Footer</el-footer>
    </el-container>
  </div>

</template>
<script>
export default {
  data() {
    return {
      input: '',
      select: '',
      activeIndex: '1',
      activeIndex2: '1'
    }
  },
  methods: {
      handleSelect(key, keyPath) {
        console.log(key, keyPath);
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
  .el-select{
    width: 130px;
  }
  .el-select .el-input {
    width: 130px;
  }
  .input-with-select .el-input-group__prepend {
    background-color: #fff;
  }
</style>


