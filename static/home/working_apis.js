

  // ********************************
  // fetch data from google maps api
  function Fetch_google_api_data() {
    initAutocomplete();
  }
  function initAutocomplete() {
    // Create the autocomplete object, restricting the search to geographical
    // location types.
    autocomplete_pickup = new google.maps.places.Autocomplete(
        /** @type {!HTMLInputElement} **/(document.getElementById('pickup')),
        {types: ['geocode']});
  
    autocomplete_drop = new google.maps.places.Autocomplete(
        /** @type {!HTMLInputElement} **/(document.getElementById('drop')),
        {types: ['geocode']});
  
    autocomplete_drop = new google.maps.places.Autocomplete(
        /** @type {!HTMLInputElement} **/(document.getElementById('drop2')),
        {types: ['geocode']});
  
    autocomplete_drop = new google.maps.places.Autocomplete(
        /** @type {!HTMLInputElement} **/(document.getElementById('drop3')),
        {types: ['geocode']});
  
    // When the user selects an address from the dropdown, populate the address
    // fields in the form.
    autocomplete_pickup.addListener('place_changed', fillInAddress_pickup);
    autocomplete_drop.addListener('place_changed', fillInAddress_drop1);
    autocomplete_drop.addListener('place_changed', fillInAddress_drop2);
    autocomplete_drop.addListener('place_changed', fillInAddress_drop3);
  }
  
  function  fillInAddress_pickup() {
    // Get the place details from the autocomplete object.
    var place = autocomplete_pickup.getPlace();
    var latitude_pickup = place.geometry.location.lat();
    var longitude_pickup = place.geometry.location.lng();
  
    console.log(latitude_pickup)
    console.log(longitude_pickup)
  
    let pickUp_array = [latitude_pickup, longitude_pickup];
    // sessionStorage.setItem("pickUp_array",JSON.stringify(pickUp_array));
  
  }
  function  fillInAddress_drop1() {
    // Get the place details from the autocomplete object.
    var place = autocomplete_drop.getPlace();
    var latitude_drop = place.geometry.location.lat();
    var longitude_drop = place.geometry.location.lng();
    // console.log(latitude_drop)
    // console.log(latitude_drop)
  
    let drop_array = [latitude_drop, longitude_drop];
    // sessionStorage.setItem("drop_array",JSON.stringify(drop_array));
  
  }
  function  fillInAddress_drop2() {
    // Get the place details from the autocomplete object.
    var place = autocomplete_drop.getPlace();
    var latitude_drop = place.geometry.location.lat();
    var longitude_drop = place.geometry.location.lng();
    // console.log(latitude_drop)
    // console.log(latitude_drop)
  
    let drop_array = [latitude_drop, longitude_drop];
    // sessionStorage.setItem("drop_array",JSON.stringify(drop_array));
  
  }
  function  fillInAddress_drop3() {
    // Get the place details from the autocomplete object.
    var place = autocomplete_drop.getPlace();
    var latitude_drop = place.geometry.location.lat();
    var longitude_drop = place.geometry.location.lng();
    // console.log(latitude_drop)
    // console.log(latitude_drop)
  
    let drop_array = [latitude_drop, longitude_drop];
    // sessionStorage.setItem("drop_array",JSON.stringify(drop_array));
  
  }
  



  