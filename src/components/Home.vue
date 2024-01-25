<template>
  <div class="home">
    <h1>{{ msg }}</h1>
    <hr>
    <Header></Header>
    <el-container class='content'>
      <div>
        <el-aside width="200px">
          <el-menu router default-active="2" class="el-menu-vertical-demo" @open="handleOpen" @close="handleClose"
            background-color="#00FFFF" active-text-color="#fff">
            <div v-for="(item, index) in menus">
              <el-submenu :index="index + ''" :key='index' v-if="!item.hidden">
                <template slot="title">
                  <i class="el-icon-location"></i>
                  <span>{{ item.name }}</span>
                </template>
                <el-menu-item-group v-for="(child, index) in item.children" :key="index">
                  <el-menu-item :index="child.path">{{ child.name }}</el-menu-item>
                </el-menu-item-group>
              </el-submenu>
            </div>

          </el-menu>
        </el-aside>
      </div>
      <el-main>
        <div>
          <router-view></router-view>
        </div>
        <Footer></Footer>
      </el-main>
      <Menu></Menu>
    </el-container>
  </div>
</template>

<script>
import Header from './common/Header'
import Footer from './common/Footer'
import Menu from './common/Menu'
export default {
  components: {
    Header,
    Footer,
    Menu
  },
  name: 'Home',
  data() {
    return {
      msg: 'Welcome to Your Vue.js App',
      menus: []
    }
  },
  created() {
    console.log(this.$router.options.routes)
    this.menus = [...this.$router.options.routes]
  },
  methods: {
    handleOpen(key, keyPath) {
      console.log(key, keyPath);
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath);
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.home .el-aside {
  height: 100%;
}

.home .content {
  position: absolute;
  width: 100%;
  top: 94px;
  bottom: 0;
}

.home .el-aside .el-menu {
  height: 5%;
}

.home .el-aside .el-submenu {
  min-width: 0;
}

.home .el-aside .el-menu-item {
  min-width: 0;
}
</style>
