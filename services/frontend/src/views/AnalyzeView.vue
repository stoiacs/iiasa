<template>
  <div>
    <select v-model="selectedScenario" @change="fetchParams">
      <option disabled value="">Select a Scenario</option>
      <option v-for="scenario in scenarios" :key="scenario">{{ scenario }}</option>
    </select>

    <select v-model="selectedItem" @change="fetchParams">
      <option disabled value="">Select an Item</option>
      <option v-for="item in items" :key="item">{{ item }}</option>
    </select>

    <select v-model="selectedVariable" @change="fetchData">
      <option disabled value="">Select a Variable</option>
      <option v-for="variable in variables" :key="variable">{{ variable }}</option>
    </select>

    <Line
        :options="chartOptions"
        :data="chartData"
    />
  </div>
</template>

<script>
import axios from 'axios'
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
  Colors
} from 'chart.js'
import autocolors from 'chartjs-plugin-autocolors';
import {Line} from 'vue-chartjs'

ChartJS.register(
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend,
    Colors,
    autocolors
)
export default {
  components: {
    Line
  },
  data() {
    return {
      variables: [],
      items: [],
      scenarios: [],
      chartData: {
        labels: [],
        datasets: []
      },
      chartOptions: {
        responsive: true
      }
    }
  },
  methods: {
    fetchParams() {
      axios.get('/csv-data/params', {
        params: {
          scenario: this.selectedScenario,
          item: this.selectedItem,
        }
      }).then(response => {
        this.items = response.data.items;
        this.variables = response.data.variables;

      }).catch(error => {
        console.error(error);
      });
    },
    fetchData() {
      axios.get('/csv-data', {
        params: {
          variable: this.selectedVariable,
          item: this.selectedItem,
          scenario: this.selectedScenario
        }
      }).then(response => {
        this.chartData = this.processData(response.data);
      }).catch(error => {
        console.error(error);
      });
    },
    processData(data) {
      let newChartData = {
        labels: [],
        datasets: []
      };
      data.forEach((item) => {
        if (!newChartData.labels.includes(item.Year)) {
          newChartData.labels.push(item.Year);
        }
        let dataset = newChartData.datasets.find((dataset) => dataset.label === item.Region);
        if (!dataset) {
          dataset = {
            label: item.Region,
            data: []
          }
          newChartData.datasets.push(dataset);
        }
        dataset.data.push(item.Value);
      });
      return newChartData;
    }
  },
  mounted() {
    this.scenarios = ["Base_cc26", "Base_cc70", "Resto_cc26", "Resto_cc70", "Restoprot_cc26", "Restoprot_cc70"]
    // axios.get('/csv-data/params').then(response => {
    //   this.scenarios = response.data.scenarios;
    //
    // }).catch(error => {
    //   console.error(error);
    // });
  }
}
</script>
