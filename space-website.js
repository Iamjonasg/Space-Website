var launchdata = JSON.parse(data);
console.log(launchdata);
var pieExists = false;


$(document).ready(function() {
	createPie()

	$("#lancer").click(function(){
		createPie();
	});
});


function createPie(){
	
	if (pieExists) {
		piechart.destroy();
		
	}



	piechart = new Chart($('#pie-chart'), {
		type: 'pie',
		data: {
			labels: ["Success", "Failure", "Other"],
			datasets: [{
				data: [155, 5, 3],
				backgroundColor:['green','red','grey']	
			  }]

		}
	  });
	pieExists = true;
	
	
}


