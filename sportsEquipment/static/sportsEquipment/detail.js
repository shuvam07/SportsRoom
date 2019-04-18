function checkAvailability(clicked_id){
	var refId=clicked_id
	// alert(refId)
	var url='/sportsEquipment/checkAvailability/'
    $.ajax({
	    type : "POST", // http method
	    url : url, // the endpoint
	    data:{
	    	reqId: refId,
	        csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
	    },
	    success : function(availability) {
	       document.getElementById("here").value=availability;
	    },
	    
	});
};