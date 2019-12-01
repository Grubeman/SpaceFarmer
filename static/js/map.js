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

scaleX.domain([0, 50]);
scaleY.domain([0, 50]);

var point = {"x": 24, "y": 31}

// var poly = [{
//               "name": "polygon 1",
//               "points":[
//                 {"x":0.0, "y":25.0},
//                 {"x":8.5,"y":23.4},
//                 {"x":13.0,"y":21.0},
//                 {"x":19.0,"y":15.5}
//               ]
//             },
//             {
//               "name": "polygon 2",
//               "points":[
//                 {"x":0.0, "y":50.0},
//                 {"x":15.5,"y":23.4},
//                 {"x":18.0,"y":30.0},
//                 {"x":20.0,"y":16.5}
//               ]
//             }];
  
    svg.selectAll("polygon")
    .data(map_data)
    .enter().append("polygon")
    .attr("points",function(d) { 
          return d.points.map(function(d) { 
            console.log("test")
            return [scaleX(d.x),scaleY(d.y)].join(","); }).join(" ");})
      .attr("stroke","black")
      .attr("stroke-width",2); 

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