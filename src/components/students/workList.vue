<template>
  <div>
    <div>
    <el-row>
      <el-col :span="24">
        <el-card class="chart-container" style="border-radius: 10px; box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1); background-color: rgba(255, 255, 255, 0.8);">
          <div id="chart" class="chart"></div>
        </el-card>
      </el-col>
      <el-col :span="12">
        <el-card class="chart-container chart2-container" style="border-radius: 10px; box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1); background-color: rgba(255, 255, 255, 0.8);">
          <div id="chart2" class="chart2"></div>
        </el-card>
      </el-col>
      <el-col :span="12">
        <el-card class="chart-container chart3-container" style="border-radius: 10px; box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1); background-color: rgba(255, 255, 255, 0.8);">
          <div id="chart3" class="chart3"></div>
        </el-card>
      </el-col>
    </el-row>
  </div>
    <div class="background-image"></div>
  </div>
</template>

<script>
import * as echarts from 'echarts';
import jsonData from './tagtime.json';
import tagsdata from './tags.json';
import popdata from './pop.json';

export default {
  mounted() {
    this.drawChart(jsonData);
    this.drawChart2(tagsdata);
    this.drawChart3(popdata);
  },

  methods: {
    drawChart(_rawData) {
      var chartDom = document.getElementById('chart');
      var myChart = echarts.init(chartDom);
      var option;
      const Types = [
        'Comedy',
        'Action',
        'Fantasy',
        'Adventure',
        'Sci-Fi',
        'Drama',
        'Kids',
        'Shounen',
        'Music',
        'Romance'
      ];
      const datasetWithFilters = [];
      const seriesList = [];
      echarts.util.each(Types, function (Type) {
        var datasetId = 'dataset_' + Type;
        datasetWithFilters.push({
          id: datasetId,
          fromDatasetId: 'dataset_raw',
          transform: {
            type: 'filter',
            config: {
              and: [
                { dimension: 'Type', '=': Type }
              ]
            }
          }
        });
        seriesList.push({
          type: 'line',
          datasetId: datasetId,
          showSymbol: false,
          name: Type,
          endLabel: {
            show: true,
            formatter: function (params) {
              return params.value[0] + ': ' + params.value[2];
            }
          },
          labelLayout: {
            moveOverlap: 'shiftY'
          },
          emphasis: {
            focus: 'series'
          },
          encode: {
            x: 'Time',
            y: 'numbers',
            label: ['Type', 'numbers'],
            itemName: 'Time',
            tooltip: ['numbers']
          }
        });
      });
      option = {
        animation: true,
        animationDuration: 10000,
        dataset: [
          {
            id: 'dataset_raw',
            source: _rawData
          },
          ...datasetWithFilters
        ],
        title: {
          text: '动画种类变化情况',
          left: '40%',
        },
        tooltip: {
          order: 'valueDesc',
          trigger: 'axis'
        },
        xAxis: {
          type: 'category',
          nameLocation: 'middle'
        },
        yAxis: {
          name: 'numbers'
        },
        grid: {
          right: 140
        },
        series: seriesList
      };

      myChart.setOption(option);
      myChart.dispatchAction({
        type: 'showTip',
        seriesIndex: 0,
        dataIndex: 0
      });
    },

    drawChart2(data) {
      var chartDom = document.getElementById('chart2');
      var myChart2 = echarts.init(chartDom);
      var option;
      var arrey1 = Object.values(data)
      var arrey2 = Object.keys(data)
      const seriesdata = Object.entries(data).map(([name, value]) => ({ name, value }));
      console.log(seriesdata)
      option = {
        title: {
          text: '类型统计',
          left: 'center'
        },
        tooltip: {
          trigger: 'item',
          formatter: '{a} <br/>{b} : {c} ({d}%)'
        },
        legend: {
          type: 'scroll',
          orient: 'vertical',
          right: 10,
          top: 20,
          bottom: 20,
          data: arrey2
        },
        series: [
          {
            name: '类型',
            type: 'pie',
            radius: '55%',
            center: ['40%', '50%'],
            data: seriesdata,
            emphasis: {
              itemStyle: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: 'rgba(0, 0, 0, 0.5)'
              }
            }
          }
        ]
      };
      myChart2.setOption(option);
    },
    drawChart3(data) {
  var chartDom = document.getElementById('chart3');
  var myChart3 = echarts.init(chartDom);
  var option;
  var arrey1 = Object.values(data);
  var arrey2 = Object.keys(data);

  myChart3.on('click', function(params) {
    var clickedLabel = params.name;
    var wikiLink = 'https://en.wikipedia.org/wiki/' + encodeURIComponent(clickedLabel);
    window.open(wikiLink, '_blank');
  });

  option = {
    title: [
      {
        text: '三十年来最受欢迎的动画',
        left: '40%'
      }
    ],
    polar: {
      radius: [30, '80%']
    },
    angleAxis: {
      max: 2000000,
      startAngle: 75
    },
    radiusAxis: {
      type: 'category',
      data: arrey2,
    },
    tooltip: {},
    series: {
      type: 'bar',
      data: arrey1,
      coordinateSystem: 'polar',
      label: {
        show: true,
        position: 'middle',
        formatter: '{b}: {c}'
      }
    }
  };
  myChart3.setOption(option);
}

  },
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

.chart3 {
  width: 100%;
  /* 设置图表宽度为100% */
  height: 600px;
  /* 设置固定的高度或者使用vh单位 */
}

.chart-container {
  margin-bottom: 20px; /* 在图表之间添加一些间距 */
}

.chart2-container {
  margin-right: 20px; /* 调整 chart2-container 右侧间距 */
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
}</style>

