<template>
  <div chart-container>
    <div id="chart" class="chart"></div>
    <div id="chart2" class="chart2"></div>
    <div class="background-image"></div>
  </div>
</template>

<script>
    import gldata from './gl.json';
    import * as echarts from 'echarts'
    import 'echarts-gl'
    import world from './world.js'
export default {
    mounted() {
    this.drawChart(gldata);
    this.drawChart2(gldata)
  },
    methods: {
      drawChart(data) {
      var chartDom = document.getElementById('chart');
      var myChart = echarts.init(chartDom);
      const canvas = document.createElement('canvas')
      const mapChart = echarts.init(canvas, null, {
      width: 4096,
      height: 2048
    })
      echarts.registerMap('world', world)
      mapChart.setOption({
      visualMap: {
        type: 'piecewise',
        show: false,
        pieces: [
          { gt: 2000, color: '#FF4646', label: '最多' },
          { gt: 500, lte: 2000, color: '#FF7500', label: '较多' },
          { gt: 100, lte: 500, color: '#FFD300', label: '适中' },
          {
            gte: 0,
            lte: 100,
            color: {
              type: 'radial', // linear 线性渐变  radial径向渐变
              x: 0.5, // 0.5为正中心，如果小于渐变中心靠左
              y: 0.5, // 0.5为正中心，如果小于渐变中心靠上
              r: 0.5,
              colorStops: [
                {
                  offset: 0,
                  color: 'rgba(255,255,255,0.8)' // 0% 处的颜色
                },
                {
                  offset: 1,
                  color: 'rgba(86, 189, 255, 0.2)' // 100% 处的颜色
                }
              ]
            },
            label: '低风险'
          },
          { value: -1, color: '#93B8F8', label: '未知' }
        ]
      },
      series: [
        {
          type: 'map',
          map: 'world',
          // 绘制完整尺寸的 echarts 实例
          top: 0,
          left: 0,
          right: 0,
          bottom: 0,
          boundingCoords: [
            [-180, 90],
            [180, -90]
          ],
          itemStyle: {
            borderColor: '#aaa', //边界线颜色
            areaColor: 'transparent' //默认区域颜色
          },
          emphasis: {
            itemStyle: {
              show: true,
              areaColor: '#fff' //鼠标滑过区域颜色
            },
            label: {
                show: true,
                formatter: '{b}: {c}' // Display name and value in the tooltip
              }
          },
          data: data
        }
      ]
    });

    myChart.setOption({
      globe: {
        baseTexture: 'https://images-1308194867.cos.ap-beijing.myqcloud.com/images/home/world.jpg', //地球的纹理。支持图片路径的字符串，图片或者 Canvas 的对象
        shading: 'lambert', //地球中三维图形的着色效果
        atmosphere: {
          show: true, //显示大气层
          offset: 8,
          color: '#13315E'
        },
        light: {
          ambient: {
            intensity: 0.8 //环境光源强度
          }, //环境光
          main: {
            intensity: 0.2 //光源强度
          }
        },
        geo3D: {
          // Enable zooming with the mouse scroll wheel
          roam: true,
          map: 'world',
          viewControl: {
            autoRotate: true,
            autoRotateSpeed: 3,
            autoRotateAfterStill: 2,
            rotateSensitivity: 2,
            targetCoord: [116.46, 39.92],
            maxDistance: 200,
            minDistance: 200
          }
        },
        layers: [
          {
            //地球表面层的配置，你可以使用该配置项加入云层，或者对 baseTexture 进行补充绘制出国家的轮廓等等。
            show: true,
            type: 'blend',
            texture: mapChart
          }
        ]
      },
      tooltip: {
          show: true,
          formatter: '{b}: {c}' // Display name and value in the tooltip
        },
    })
    },
    drawChart2(data) {
      var chartDom = document.getElementById('chart2');
      var myChart = echarts.init(chartDom);
      const mapOption = {
    visualMap: {
      left: 'right',
      min: 0,
      max: 5000,
      inRange: {
        // prettier-ignore
        color: ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf', '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
      },
      text: ['High', 'Low'],
      calculable: true
    },
    series: [
      {
        id: 'population',
        type: 'map',
        roam: true,
        map: 'world',
        animationDurationUpdate: 5000,
        universalTransition: true,
        data: data
      }
    ]
  };
  const barOption = {
    xAxis: {
      type: 'value'
    },
    yAxis: {
      type: 'category',
      axisLabel: {
        rotate: 30
      },
      data: data.map(function (item) {
        return item.name;
      })
    },
    animationDurationUpdate: 5000,
    series: {
      type: 'bar',
      id: 'population',
      data: data.map(function (item) {
        return item.value;
      }),
      universalTransition: true
    }
  };
  let currentOption = mapOption;
  myChart.setOption(mapOption);
  setInterval(function () {
    currentOption = currentOption === mapOption ? barOption : mapOption;
    myChart.setOption(currentOption, true);
  }, 20000);

    
    },
   }
}
</script>
<style scoped>
.chart {
    width: 100%;
    /* 设置图表宽度为100% */
    height: 600px;
    /* 设置固定的高度或者使用vh单位 */
  }
  
.chart2 {
    width: 100%;
    /* 设置图表宽度为100% */
    height: 600px;
   /* 设置固定的高度或者使用vh单位 */
}
  .background-image {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-image: url('114541488_p0_master1200.jpg'); /* Replace with the correct path to your image */
    background-size: cover;
    background-position: center;
    opacity: 0.5; /* Adjust opacity as needed */
    z-index: -1; /* Move the background behind the charts */
  }
</style>
