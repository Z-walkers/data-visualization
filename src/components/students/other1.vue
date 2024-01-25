<template>
  <div>

  <div chart-container>
    <div id="chart" class="chart"></div>
    <div class="image-title">评分与热度对比</div>
    <div id="chart1" class="chart1"></div>
    <div class="background-image"></div>
  </div>
</div>
</template>

<script>
import * as echarts from 'echarts'
import data1 from './worst.json'
import data2 from './bad.json'
import data3 from './soso.json'
import data4 from './good.json'
import data5 from './best.json'
export default {
  mounted() {
    this.drawChart();
    this.drawChart2(data1, data2, data3, data4, data5);
  },
  methods: {
    drawChart() {
      var ROOT_PATH = 'https://echarts.apache.org/examples';
      var chartDom = document.getElementById('chart');
      var myChart = echarts.init(chartDom);
      var option;

      var paperDataURI =
        'data:image/png;base64,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';
      option = {
        backgroundColor: '#0f375f',
        tooltip: {},
        legend: {
          textStyle: { color: '#ddd' }
        },
        xAxis: [
          {
            data: ['日本动画的蓝光碟摞起来', '', 'Qomolangma', 'Kilimanjaro'],
            axisTick: { show: false },
            axisLine: { show: false },
            axisLabel: {
              margin: 20,
              color: '#ddd',
              fontSize: 14
            }
          }
        ],
        yAxis: {
          splitLine: { show: false },
          axisTick: { show: false },
          axisLine: { show: false },
          axisLabel: { show: false }
        },
        markLine: {
          z: -1
        },
        animationEasing: 'elasticOut',
        series: [
          {
            title:'日本动画蓝光碟总数',
            type: 'pictorialBar',
            name: '单位：米',
            emphasis: {
              scale: true
            },
            label: {
              show: true,
              position: 'top',
              formatter: '{c} m',
              fontSize: 16,
              color: '#e54035'
            },
            data: [
              {
                value: 5000 * 1489 * 1.2 / 1000,
                symbol: 'image://' + paperDataURI,
                symbolRepeat: true,
                symbolSize: ['130%', '20%'],
                symbolOffset: [0, 10],
                symbolMargin: '-30%',
                animationDelay: function (dataIndex, params) {
                  return params.index * 30;
                }
              },
              {
                value: '-',
                symbol: 'none'
              },
              {
                value: 8844,
                symbol:
                  'image://' + ROOT_PATH + '/data/asset/img/hill-Qomolangma.png',
                symbolSize: ['200%', '105%'],
                symbolPosition: 'end',
                z: 10
              },
              {
                value: 5895,
                symbol:
                  'image://' + ROOT_PATH + '/data/asset/img/hill-Kilimanjaro.png',
                symbolSize: ['200%', '105%'],
                symbolPosition: 'end'
              }
            ],
            markLine: {
              symbol: ['none', 'none'],
              label: {
                show: false
              },
              lineStyle: {
                color: '#e54035',
                width: 2
              },
              data: [
                {
                  yAxis: 8848
                }
              ]
            }
          },
          {
            name: '',
            type: 'pictorialBar',
            barGap: '-100%',
            symbol: 'circle',
            itemStyle: {
              color: '#185491'
            },
            silent: true,
            symbolOffset: [0, '50%'],
            z: -10,
            data: [
              {
                value: 1,
                symbolSize: ['150%', 50]
              },
              {
                value: '-'
              },
              {
                value: 1,
                symbolSize: ['200%', 50]
              },
              {
                value: 1,
                symbolSize: ['200%', 50]
              }
            ]
          }
        ]
      };
      myChart.setOption(option);


    },
    drawChart2(worst, bad, soso, good, best) {
      var chartDom = document.getElementById('chart1');
      var myChart = echarts.init(chartDom);
      var option;
      function calculateAverage(data, dim) {
        let total = 0;
        for (var i = 0; i < data.length; i++) {
          total += data[i][dim];
        }
        return (total /= data.length);
      }
    
      const scatterOption = (option = {
        xAxis: {
          scale: true
        },
        yAxis: {
          scale: true
        },
        series: [
          {
            type: 'scatter',
            id: 'worst',
            dataGroupId: 'worst',
            universalTransition: {
              enabled: true,
              delay: function (idx, count) {
                return Math.random() * 400;
              }
            },
            data: worst
          },
          {
            type: 'scatter',
            id: 'bad',
            dataGroupId: 'bad',
            universalTransition: {
              enabled: true,
              delay: function (idx, count) {
                return Math.random() * 400;
              }
            },
            data: bad
          },
          {
            type: 'scatter',
            id: 'soso',
            dataGroupId: 'soso',
            universalTransition: {
              enabled: true,
              delay: function (idx, count) {
                return Math.random() * 400;
              }
            },
            data: soso
          },
          {
            type: 'scatter',
            id: 'good',
            dataGroupId: 'good',
            universalTransition: {
              enabled: true,
              delay: function (idx, count) {
                return Math.random() * 400;
              }
            },
            data: good
          },
          {
            type: 'scatter',
            id: 'best',
            dataGroupId: 'best',
            universalTransition: {
              enabled: true,
              delay: function (idx, count) {
                return Math.random() * 400;
              }
            },
            data: best
          }
        ]
      });
      const barOption = {
        xAxis: {
          type: 'category',
          data: ['worst', 'bad','soso','good','best']
        },
        yAxis: {},
        series: [
          {
            type: 'bar',
            id: 'total',
            data: [
              {
                value: calculateAverage(worst, 0),
                groupId: 'worst'
              },
              {
                value: calculateAverage(bad, 0),
                groupId: 'bad'
              },
              {
                value: calculateAverage(soso, 0),
                groupId: 'soso'
              },
              {
                value: calculateAverage(good, 0),
                groupId: 'good'
              },
              {
                value: calculateAverage(best, 0),
                groupId: 'best'
              }
            ],
            universalTransition: {
              enabled: true,
              seriesKey: ['worst', 'bad','soso','good','best'],
              delay: function (idx, count) {
                return Math.random() * 400;
              }
            }
          }
        ]
      };
      let currentOption = scatterOption;
      setInterval(function () {
        currentOption = currentOption === scatterOption ? barOption : scatterOption;
        myChart.setOption(currentOption, true);
      }, 20000);
      myChart.setOption(option);
    },
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.chart {
  width: 100%;
  /* 设置图表宽度为100% */
  height: 600px;
  /* 设置固定的高度或者使用vh单位 */
  top: 10%;
}

.chart1 {
  width: 100%;
  /* 设置图表宽度为100% */
  height: 600px;
  /* 设置固定的高度或者使用vh单位 */
  top: 50%;
}

.background-image {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: url('114541488_p0_master1200.jpg');
  /* Replace with the correct path to your image */
  background-size: cover;
  background-position: center;
  opacity: 0.5;
  /* Adjust opacity as needed */
  z-index: -1;
  /* Move the background behind the charts */
}
.image-title {
  position: absolute;
  top: 35%;
  left: 50%;
  transform: translateX(-50%);
  padding: 10px;
  font-weight: bold;
  font-size: 32px;
}
.chart-container {
  top : 10%; /* 在图表之间添加一些间距 */
}
</style>
