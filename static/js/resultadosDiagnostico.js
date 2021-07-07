const data = {
  labels: [
    'Finalidad, licitud y consentimiento',
    'Medidas de limitación',
    'Transparencia',
    'Decisiones automatizadas y perfilado',
    'Control de la información',
    'Evaluación de riesgos',
    'Otras prácticas',
  ],
  datasets: [{
    label: 'Media del sector',
    lineTension: 0.2,
    data: sector,
    fill: true,
    backgroundColor: 'rgba(255, 99, 132, 0.2)',
    borderColor: 'rgb(255, 99, 132)',
    pointBackgroundColor: 'rgb(255, 99, 132)',
    pointBorderColor: '#fff',
    pointHoverBackgroundColor: '#fff',
    pointHoverBorderColor: 'rgb(255, 99, 132)'
  },
  {
    label: '',
    lineTension: 0.2,
    data: [0,6,0,6,0,6,0,6,0,6,0,6,0,6],
    fill: true,
    backgroundColor: 'rgba(255, 99, 132, 0)',
    borderColor: 'rgba(255, 99, 132,0)',
    pointBackgroundColor: 'rgba(255, 99, 132,0)',
    pointBorderColor: '#fff',
    pointHoverBackgroundColor: '#fff',
    pointHoverBorderColor: 'rgb(255, 99, 132)',
  }
]
};
const data2 = {
  labels: [
    'Finalidad, licitud y consentimiento',
    'Medidas de limitación',
    'Transparencia',
    'Decisiones automatizadas y perfilado',
    'Control de la información',
    'Evaluación de riesgos',
    'Otras prácticas',
  ],
  datasets: [{
    label: 'Media del sector',
    lineTension: 0.2,
    data: sector,
    fill: true,
    backgroundColor: 'rgba(255, 99, 132, 0.2)',
    borderColor: 'rgb(255, 99, 132)',
    pointBackgroundColor: 'rgb(255, 99, 132)',
    pointBorderColor: '#fff',
    pointHoverBackgroundColor: '#fff',
    pointHoverBorderColor: 'rgb(255, 99, 132)',
  }, {
    label: 'Tus respuestas',
    data: respuestas,
    fill: true,
    lineTension: 0.2,
    backgroundColor: 'rgba(54, 162, 235, 0.2)',
    borderColor: 'rgb(54, 162, 235)',
    pointBackgroundColor: 'rgb(54, 162, 235)',
    pointBorderColor: '#fff',
    pointHoverBackgroundColor: '#fff',
    pointHoverBorderColor: 'rgb(54, 162, 235)'
  },
  ]
};
const config = {
  type: 'radar',
  data: data,
  options: {
    plugins: {
            legend: {
                labels: {
                    // This more specific font property overrides the global property
                    font: {
                        size: 24
                    }
                }
            }
        },
    scales: {
        r: {
          min: 0,
          max: 6,
          ticks: {
              stepSize: 1
          }
        }
    },
    responsive: false,
    maintainAspectRatio: false,
    plugins: {
      filler: {
        propagate: false
      },
      'samples-filler-analyser': {
        target: 'chart-analyser'
      }
    },
    interaction: {
      intersect: false
    }
  }
};
const config2 = {
  type: 'radar',
  data: data2,
  options: {
    plugins: {
            legend: {
                labels: {
                    // This more specific font property overrides the global property
                    font: {
                        size: 24
                    }
                }
            }
        },
    scales: {

        r: {
            min: 0,
            max: 6,
            ticks: {
                stepSize: 1
            }
        },
    },
    responsive: false,
    maintainAspectRatio: false,
    plugins: {
      filler: {
        propagate: false
      },
      'samples-filler-analyser': {
        target: 'chart-analyser'
      },
    },
    interaction: {
      intersect: false
    },
  }
};
// var myChart = new Chart(
//   document.getElementById('myChart'),
//   config
// );
var myChart2 = new Chart(
  document.getElementById('myChart2'),
  config2
);
console.log(respuestas)
