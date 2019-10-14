var draw_crop_graph = function (svg, crop_data, prop) {
    var max = d3.max(crop_data, function(d) { return +d[prop];} );

    let yScale = d3.scaleLinear()
    .domain([0, max]) // input 
    .range([height, 0]); // output 

    // 7. d3's line generator
    let line = d3.line()
        .x(function(d, i) { return xScale(i); }) // set the x values for the line generator
        .y(function(d) { return yScale(d[prop]); }) // set the y values for the line generator 
        .curve(d3.curveMonotoneX) // apply smoothing to the line    

// 3. Call the x axis in a group tag
svg.append("g")
    .attr("class", "x axis")
    .attr("transform", "translate(0," + height + ")")
    .call(d3.axisBottom(xScale)); // Create an axis component with d3.axisBottom
    
// 4. Call the y axis in a group tag
svg.append("g")
.attr("class", "y axis")
.call(d3.axisLeft(yScale)); // Create an axis component with d3.axisLeft

// 9. Append the path, bind the data, and call the line generator 
svg.append("path")
    .datum(crop_data) // 10. Binds data to the line 
    .attr("class", "line") // Assign a class for styling 
    .attr("d", line); // 11. Calls the line generator 

    // 12. Appends a circle for each datapoint 
svg.selectAll(".dot")
.data(crop_data)
.enter().append("circle") // Uses the enter().append() method
.attr("class", "dot") // Assign a class for styling
.attr("cx", function(d, i) { return xScale(i) })
.attr("cy", function(d) { return yScale(d[prop]) })
.attr("r", 5);
}