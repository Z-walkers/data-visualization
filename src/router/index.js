import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      redirect: '/home',
      hidden: 'true'
    },
    {
      path: '/home',
      name: '总数据',
      redirect: '/home/student',
      component: () => import('@/components/Home'),
      children: [
        {
          path: '/home/student',
          name: '查询数据',
          component: () => import('@/components/students/studentList')
        },
        {
          path: '/home/work',
          name: '类别总结',
          component: () => import('@/components/students/workList')
        },
        {
          path: '/home/info',
          name: '增长趋势',
          component: () => import('@/components/students/infoList')
        },
        {
          path: '/home/other',
          name: '数据来源',
          component: () => import('@/components/students/other')
        },
        {
          path: '/home/other1',
          name: '直观数量与评分',
          component: () => import('@/components/students/other1')
        }
      ]
    }
  ],
  mode: 'history'
})
