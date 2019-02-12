
// Create the Traces
var trace1 = {
    x: data.states,
    y: data.cc_debt,
    mode: "markers",
    type: "scatter",
    name: "CC_Debt",
    marker: {
      color: "#2077b4",
      symbol: "hexagram"
    }
  };
  
  var trace2 = {
    x: data.states,
    y: data.avg_std_loan_debt,
    mode: "markers",
    type: "scatter",
    name: "Avg_Std_Loan_Debt",
    marker: {
      color: "orange",
      symbol: "diamond-x"
    }
  };
  
  var trace3 = {
    x: data.states,
    y: data.avg_mortgage_debt,
    mode: "markers",
    type: "scatter",
    name: "Avg_Mortgage_Debt",
    marker: {
      color: "rgba(156, 165, 196, 1.0)",
      symbol: "cross"
    }
  };
  
  // Create the data array for the plot
  var data = [trace1, trace2, trace3];
  
  // Define the plot layout
  var layout = {
    title: "Loan Comparison",
    xaxis: { title: "States" },
    yaxis: { title: "Amount in Dollars" }
  };
  
  // Plot the chart to a div tag with id "plot"
  Plotly.newPlot("plot", data, layout);
  