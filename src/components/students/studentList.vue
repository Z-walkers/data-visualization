<template>
  <div chart-container>
    <el-input v-model="searchValue" placeholder="Enter search value"></el-input>
    <el-button @click="search">Search</el-button>
    <el-button @click="searchInGoogle">Search in wikipedia</el-button>
    <el-button @click="searchInNetflix">Search in Netflix</el-button>
    <div id="chart" class="chart"></div>
    <div class="image-title">动画封面</div>
   <div class="image-container"> 
      <img :src="imageUrl" alt="Image" v-if="imageUrl">
    </div>
    <el-button @click="changing">change</el-button>
    <div class="background-image"></div>
  </div>
</template>

<script>
import * as echarts from 'echarts';
import jsonData from './processed.json';
var i = 0;
console.log(this.chartData);
export default {
  data() {
    return {
      searchValue: '',
      chartData: [],
      imageUrl: null,
    };
  },
  create() {
    this.drawChart();
  },
  methods: {
    drawChart() {
      var chartDom = document.getElementById('chart');
      var myChart = echarts.init(chartDom);
      var option, option2;
      option = {
        title: {
          text: '动画评分雷达图',
          left: '40%'
        },
        legend: {
          data: ['评分']
        },
        radar: {
          indicator: [
            { name: 'Overall', max: 10 },
            { name: 'Story', max: 10 },
            { name: 'Animation', max: 10 },
            { name: 'Sound', max: 10 },
            { name: 'Character', max: 10 },
            { name: 'Enjoyment', max: 10 }
          ]
        },
        toolbox: {
          show: true,
          feature: {
            magicType: { type: ['radar', 'bar'] }
          }
        },
        series: [
          {
            name: '动画评分',
            type: 'radar',
            data: [
              {
                value: this.chartData,
                name: '评分'
              },
            ]
          }
        ]
      };
      option2 = {
        title: [
          {
            text: '动画评分',
            left: '40%'
          }
        ],
        polar: {
          radius: [30, '80%']
        },
        radiusAxis: {
          max: 10
        },
        angleAxis: {
          type: 'category',
          data: ['Overall', 'Story', 'Animation', 'Sound', 'Character', 'Enjoyment'],
          startAngle: 75
        },
        tooltip: {},

        series: {
          type: 'bar',
          data:  this.chartData,
          
          coordinateSystem: 'polar',
          label: {
            show: true,
            position: 'middle',
            formatter: '{b}: {c}'
          }
        },
        animation: true
      };
      if (i % 2 == 0)
        myChart.setOption(option);
      else
        myChart.setOption(option2);
    },
    search() {
      const result = this.processData(jsonData, this.searchValue);
      if (result) {
        this.chartData = result.chartData;
        this.imageUrl = result.imageUrl;
      } else {
        alert('找不到数据');
      }
      this.drawChart();
    },
    searchInGoogle() {
      if (this.searchValue) {
        const googleUrl = `https://en.wikipedia.org/wiki/${encodeURIComponent(this.searchValue)}`;
        window.open(googleUrl, '_blank'); // Opens a new tab or window
      } else {
        alert('Please enter a search value.');
      }
    },
    searchInNetflix() {
      if (this.searchValue) {
        const netflixUrl = `https://www.netflix.com/search?q=${encodeURIComponent(this.searchValue)}`;
        window.open(netflixUrl, '_blank'); // Opens a new tab or window
      } else {
        alert('Please enter a search value.');
      }
    },
    processData(data, searchValue) {
      var filteredData = data.filter(item => item[Object.keys(item)[7]] === searchValue);

      if (filteredData.length > 0) {
        var array1 = Object.values(filteredData[0]).slice(1, 7);
        var array = array1.map(parseFloat);
        var imageUrl = filteredData[0][Object.keys(filteredData[0])[15]];
        console.log(array);
        return { chartData: array, imageUrl: imageUrl };
      } else {
        console.log('No matching result found.');
        return null;
      }
    },
    changing() {
      i++;
      var chartDom = document.getElementById('chart');
      var myChart = echarts.init(chartDom);
      myChart.clear();
      this.drawChart();
    }
  }
};
</script>
  
<style scoped>
.chart-container {
  display: flex;
  flex-direction: column;
  width: 100%;
}

.chart {
  width: 100%;
  height: 600px;
}

.image-container {
  margin-top: 20px;

}

img {
  max-width: 100%;
  max-height: 300px;
  position: absolute;
  top: 30%;
  /* 垂直方向上居中 */
  left: 20%;
  /* 水平方向上居中 */
}
.image-title {
  position: absolute;
  top: 20%;
  left: 25%;
  transform: translateX(-50%);
  padding: 10px;
  font-weight: bold;
  font-size: 32px;
}
.background-image {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: url('knd.jpg'); /* Replace with the correct path to your image */
  background-size: cover;
  background-position: center;
  opacity: 0.5; /* Adjust opacity as needed */
  z-index: -1; /* Move the background behind the charts */
}
</style>
  