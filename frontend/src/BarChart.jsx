BarChart.jsx
import { useEffect, useRef } from "react";
import * as d3 from "d3";

function BarChart({ data }) {

    const svgRef = useRef();

    useEffect(() => {

        const width = 800;
        const height = 500;

        d3.select(svgRef.current).selectAll("*").remove();

        const svg = d3
            .select(svgRef.current)
            .attr("width", width)
            .attr("height", height);

        const x = d3.scaleBand()
            .domain(data.map(d => d.Occupation))
            .range([50, width - 20])
            .padding(0.2);

        const y = d3.scaleLinear()
            .domain([0, d3.max(data, d => d.Number)])
            .nice()
            .range([height - 40, 20]);

        svg.selectAll("rect")
            .data(data)
            .enter()
            .append("rect")
            .attr("x", d => x(d.Occupation))
            .attr("y", d => y(d.Number))
            .attr("width", x.bandwidth())
            .attr("height", d => height - 40 - y(d.Number));

        svg.append("g")
            .attr("transform", `translate(0,${height-40})`)
            .call(d3.axisBottom(x))
            .selectAll("text")
            .attr("transform","rotate(-45)")
            .style("text-anchor","end");

        svg.append("g")
            .attr("transform","translate(50,0)")
            .call(d3.axisLeft(y));

    }, [data]);

    return <svg ref={svgRef}></svg>;
}

export default BarChart;