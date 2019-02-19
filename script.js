var chartnames=["School Type", "Program Length","Ethnicity"];
var selector = d3.select("#selDataset");
var chartdiv = d3.select("#chartdiv")

chartnames.forEach((chart) => {
    selector
      .append("option")
      .text(chart)
      .property("value", chart);
  });

  function optionChanged(chart) {
    chartdiv
    .html("")
    .append("img")
    .property("src", "Images/"+chart+".png");
    }