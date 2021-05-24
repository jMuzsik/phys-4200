import * as d3 from "d3";

export default function d3Code(svg, data, dots) {
  let margin = 15,
    height = 400 - 3 * margin,
    width = 400 - 3 * margin;

  var x = d3.scaleLinear().domain([0, 100]).range([0, width]);
  svg
    .append("g")
    .attr("transform", `translate(0, ${height})`)
    .call(d3.axisBottom(x));

  // Add Y axis
  var y = d3.scaleLinear().domain([0, 100]).range([height, 0]);
  svg.append("g").attr("transform", `translate(0, 0)`).call(d3.axisLeft(y));

  // compute the density data
  var densityData = d3
    .contourDensity()
    .x(function (d) {
      return x(d.x);
    }) // x and y = column name in .csv input data
    .y(function (d) {
      return y(d.y);
    })
    .size([width, height])
    .bandwidth(20)(data);

  // Add the contour: several "path"
  svg
    .selectAll("path")
    .data(densityData)
    .enter()
    .append("path")
    .attr("d", d3.geoPath())
    .attr("fill", "none")
    .attr("stroke", "#69b3a2")
    .attr("stroke-linejoin", "round");

  // Define the div for the tooltip
  var div = d3
    .select("body")
    .append("div")
    .attr("class", "tooltip")
    .style("opacity", 0);

  svg
    .append("g")
    .selectAll("dot")
    .data(dots)
    .enter()
    .append("circle")
    .attr("cx", function (d) {
      return x(d.x);
    })
    .attr("cy", function (d) {
      return y(d.y);
    })
    .attr("r", function (d) {
      return Math.abs(d.charge);
    })
    .on("mouseover", function (event, d) {
      d3.select(this)
        .transition()
        .duration("100")
        .attr("r", Math.abs(d.charge * 2));
      //Makes div appear
      div.transition().duration(100).style("opacity", 1);
      div
        .html(JSON.stringify(d))
        .style("left", event.pageX + 10 + "px")
        .style("top", event.pageY - 15 + "px");
    })
    .on("mouseout", function (event, d) {
      d3.select(this)
        .transition()
        .duration("200")
        .attr("r", Math.abs(d.charge));
      //makes div disappear
      div.transition().duration("200").style("opacity", 0);
    });
  // .style("fill", function (d) { return color() } )
}
