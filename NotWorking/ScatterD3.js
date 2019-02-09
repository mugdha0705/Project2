//Sample chart text from Chart.js

var GraphPoints = [];
d3.csv("College_Scatter.csv", function(data) {
    var Cost = data.map(data => data.NetPrice);
    var dRate = data.map(data => data.DefRate);
    console.log(Cost);
    console.log(dRate);
    // var GraphPoints = [];
    console.log("begin loop");

    for (var i=0; i<10; i++) {
        var AddPoint = {x:parseFloat(Cost[i]), y:Number(dRate[i])};
        // console.log(AddPoint);
        GraphPoints.push(AddPoint);
    };

    console.log("End Loop");
    
    //buildChart(GraphPoints)

});

//function buildChart(data){
    //console.log("from buildChart: ", data);
    var ctx = document.getElementById("myChart").getContext('2d');
    //var ctx = "scatterChart"
    var myChart = new Chart(ctx, {
        type: 'scatter',
        label:"Is This Working?",
        data: [{x:7,y:9},{x:8,y:6}],
        options: {
            scales: {
                xAxes: [{
                    type: 'linear',
                    position: 'bottom'
                }]
            }
        }
    });
 
//}



// //https://stackoverflow.com/questions/37533762/how-to-include-many-datapoints-to-plot-in-chart-js    



    
//     console.log("Fin!");



