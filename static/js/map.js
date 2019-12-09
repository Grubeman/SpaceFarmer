var margin = {top: 20, right: 20, bottom: 30, left: 50},
width = 600 - margin.left - margin.right,
height = 500 - margin.top - margin.bottom;

var svg = d3.select("svg")
            .attr("width", width + margin.left + margin.right)
            .attr("height", height + margin.top + margin.bottom)
            .append("g")
            .attr("transform","translate(" + margin.left + "," + margin.top + ")");

var scaleX = d3.scaleLinear().range([0, width]);
var scaleY = d3.scaleLinear().range([height, 0]);

scaleX.domain([0, 100]);
scaleY.domain([0, 50]);

var point = {"x": 24, "y": 31}
  
    svg.selectAll(".field")
    .data(map_data.fields)
    .enter().append("polygon")
    .attr("class", "field")
    .attr("points",function(d) { 
          return d.points.map(function(d) { 
            return [scaleX(d.x),scaleY(d.y)].join(","); }).join(" ");})
      .style("stroke","black")
      .style("fill","grey")
      .style("stroke-width",2); 
      
      svg.selectAll(".road")
      .data(map_data.roads)
      .enter().append("polygon")
      .attr("class", "road")
      .attr("points",function(d) { 
            return d.segments.map(function(d) { 
              return [scaleX(d[0].x),scaleY(d[0].y)].join(",") +" "+[scaleX(d[1].x),scaleY(d[1].y)].join(","); }).join(" ");})
        .style("stroke","yellow")
        .style("stroke-width",7); 

        svg.selectAll(".road_center")
        .data(map_data.roads)
        .enter().append("polygon")
        .attr("class", "road_center")
        .attr("points",function(d) { 
              return d.segments.map(function(d) { 
                return [scaleX(d[0].x),scaleY(d[0].y)].join(",") +" "+[scaleX(d[1].x),scaleY(d[1].y)].join(","); }).join(" ");})
          .style("stroke","black")
          .style("stroke-dasharray", "5, 3") 
          .style("stroke-width",1); 

  svg.append("circle")
    .attr("r", 4)
    .attr("cx", scaleX(point.x))
    .attr("cy", scaleY(point.y))
  
    // add the X Axis
  svg.append("g")
    .attr("transform", "translate(0," + height + ")")
    .call(d3.axisBottom(scaleX));

  // add the Y Axis
  svg.append("g")
    .call(d3.axisLeft(scaleY));