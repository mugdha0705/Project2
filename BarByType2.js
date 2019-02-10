//Sample chart text from Chart.js
console.log("Is this working?");
var ctx = document.getElementById("myChart").getContext('2d');
var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ["Graduate/Professional (≥ 300 hours)", "Non-Degree (600–899 hours)", "Non-Degree  (900–1799 hours)", "Non-Degree (1800–2699 hours)", "Non-Degree (≥ 2700 hours)", "Associate's", "Bachelor's", "First Professional Degree", "Master's or Doctor's",  "Two-Year Transfer"],
        datasets: [{
            label: 'Default Rates',
            data:  [2.9, 13.3, 12.6, 10.2, 7.8, 15.4, 11, 2.4, 6, 4.6],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                ],
            borderColor: [
                'rgba(255,99,132,1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero:true
                }
            }]
        }
    }
});