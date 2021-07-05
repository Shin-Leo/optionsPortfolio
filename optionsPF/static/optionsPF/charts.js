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
const data = {
    labels: labels,
    datasets: [{
        label: 'Long Butterfly Call',
        backgroundColor: 'rgb(73,114,126)',
        borderColor: 'rgb(85,117,159)',
        data: [-30, -30, -30, 60, 150, 60, -30, -30, -30,],
    }]
};
const config = {
    type: 'line',
    data,
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
            }
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
    }
}

let chart1 = new Chart(
    document.getElementById('chart1'),
    config
)
let chart2 = new Chart(
    document.getElementById('chart2'),
    config
);

