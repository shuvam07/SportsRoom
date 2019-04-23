function checkAvailability(id){
	// alert(refId)
	var url='/sportsEquipment/checkAvailability/'
    $.ajax({
	    type : "POST", // http method
	    url : url, // the endpoint
	    data:{
	    	reqId: id,
	        csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
	    },
	    success : function(availability) {
	       console.log(id)
	       document.getElementById(id).firstElementChild.value=availability;
	    },
	    
	});
};