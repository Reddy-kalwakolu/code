var svg = d3.select("svg"),
    margin = {top: 40, right: 20, bottom: 50, left: 70},
    width = +svg.attr("width") - margin.left - margin.right,
    height = +svg.attr("height") - margin.top - margin.bottom,
    g = svg.append("g").attr("transform", "translate(" + margin.left + "," + margin.top + ")");

var x = d3.scaleTime().range([0, width]),
    y = d3.scaleLinear().range([height, 0]);

var line = d3.line()
    .x(function(d) { return x(d.date); })
    .y(function(d) { return y(d.new_cases); });

var tooltip = d3.select(".tooltip");

d3.csv("data/covid_daily_new_cases.csv", function(d) {
    d.date = d3.timeParse("%Y-%m-%d")(d.date);
    d.new_cases = +d.new_cases;
    return d;
}).then(function(data) {
    x.domain(d3.extent(data, function(d) { return d.date; }));
    y.domain([0, d3.max(data, function(d) { return d.new_cases; })]);

    g.append("g")
        .attr("class", "axis axis--x")
        .attr("transform", "translate(0," + height + ")")
        .call(d3.axisBottom(x))
        .append("text")
        .attr("fill", "#000")
        .attr("x", width / 2)
        .attr("y", 35)
        .style("text-anchor", "middle")
        .text("Date");

    g.append("g")
        .attr("class", "axis axis--y")
        .call(d3.axisLeft(y).tickFormat(d3.format(".2s")))
        .append("text")
        .attr("fill", "#000")
        .attr("transform", "rotate(-90)")
        .attr("y", -50)
        .attr("x", -height / 2)
        .attr("dy", "0.71em")
        .style("text-anchor", "middle")
        .text("New Cases");

    g.append("path")
        .datum(data)
        .attr("class", "line")
        .attr("d", line);

    g.selectAll(".dot")
        .data(data)
        .enter().append("circle")
        .attr("class", "dot")
        .attr("cx", function(d) { return x(d.date); })
        .attr("cy", function(d) { return y(d.new_cases); })
        .attr("r", 3)
        .on("mouseover", function(event, d) {
            tooltip.transition()
                .duration(200)
                .style("opacity", .9);
            tooltip.html("Date: " + d3.timeFormat("%Y-%m-%d")(d.date) + "<br/>Cases: " + d.new_cases)
                .style("left", (event.pageX + 5) + "px")
                .style("top", (event.pageY - 28) + "px");
        })
        .on("mouseout", function(d) {
            tooltip.transition()
                .duration(500)
                .style("opacity", 0);
        });

    g.append("text")
        .attr("x", (width / 2))             
        .attr("y", 0 - (margin.top / 2))
        .attr("text-anchor", "middle")  
        .style("font-size", "16px") 
        .style("text-decoration", "underline")  
        .text("COVID-19 Daily New Cases Over Time");
});
