$(document).ready(function() {
    // Show the modal after 15 seconds of page load
    setTimeout(function() {
      $('#enquiryModal').modal('show');
    }, 60000);
  
    // Hide the modal and set a cookie when the cancel button is clicked
    $('#enquiryModal button[data-dismiss="modal"]').click(function() {
      // Set a cookie with a 1-day expiration
      document.cookie = "enquiryModalShown=true; expires=" + new Date(new Date().getTime() + (24 * 60 * 60 * 1000)).toUTCString();
  
      // Hide the modal
      $('#enquiryModal').modal('hide');
    });
  
    // Check if the cookie exists and show/hide the modal accordingly
    if (document.cookie.indexOf("enquiryModalShown=true") >= 0) {
      // The cookie exists, hide the modal
      $('#enquiryModal').modal('hide');
    } else {
      // The cookie doesn't exist, show the modal
      $('#enquiryModal').modal('show');
    }
    // Hide the modal and set a cookie when the cancel button is clicked
    $('#enquiryModal button[data-dismiss="modal"]').click(function() {
        console.log("Cancel button clicked");
        // Set a cookie with a 1-day expiration
        document.cookie = "enquiryModalShown=true; expires=" + new Date(new Date().getTime() + (24 * 60 * 60 * 1000)).toUTCString();
    });
  });



 



