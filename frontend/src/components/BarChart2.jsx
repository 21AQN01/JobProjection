BarChart2.jsx;
import { useEffect, useRef } from "react";
import * as d3 from "d3";

function BarChart2({ data }) {
  const svgRef = useRef();

  useEffect(() => {
    const width = 900;
    const height = data.length * 35 + 50;

    const margin = {
      top: 40,
      right: 30,
      bottom: 40,
      left: 300,
    };

    d3.select(svgRef.current).selectAll("*").remove();

    const svg = d3
      .select(svgRef.current)
      .attr("width", width)
      .attr("height", height);

    // X scale (Median Wage)
    const x = d3
      .scaleLinear()
      .domain([0, d3.max(data, (d) => d.EARN_MDN_4YR_NAT)])
      .nice()
      .range([margin.left, width - margin.right]);

    // Y scale (Education names)
    const y = d3
      .scaleBand()
      .domain(data.map((d) => d.CIPDESC))
      .range([margin.top, height - margin.bottom])
      .padding(0.2);

    // Draw bars
    svg
      .selectAll("rect")
      .data(data)
      .join("rect")
      .attr("x", margin.left)
      .attr("y", (d) => y(d.CIPDESC))
      .attr("width", (d) => x(d.EARN_MDN_4YR_NAT) - margin.left)
      .attr("height", y.bandwidth());

    //Add title
    svg
      .append("text")
      .attr("x", width / 2)
      .attr("y", 20)
      .attr("text-anchor", "middle")
      .style("font-size", "20px")
      .style("font-weight", "bold")
      .text("Top 10 Major by Median Wage");

    // X axis
    svg
      .append("g")
      .attr("transform", `translate(0,${height - margin.bottom})`)
      .call(d3.axisBottom(x));
    // X-axis label
    svg
      .append("text")
      .attr("x", (margin.left + width - margin.right) / 2)
      .attr("y", height - 5)
      .attr("text-anchor", "middle")
      .text("Median Wage (USD)");

    // Y axis
    svg
      .append("g")
      .attr("transform", `translate(${margin.left},0)`)
      .call(d3.axisLeft(y));
  }, [data]);

  return <svg ref={svgRef}></svg>;
}

export default BarChart2;
