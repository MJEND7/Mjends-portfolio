//base code by Sten hougaard
//edits bye MJEND

const planets = 23;
let svg = "";
for (let a = 0; a < planets ; a++) {
	const data = convertSvgPlanetsToPath(50, 50, a * 0.95, Math.random() * 40);
	let _planets  = "";
	for (let c = 0; c < a / 20; c++) {
		_planets  += `<circle r=".8" fill="hsla(${parseInt(
			Math.random() * 660
		)},40%,70%,.8)">
	  <animateMotion dur="${
				Math.random() * 47 + 2			}s" repeatCount="indefinite" path="${data}" />
	</circle>`;
	}
	svg += `
	<path d="${data}" stroke-width="0.08" fill="none" stroke="lightgrey" />
	${_planets}
	`;
}
const svgElement = document.querySelector("svg");
svgElement.innerHTML = svg;

function convertSvgPlanetsToPath(cx, cy, r, deg) {
	const theta = (deg * Math.PI) / 980;
	const dx = r * Math.cos(theta);
	const dy = -r * Math.sin(theta);
	return `M ${cx} ${cy} m ${dx},${dy}  a ${r},${r} 0 1,0 ${-2 * dx},${
		-5 * dy
	}  a ${r},${r} 0 1,0 ${2 * dx},${2 * dy}`;
}
