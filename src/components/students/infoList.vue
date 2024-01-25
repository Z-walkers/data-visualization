<template>
  <div chart-container>
    <div>
      <el-row>
        <el-card class="chart-container"
          style="border-radius: 10px; box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1); background-color: rgba(255, 255, 255, 0.8);">
          <div id="chart4" class="chart4"></div>
        </el-card>
        <el-card class="chart-container "
          style="border-radius: 10px; box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1); background-color: rgba(255, 255, 255, 0.8);">
          <div id="chart5" class="chart5"></div>
        </el-card>
        <el-card class="chart-container "
          style="border-radius: 10px; box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1); background-color: rgba(255, 255, 255, 0.8);">
          <div id="chart6" class="chart6"></div>
        </el-card>
        <el-card class="chart-container "
          style="border-radius: 10px; box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1); background-color: rgba(255, 255, 255, 0.8);">
          <div id="chart7" class="chart7"></div>
        </el-card>
      </el-row>
    </div>
    <div class="background-image"></div>
  </div>
</template>
  
<script>
import * as echarts from 'echarts';
import sumdata from './sums.json';
import alldata from './sum.json';
import fdata from './sums1.json';
import sdata from './sum1.json';
import data2019 from './2019.json';
import data2018 from './2017.json';
import data2017 from './2018.json';
export default {
  mounted() {
    this.drawChart4(sumdata);
    this.drawChart5(alldata);
    this.drawChart6(sdata, fdata);
    this.drawChart7(data2019, data2018, data2017);
  },

  methods: {
    drawChart4(data) {
      var chartDom = document.getElementById('chart4');
      var myChart4 = echarts.init(chartDom);
      var option;
      option = {
        title: {
          text: '每日开播数目',
          left: '45%'
        },
        tooltip: {
          trigger: 'axis'
        },
        grid: {
          left: '5%',
          right: '15%',
          bottom: '10%'
        },
        xAxis: {
          data: data.map(function (item) {
            return item[0];
          })
        },
        yAxis: {},
        toolbox: {
          right: 10,
          feature: {
            dataZoom: {
              yAxisIndex: 'none'
            },
            restore: {},
            saveAsImage: {}
          }
        },
        dataZoom: [
          {
            startValue: '1993/1/1'
          },
          {
            type: 'inside'
          }
        ],
        visualMap: {
          top: 50,
          right: 10,
          pieces: [
            {
              gt: 0,
              lte: 4,
              color: '#93CE07'
            },
            {
              gt: 4,
              lte: 8,
              color: '#FBDB0F'
            },
            {
              gt: 8,
              lte: 12,
              color: '#FC7D02'
            },
            {
              gt: 12,
              lte: 16,
              color: '#FD0100'
            },
            {
              gt: 16,
              lte: 20,
              color: '#AA069F'
            },
            {
              gt: 20,
              color: '#AC3B2A'
            }
          ],
          outOfRange: {
            color: '#999'
          }
        },
        series: {
          name: '开播动画数',
          type: 'line',
          data: data.map(function (item) {
            return item[1];
          }),
          markLine: {
            silent: true,
            lineStyle: {
              color: '#333'
            },
            data: [
              {
                yAxis: 4
              },
              {
                yAxis: 8
              },
              {
                yAxis: 12
              },
              {
                yAxis: 16
              },
              {
                yAxis: 20
              }
            ]
          }
        }
      }
      myChart4.setOption(option);
    },
    drawChart5(data) {
      var chartDom = document.getElementById('chart5');
      var myChart5 = echarts.init(chartDom);
      var option;
      option = {
        tooltip: {
          trigger: 'axis',
          position: function (pt) {
            return [pt[0], '10%'];
          }
        },
        title: {
          left: 'center',
          text: '动画总数'
        },
        toolbox: {
          feature: {
            dataZoom: {
              yAxisIndex: 'none'
            },
            restore: {},
            saveAsImage: {}
          }
        },
        xAxis: {
          type: 'time',
          boundaryGap: false
        },
        yAxis: {
          type: 'value',
          boundaryGap: [0, '100%']
        },
        dataZoom: [
          {
            type: 'inside',
            start: 0,
            end: 20
          },
          {
            start: 0,
            end: 20
          }
        ],
        series: [
          {
            name: '开播动画总数',
            type: 'line',
            smooth: true,
            symbol: 'none',
            areaStyle: {},
            data: data,
            color: '#FF66CC'
          }
        ]
      };
      myChart5.setOption(option);
    },
    drawChart6(data1, data2) {
      var chartDom = document.getElementById('chart6');
      var myChart6 = echarts.init(chartDom);
      var option;
      var arrey = Object.keys(data1)
      var arrey1 = Object.values(data1)
      var arrey2 = Object.values(data2)
      console.log(arrey)
      console.log(arrey1)
      console.log(arrey2)
      option = {
        title: {
          text: '动画总数与新增对比',
          left: 'center'
        },
        grid: {
          bottom: 80
        },
        toolbox: {
          feature: {
            dataZoom: {
              yAxisIndex: 'none'
            },
            restore: {},
            saveAsImage: {}
          }
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'cross',
            animation: false,
            label: {
              backgroundColor: '#500000'
            }
          }
        },
        legend: {
          data: ['Flow', 'Rainfall'],
          left: 10
        },
        dataZoom: [
          {
            show: true,
            realtime: true,
            start: 65,
            end: 85
          },
          {
            type: 'inside',
            realtime: true,
            start: 65,
            end: 85
          }
        ],
        xAxis: [
          {
            type: 'category',
            boundaryGap: false,
            axisLine: { onZero: false },
            // prettier-ignore
            data: arrey.map(function (str) {
              return str.replace(' ', '\n');
            })
          }
        ],
        yAxis: [
          {
            name: '数量',
            type: 'value'
          },
          {
            name: '动画总数',
            nameLocation: 'start',
            alignTicks: true,
            type: 'value',
            inverse: true
          }
        ],
        series: [
          {
            name: '动画总数',
            type: 'line',
            areaStyle: {
              color: '#FF66CC'
            },
            lineStyle: {
              width: 1
            },
            emphasis: {
              focus: 'series'
            },
            markArea: {
              silent: true,
              itemStyle: {
                opacity: 0.3
              },
              data: [
                [
                  {
                    xAxis: '1993/1/1'
                  },
                  {
                    xAxis: '1993/1/10'
                  }
                ]
              ]
            },
            // prettier-ignore
            data: arrey1
          },
          {
            name: '新增动画',
            type: 'line',
            yAxisIndex: 1,
            areaStyle: {
              color: '#7401DF'
            },
            lineStyle: {
              width: 1,
              color: '#7401DF'
            },
            emphasis: {
              focus: 'series'
            },
            markArea: {
              silent: true,
              itemStyle: {
                opacity: 0.3
              },
              data: [
                [
                  {
                    xAxis: '1993/1/1'
                  },
                  {
                    xAxis: '1993/1/10'
                  }
                ]
              ]
            },
            // prettier-ignore
            data: arrey2
          }
        ]
      };
      myChart6.setOption(option);
    },
    drawChart7(d2019, d2018, d2017) {
      var chartDom = document.getElementById('chart7');
      var myChart7 = echarts.init(chartDom);
      var option;
      option = {
        title: {
          text: '2017-2019年每日新增',
          left: '20%'
        },
        tooltip: {
          position: 'top'
        },
        visualMap: {
          min: 0,
          max: 40,
          calculable: true,
          orient: 'horizontal',
          left: 'center',
          top: 'top'
        },
        calendar: [
          {
            range: '2017',
            cellSize: ['auto', 20]
          },
          {
            top: 260,
            range: '2018',
            cellSize: ['auto', 20]
          },
          {
            top: 450,
            range: '2019',
            cellSize: ['auto', 20],
            right: 5
          }
        ],
        series: [
          {
            type: 'heatmap',
            coordinateSystem: 'calendar',
            calendarIndex: 0,
            data: d2017
          },
          {
            type: 'heatmap',
            coordinateSystem: 'calendar',
            calendarIndex: 1,
            data: d2018
          },
          {
            type: 'heatmap',
            coordinateSystem: 'calendar',
            calendarIndex: 2,
            data: d2019
          }
        ]
      };
      myChart7.setOption(option);
    },
  },
}
</script>
  
<style scoped>
.chart-container {
  display: flex;
  flex-direction: column;
  /* 设置flex方向为垂直 */
  width: 100%;
  /* 设置容器宽度为100% */
  margin-bottom: 20px;
}

.chart4 {
  width: 100%;
  /* 设置图表宽度为100% */
  height: 600px;
  /* 设置固定的高度或者使用vh单位 */

}

.chart5 {
  width: 100%;
  /* 设置图表宽度为100% */
  height: 600px;
  /* 设置固定的高度或者使用vh单位 */
}

.chart6 {
  width: 100%;
  /* 设置图表宽度为100% */
  height: 600px;
  /* 设置固定的高度或者使用vh单位 */
}

.chart7 {
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
  background-image: url('114771814_p0_master1200.jpg');
  /* Replace with the correct path to your image */
  background-size: cover;
  background-position: center;
  opacity: 0.5;
  /* Adjust opacity as needed */
  z-index: -1;
  /* Move the background behind the charts */
}
</style>
  
  