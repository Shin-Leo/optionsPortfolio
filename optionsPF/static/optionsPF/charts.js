var ctx1 = document.getElementById('chart1').getContext('2d');
var ctx2 = document.getElementById('chart2').getContext('2d');

var green = ctx1.createLinearGradient(0, 0, 0, 300);
green.addColorStop(1, 'rgba(100, 100, 0,0)');
green.addColorStop(0, 'rgb(183,252,121)');

var red = ctx1.createLinearGradient(0, 0, 0, 300);
red.addColorStop(1, 'rgba(210, 48, 48,0)');
red.addColorStop(0, 'rgb(255,96,96)');


const labels = [
    ' ',
    ' ',
    ' ',
    ' ',
    ' ',
    ' ',
    ' ',
    ' ',
    ' ',
];
const dataButterfly = {
    labels: labels,
    datasets: [
        {
            label: 'Long Butterfly Call',
            backgroundColor: 'rgb(73,114,126)',
            borderColor: 'rgb(85,117,159)',
            data: [-30, -30, -30, 60, 150, 60, -30, -30, -30,],
            fill: false,
            radius: 0
        }]

};
const dataCondor = {
    labels: labels,
    datasets: [
        {
            label: 'Long Butterfly Call',
            backgroundColor: 'rgb(73,114,126)',
            borderColor: 'rgb(85,117,159)',
            data: [-30, -30, -30, 60, 60, 60, -30, -30, -30,],
            fill: false,
                radius: 0

        }],
};
const config1 = {
    type: 'line',
    data: dataButterfly,
    options: {
        plugins: {
            autocolors: false,
            annotation: {
                annotations: {
                    line1: {
                        type: 'line',
                        yMin: 0,
                        yMax: 0,
                        borderColor: 'rgb(145,160,160)',
                        borderWidth: 2,
                    }
                }
            },
            id: 'myEventCatcher',
            events: ['hover'],
        legend: {
            display: false
         },
        },
        maintainAspectRatio: false,
        responsive: true,
        scales: {
            x: {
                display: true,
                title: {
                    display: true,
                    text: "underlying price"

                },
                grid: {
                    display: false
                }
                ,
                ticks: {
                    major: {
                        enabled: true
                    },
                    display: true
                }
            },
            y: {
                display: true,
                title: {
                    display: true,
                    text: 'profit / loss'

                },
                ticks: {
                    callback: function (val) {
                        return val === 0 ? this.getLabelForValue(val) : " ";
                    },
                    grid: {
                        display: false
                    }
                }
            },
        },
        onHover: (e, activeElements) => {
            if (e.type !== 'mouseout') {
                let chartFill = chart1.config._config.data.datasets[0]
                chartFill.fill = {
                    target: 'origin',
                    above: green,
                    below: red,
                }
                chart1.update()
                setTimeout(function () {
                    fn(chartFill);
                }, 500)

                function fn(chartFill) {
                    chartFill.fill = false
                    chart1.update()
                }

                console.log(activeElements)
            }
        },
        legend: {
            display: false
         },
    }
}
const config2 = {
    type: 'line',
    data: dataCondor,
    options: {
        plugins: {
            autocolors: false,
            annotation: {
                annotations: {
                    line1: {
                        type: 'line',
                        yMin: 0,
                        yMax: 0,
                        borderColor: 'rgb(145,160,160)',
                        borderWidth: 2,
                    }
                }
            },
            id: 'myEventCatcher',
            events: ['hover'],
        legend: {
            display: false
         },
        },
        maintainAspectRatio: false,
        responsive: true,
        scales: {
            x: {
                display: true,
                title: {
                    display: true,
                    text: "underlying price"

                },
                grid: {
                    display: false
                }
                ,
                ticks: {
                    major: {
                        enabled: true
                    },
                    display: true
                }
            },
            y: {
                display: true,
                title: {
                    display: true,
                    text: 'profit / loss'

                },
                ticks: {
                    callback: function (val) {
                        return val === 0 ? this.getLabelForValue(val) : " ";
                    },
                    grid: {
                        display: false
                    }
                }
            },
        },
        onHover: (e, activeElements) => {
            if (e.type !== 'mouseout') {
                let chartFill = chart2.config._config.data.datasets[0]
                chartFill.fill = {
                    target: 'origin',
                    above: green,
                    below: red,
                }
                chart2.update()
                setTimeout(function () {
                    fn(chartFill);
                }, 500)

                function fn(chartFill) {
                    chartFill.fill = false
                    chart2.update()
                }

            }
        },
        legend: {
            display: false
         },
    }
}

let chart1 = new Chart(
    ctx1,
    config1
)
let chart2 = new Chart(
    ctx2,
    config2
);



