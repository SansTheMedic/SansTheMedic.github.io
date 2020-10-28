
///// Loads the content for when page change occurs
function loadpage(aPagename,aPageLink) {

    // Removes alternate colouration for previously added page
    removeClasses();

    // Isolates the div for the content of the page
    var content_div = document.getElementById("content");

    // Following IF statements colour current page if it is one on the sidebar
    if (aPagename == "home") {
        aPageLink.classList.add("active");
        content_div.classList.remove("content");
        content_div.classList.add("backdrop");
    }
    else if (aPagename == "about") {
        aPageLink.classList.add("active");
        content_div.classList.add("content");
        content_div.classList.remove("backdrop");
    }
    else if (aPagename == "games") {
        aPageLink.classList.add("active");
        content_div.classList.add("content");
        content_div.classList.remove("backdrop");
    }
    else if (aPagename == "thinktank") {
        aPageLink.classList.add("active");
        content_div.classList.add("content");
        content_div.classList.remove("backdrop");
    }
    else if (aPagename == "blog") {
        aPageLink.classList.add("active");
        content_div.classList.add("content");
        content_div.classList.remove("backdrop");
    }
    else if (aPagename == "stuff") {
        aPageLink.classList.add("active");
        content_div.classList.add("content");
        content_div.classList.remove("backdrop");
    }

    // Loads the HTML content into the content div
    loadHTML(aPagename,content_div)
}


///// Removes active class from all sidebar page options
function removeClasses() {
    // All pages on sidebar
    var pages = ["home", "about", "games", "thinktank", "blog", "stuff"]

    // Iterates through all sidebar options
    for (var each_page of pages) {
        // Isolates element of the page options
        var this_page = document.getElementById(each_page);

        // Removes highlighting class if it exists, else this does nothing
        this_page.classList.remove("active");
    }
}


///// Calls for page content from server and puts it into the content div of the page
function loadHTML(aHTMLFragmentName, aContentElement) {
       // Get full name of page to load
       var html_filename = "\\pages\\" + aHTMLFragmentName + ".html";

       // Set up to load the HTML content by Ajax 
       ajax_request = new XMLHttpRequest();
   
       // Handle Ajax response
       ajax_request.onreadystatechange = function() {
   
         // Ajax returned  
         if (this.readyState == 4) {
   
           // Got the data  
           if (this.status == 200) {
   
            // Puts content into the div
            aContentElement.innerHTML = this.responseText;
           }

         }
       };
       
       // Call by Ajax    
       ajax_request.open("GET", html_filename, true);
       ajax_request.send();
}