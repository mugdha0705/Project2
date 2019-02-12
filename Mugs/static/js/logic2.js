
function buildCharts(region) {
  console.log("Hello world")
  
    // @TODO: Use `d3.json` to fetch the sample data for the plots
    d3.json(`/loans/${region}`).then(function(selection) {
      //console.log(selection);
      

      const states = selection.States;
      const defaults = selection.Defaults;
      const loan = selection.Loans;
      const defrate = selection.DefRate;
      console.log("region: ", region)
      
      //////////////////////////////////////////////////////////////
      // Build Pie Chart for genre
      var pieData = [{
        values: loans,
        labels: states,
        hoverinfo: loans,
        type: "pie"
      }];
  
      var pieLayout = {
        margin: {t: 0, 1: 0}
      };
    
      Plotly.plot("pie1", pieData, pieLayout);
  
      //////////////////////////////////////////////////////////////
    //   // Build a Bar Chart for genre
    //   var genreData = [{
    //     x: genre,
    //     y: region,
    //     type: "bar",
    //     transforms: [{
    //       type: 'aggregate',
    //       groups: genre,
    //       aggregations: [
    //         {target: 'y', func: 'sum', enabled: true},
    //       ]
    //     }]
    //   }];
      
    //   var genreLayout = {
    //     //title: 'Sales by Genre',
    //     margin: {t: 0}
    //   };
  
    //   Plotly.plot("bar1", genreData, genreLayout);
      
    //   //////////////////////////////////////////////////////////////
    //   // Build a Bar Chart for publisher
    //   var pubData = [{
    //     x: publisher,
    //     y: region,
    //     type: "bar",
    //     transforms: [{
    //       type: 'aggregate',
    //       groups: publisher,
    //       aggregations: [
    //         {target: 'y', func: 'sum', enabled: true},
    //       ]
    //     }]
    //   }];
      
    //   var pubLayout = {
    //     //title: 'Sales by Genre',
    //     margin: {t: 0},
    //     xaxis: {range: [-.5, 10.5]}
    //   };
  
    //   Plotly.plot("bar2", pubData, pubLayout);
  
    //   //////////////////////////////////////////////////////////////
    //   // Build a Bar Chart for platform
    //   var platformData = [{
    //     x: platform,
    //     y: region,
    //     type: "bar",
    //     transforms: [{
    //       type: 'aggregate',
    //       groups: platform,
    //       aggregations: [
    //         {target: 'y', func: 'sum', enabled: true},
    //       ]
    //     }]
    //   }];
      
    //   var platformLayout = {
    //     //title: 'Sales by Genre',
    //     margin: {t: 0},
    //     // xaxis: {range: [-.5, 10.5]}
    //   };
  
    //   Plotly.plot("bar3", platformData, platformLayout);
  
  
    //   //////////////////////////////////////////////////////////////
    //   // Build Pie Chart for rating
    //   var ratingData = [{
    //     values: region,
    //     labels: rating,
    //     hoverinfo: rating,
    //     type: "pie"
    //   }];
  
    //   var ratingLayout = {
    //     margin: {t: 0, 1: 0}
    //   };
    
    //   Plotly.plot("pie2", ratingData, ratingLayout);
  
  
    // //////////////////////////////////////////////////////////////
    // // Critic & User Scores scatter plots
    //   // Plot critic score
    //   var criticData = [{
    //     x: critic_score,
    //     y: region,
    //     mode: "markers",    
    //     type: "scatter"
    //   }];
  
    //   var criticLayout = {
    //     title: 'Sales by Genre',
    //     margin: {t: 0},
    //     yaxis: {range: [0, 42]}
    //   };
  
    //   Plotly.plot("plot1", criticData, criticLayout);
  
    //   // // Plot user score
    //   var userData = [{
    //     x: user_score,
    //     y: region,
    //     mode: "markers",    
    //     type: "scatter"
    //   }];
  
    //   var userLayout = {
    //     //title: 'Sales by Genre',
    //     margin: {t: 0},
    //     yaxis: {range: [0, 42]}
    //   };
  
    //   Plotly.plot("plot2", userData, userLayout);
  
  
  
    // });
  }
  
  
  
  
  
  function init() {
    // Grab a reference to the dropdown select element
    var selector = d3.select("#selDataset");
  
    // Use the list of sample names to populate the select options
    d3.json("/region").then((regionName) => {
      regionName.forEach((region) => {
        selector
          .append("option")
          .text(region)
          .property("value", region);
      });
      
      // Use the first sample from the list to build the initial plots --MAYBE MAKE GLOBAL SALES FIRST OPTION?
      const firstRegion = regionName[0];
      buildCharts(firstRegion);
    });
  }
  
  function optionChanged(newRegion) {
    Plotly.purge("pie1");
    Plotly.purge("pie2");
    Plotly.purge("bar1");
    Plotly.purge("bar2");
    Plotly.purge("bar3");
    Plotly.purge("plot1");
    Plotly.purge("plot2");
    // Fetch new data each time a new sample is selected
    buildCharts(newRegion);
  }
  
  // Initialize the dashboard
  init();
  