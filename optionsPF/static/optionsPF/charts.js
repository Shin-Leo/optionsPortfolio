let butterfly = document.getElementById('butterfly').getContext('2d');
let condor = document.getElementById('condor').getContext('2d');
let strangle= document.getElementById('strangle').getContext('2d');
let straddle = document.getElementById('straddle').getContext('2d');
let vertical = document.getElementById('vertical').getContext('2d');

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
            data: [60, 30, 0, -30, -60, -30, 0, 30, 60],
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
            data: [-60, -30, 0, 30, 60, 30, 0, -30, -60],
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
            data: [60, 0, -60, -60, -60, -60, -60, 0, 60],
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
            data: [-60, 0, 60, 60, 60, 60, 60, 0, -60],
            fill: false,
            radius: 0
        }]

};

const dataLongCondor = {
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
const dataShortCondor = {
    labels: labels,
    datasets: [
        {
            label: 'Long Butterfly Call',
            backgroundColor: 'rgb(73,114,126)',
            borderColor: 'rgb(85,117,159)',
            data: [30, 30, -15, -60, -60, -60, -15, 30, 30,],
            fill: false,
                radius: 0

        }],
};
const dataBullCallVertical = {
    labels: labels,
    datasets: [
        {
            label: 'Bull Call Vertical Spread',
            backgroundColor: 'rgb(73,114,126)',
            borderColor: 'rgb(85,117,159)',
            data: [-30, -30, -30, -15, 0, 15, 30, 30, 30],
            fill: false,
                radius: 0

        }],
};
const dataBullPutVertical = {
    labels: labels,
    datasets: [
        {
            label: 'Bull Put Vertical Spread',
            backgroundColor: 'rgb(73,114,126)',
            borderColor: 'rgb(85,117,159)',
            data: [30, 30, 30, 15, 0, -15,-30,-30, -30],
            fill: false,
                radius: 0

        }],
};
const dataBearCallVertical = {
    labels: labels,
    datasets: [
        {
            label: 'Bear Call Vertical Spread',
            backgroundColor: 'rgb(73,114,126)',
            borderColor: 'rgb(85,117,159)',
            data: [-30, -30, -30, -15, 0, 15, 30, 30, 30],
            fill: false,
                radius: 0

        }],
};
const dataBearPutVertical = {
    labels: labels,
    datasets: [
        {
            label: 'Bear Put Vertical Spread',
            backgroundColor: 'rgb(73,114,126)',
            borderColor: 'rgb(85,117,159)',
            data: [30, 30, 30, 15, 0, -15,-30,-30, -30],
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
    data: dataLongCondor,
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
    data: dataLongStrangle,
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
const verticalConfig = {
    type: 'line',
    data: dataBullCallVertical,
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
                let chartFill = verticalChart.config._config.data.datasets[0]
                chartFill.fill = {
                    target: 'origin',
                    above: green,
                    below: red,
                }
                verticalChart.update()
                setTimeout(function () {
                    fn(chartFill);
                }, 500)

                function fn(chartFill) {
                    chartFill.fill = false
                    verticalChart.update()
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

let verticalChart = new Chart(
    vertical,
    verticalConfig
)

let lcbButton = document.getElementById("long-call-butterfly")
let scbButton = document.getElementById("short-call-butterfly")
let longStrangleButton = document.getElementById("long-strangle")
let shortStrangleButton = document.getElementById("short-strangle")
let longCondorButton = document.getElementById("long-condor")
let shortCondorButton = document.getElementById("short-condor")
let longStraddleButton = document.getElementById("long-straddle")
let shortStraddleButton = document.getElementById("short-straddle")
let bullCallButton = document.getElementById("bull-call")
let bullPutButton = document.getElementById("bull-put")
let bearCallButton = document.getElementById("bear-call")
let bearPutButton = document.getElementById("bear-put")


lcbButton.addEventListener('click', updateChart)
scbButton.addEventListener('click', updateChart)
longStrangleButton.addEventListener('click', updateChart)
shortStrangleButton.addEventListener('click', updateChart)
longCondorButton.addEventListener('click', updateChart)
shortCondorButton.addEventListener('click', updateChart)
longStraddleButton.addEventListener('click', updateChart)
shortStraddleButton.addEventListener('click', updateChart)
bullCallButton.addEventListener('click', updateChart)
bullPutButton.addEventListener('click', updateChart)
bearCallButton.addEventListener('click', updateChart)
bearPutButton.addEventListener('click', updateChart)

function updateChart() {
    console.log(this.attributes.id.value)
    let id = this.attributes.id.value
    if (id === "short-call-butterfly") {
        butterflyChart.config.data = dataShortCallButterfly;
        console.log(document.querySelector("#form-table > div > div > div:nth-child(1) > div > div.card-body > h6"))
        document.querySelector("#form-table > div > div > div:nth-child(1) > div > div.card-body > h6").innerHTML = "Short Call Butterfly Spread"
        butterflyChart.update()
    } else if (id === "long-put-butterfly") {

    } else if ( id === "short-put-butterfly") {

    } else if ( id === "long-call-butterfly") {
        butterflyChart.config.data = dataLongCallButterfly;
        document.querySelector("#form-table > div > div > div:nth-child(1) > div > div.card-body > h6").innerHTML = "Long Call Butterfly Spread"
        butterflyChart.update()
    } else if (id === "short-strangle") {
        strangleChart.config.data = dataShortStrangle;
        strangleChart.update()
    } else if (id === "long-strangle") {
        strangleChart.config.data = dataLongStrangle;
        strangleChart.update()
    } else if (id === "long-condor") {
        condorChart.config.data = dataLongCondor;
        condorChart.update()
    } else if (id === "short-condor") {
        condorChart.config.data = dataShortCondor;
        condorChart.update()
    } else if (id === "long-straddle") {
        straddleChart.config.data = dataLongStraddle;
        straddleChart.update()
    } else if (id === "short-straddle") {
        straddleChart.config.data = dataShortStraddle;
        straddleChart.update()
    }else if (id === "bull-call") {
        verticalChart.config.data = dataBullCallVertical;
        verticalChart.update()
    }else if (id === "bull-put") {
        verticalChart.config.data = dataBullPutVertical;
        verticalChart.update()
    }else if (id === "bear-call") {
        verticalChart.config.data = dataBearCallVertical;
        verticalChart.update()
    }else if (id === "bear-put") {
        verticalChart.config.data = dataBearPutVertical;
        verticalChart.update()
    }
}



