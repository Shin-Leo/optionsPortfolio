let butterfly = document.getElementById('butterfly').getContext('2d');
let condor = document.getElementById('condor').getContext('2d');
let strangle= document.getElementById('strangle').getContext('2d');
let straddle = document.getElementById('straddle').getContext('2d');

let green = butterfly.createLinearGradient(0, 0, 0, 300);
green.addColorStop(1, 'rgba(100, 100, 0,0)');
green.addColorStop(0, 'rgb(183,252,121)');

let red = butterfly.createLinearGradient(0, 0, 0, 300);
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
const dataLongCallButterfly = {
    labels: labels,
    datasets: [
        {
            label: 'Long Call Butterfly',
            backgroundColor: 'rgb(73,114,126)',
            borderColor: 'rgb(85,117,159)',
            data: [-30, -30, -30, 60, 150, 60, -30, -30, -30,],
            fill: false,
            radius: 0
        }]

};

const dataShortCallButterfly = {
    labels: labels,
    datasets: [
        {
            label: 'Short Call Butterfly',
            backgroundColor: 'rgb(73,114,126)',
            borderColor: 'rgb(85,117,159)',
            data: [60, 60, 60, 0, -60, 0, 60, 60, 60],
            fill: false,
            radius: 0
        }]

};

const dataLongStraddle = {
    labels: labels,
    datasets: [
        {
            label: 'Long Straddle',
            backgroundColor: 'rgb(73,114,126)',
            borderColor: 'rgb(85,117,159)',
            data: [60, 60, 60, 0, -60, 0, 60, 60, 60],
            fill: false,
            radius: 0
        }]

};

const dataShortStraddle = {
    labels: labels,
    datasets: [
        {
            label: 'Short Straddle',
            backgroundColor: 'rgb(73,114,126)',
            borderColor: 'rgb(85,117,159)',
            data: [60, 60, 60, 0, -60, 0, 60, 60, 60],
            fill: false,
            radius: 0
        }]

};
const dataLongStrangle = {
    labels: labels,
    datasets: [
        {
            label: 'Long Strangle',
            backgroundColor: 'rgb(73,114,126)',
            borderColor: 'rgb(85,117,159)',
            data: [60, 60, 60, 0, -60, 0, 60, 60, 60],
            fill: false,
            radius: 0
        }]

};
const dataShortStrangle = {
    labels: labels,
    datasets: [
        {
            label: 'Short Strangle',
            backgroundColor: 'rgb(73,114,126)',
            borderColor: 'rgb(85,117,159)',
            data: [60, 60, 60, 0, -60, 0, 60, 60, 60],
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
const butterflyConfig = {
    type: 'line',
    data: dataLongCallButterfly,
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
                let chartFill = butterflyChart.config._config.data.datasets[0]
                chartFill.fill = {
                    target: 'origin',
                    above: green,
                    below: red,
                }
                butterflyChart.update()
                setTimeout(function () {
                    fn(chartFill);
                }, 500)

                function fn(chartFill) {
                    chartFill.fill = false
                    butterflyChart.update()
                }
            }
        },
        legend: {
            display: false
         },
    }
}
const condorConfig = {
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
                let chartFill = condorChart.config._config.data.datasets[0]
                chartFill.fill = {
                    target: 'origin',
                    above: green,
                    below: red,
                }
                condorChart.update()
                setTimeout(function () {
                    fn(chartFill);
                }, 500)

                function fn(chartFill) {
                    chartFill.fill = false
                    condorChart.update()
                }

            }
        },
        legend: {
            display: false
         },
    }
}
const strangleConfig = {
    type: 'line',
    data: dataLongStraddle,
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
                let chartFill = strangleChart.config._config.data.datasets[0]
                chartFill.fill = {
                    target: 'origin',
                    above: green,
                    below: red,
                }
                strangleChart.update()
                setTimeout(function () {
                    fn(chartFill);
                }, 500)

                function fn(chartFill) {
                    chartFill.fill = false
                    strangleChart.update()
                }

            }
        },
        legend: {
            display: false
         },
    }
}
const straddleConfig = {
    type: 'line',
    data: dataLongStraddle,
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
                let chartFill = straddleChart.config._config.data.datasets[0]
                chartFill.fill = {
                    target: 'origin',
                    above: green,
                    below: red,
                }
                straddleChart.update()
                setTimeout(function () {
                    fn(chartFill);
                }, 500)

                function fn(chartFill) {
                    chartFill.fill = false
                    straddleChart.update()
                }

            }
        },
        legend: {
            display: false
         },
    }
}

let butterflyChart = new Chart(
    butterfly,
    butterflyConfig
)
let condorChart = new Chart(
    condor,
    condorConfig
);

let strangleChart = new Chart(
    strangle,
    strangleConfig
);

let straddleChart = new Chart(
    straddle,
    straddleConfig
);

let lcbButton = document.getElementById("long-call-butterfly")
let scbButton = document.getElementById("short-call-butterfly")


lcbButton.addEventListener('click', updateChart)
scbButton.addEventListener('click', updateChart)

function updateChart() {
    console.log(this.attributes.id.value)
    let id = this.attributes.id.value
    if (id === "short-call-butterfly") {
        butterflyChart.config.data = dataShortCallButterfly;
        butterflyChart.update()
    } else if (id === "long-put-butterfly") {

    } else if ( id === "short-put-butterfly") {

    } else if ( id === "long-call-butterfly") {
        butterflyChart.config.data = dataLongCallButterfly;
        butterflyChart.update()
    }
}



