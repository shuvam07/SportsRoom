function del(clicked_id){
	var eqpId=clicked_id
	// alert(refId)
	var url='/sportsEquipment/deleteEquip/'
    $.ajax({
	    type : "POST", // http method
	    url : url, // the endpoint
	    data:{
	    	eqpId: eqpId,
	        csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
	    },
	    success : function() {
	       // document.getElementById("here").value=availability;
	    },
	    
	});
};