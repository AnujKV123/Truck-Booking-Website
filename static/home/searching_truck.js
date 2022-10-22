let map;

// handling popup of logout
window.addEventListener('click', (e) => {
  if (document.querySelector("#containerUserIMG").contains(e.target)) {
    // Clicked in box
    document.querySelector(".containerPicUserDTL").style.display = "block";
  } else {
    // Clicked outside the box
    document.querySelector(".containerPicUserDTL").style.display = "none";
  }
});

function initMap() {
  setTimeout(DisplayPoup,1000);
  setTimeout(ClosePoup,10000);
  fetch("http://127.0.0.1:8000/API/ShowMap/", {
	
    // Adding method type
    method: "GET",
  }).then(response => response.json())
  // Converting to JSON
  
  
  // Displaying results to console
  .then((data) => {
    const Pickup = data[0]['pickupL']
    const Drop = data[0]['dropL']
    const Drop2 = data[0]['drop2L']
    const Drop3 = data[0]['drop3L']
 
    var origin = Pickup
    const Waypath = [];
    if(Drop3 == '' && Drop2 != ''){
      var destination = Drop2;
      Waypath.push({ location: Drop})
    }
    else if(Drop3 != '' && Drop2 != ''){
      var destination = Drop3;
      Waypath.push({ location: Drop})
      Waypath.push({ location: Drop2})
    }
    else {
      var destination = Drop;
    }
 
    map = new google.maps.Map(document.getElementById("map"), {
     center: { lat: 23.491171, lng: 85.47867 },
     zoom: 1,
     disableDefaultUI: true,
     options: {
      gestureHandling: 'greedy'
    }
   });
   map.setOptions({
     minZoom: 8,
     maxZoom: 20
  });
   const directionsService = new google.maps.DirectionsService();
 
   const directionsRenderer = new google.maps.DirectionsRenderer({
     draggable: true,
     map,
     // panel: document.getElementById("right-panel"),
   });
 
   directionsRenderer.addListener("directions_changed", () => {
     computeTotalDistance(directionsRenderer.getDirections());
   });
 
   displayRoute(
     origin,
     destination,
     directionsService,
     directionsRenderer,
     Waypath
   );
  });

}

function displayRoute(origin, destination, service, display, Waypath) {
  console.log(Waypath)
  service.route(
    {
      origin: origin,
      destination: destination,
      waypoints:Waypath,
      // waypoints: [
      //   { location: "Ratu Road, Shahdeo Nagar, Panchsheel Colony, Ranchi, Jharkhand, India" },
      //   { location: "Patratu Dam, Labga, Jharkhand" },
      // ],
      travelMode: google.maps.TravelMode.DRIVING,
      avoidTolls: true,
    },
    (result, status) => {
      if (status === "OK" && result) {
        display.setDirections(result);
      } else {
        alert("Could not display directions due to: " + status);
      }
    }
  );
}

function computeTotalDistance(result) {
  let total = 0;
  const myroute = result.routes[0];
  console.log(myroute)
  
  if (!myroute) {
    return;
  }

  for (let i = 0; i < myroute.legs.length; i++) {
    total += myroute.legs[i].distance.value;
  }

  total = total / 1000;
  T_id = sessionStorage.getItem('id')
  sessionStorage.setItem('dX',total)
  document.getElementById("data101w").innerHTML = '<b>Distance :- </b><p id="total">'+ total + " km"+'</p>';

  if(sessionStorage.getItem('Rdx') == 1){
    const originX_lat = myroute.legs[0].start_location.lat()
    const originX_lng = myroute.legs[0].start_location.lng()
    const destinationX_lat = myroute.legs[0].end_location.lat()
    const destinationX_lng = myroute.legs[0].end_location.lng()

    const originX = myroute.legs[0].start_address
    const destinationX = myroute.legs[0].end_address
    const wayapoint = 'zero'
    sessionStorage.setItem("wxp", wayapoint)
    document.getElementById("data101x").innerHTML = '<b>pickup location :- </b><p id="p1">'+ originX+ " " + '</p><b> drop location :- </b><p id="d1">'+destinationX+'</p>';
    
  }

  else if(sessionStorage.getItem('Rdx') == 2){
    const originX_lat = myroute.legs[0].start_location.lat()
    const originX_lng = myroute.legs[0].start_location.lng()
    const destinationX_lat = myroute.legs[1].end_location.lat()
    const destinationX_lng = myroute.legs[1].end_location.lng()
    const wayapathX1_lat = myroute.legs[1].start_location.lat()
    const wayapathX1_lng = myroute.legs[1].start_location.lng()

    const originX = myroute.legs[0].start_address
    const destinationX = myroute.legs[1].end_address
    const wayapathX1 = myroute.legs[1].start_address
    const wayapoint = 'one'
    sessionStorage.setItem("wxp", wayapoint)
    document.getElementById("data101x").innerHTML = '<b>pickup location :- </b><p id="p1">'+ originX+ " " +'</p><b> drop location :- </b><p id="d1">'+wayapathX1+'</p>';
    document.getElementById("data101y").innerHTML = '<b>drop location 2 :- </b><p id="d2">'+ destinationX+'</p>';
  }

  else if(sessionStorage.getItem('Rdx') == 3){
    const originX_lat = myroute.legs[0].start_location.lat()
    const originX_lng = myroute.legs[0].start_location.lng()
    const destinationX_lat = myroute.legs[2].end_location.lat()
    const destinationX_lng = myroute.legs[2].end_location.lng()
    const wayapathX1_lat = myroute.legs[1].start_location.lat()
    const wayapathX1_lng = myroute.legs[1].start_location.lng()
    const wayapathX2_lat = myroute.legs[2].start_location.lat()
    const wayapathX2_lng = myroute.legs[2].start_location.lng()

    const originX = myroute.legs[0].start_address
    const destinationX = myroute.legs[2].end_address
    const wayapathX1 = myroute.legs[1].start_address
    const wayapathX2 = myroute.legs[2].start_address
    const wayapoint = 'two'
    sessionStorage.setItem("wxp", wayapoint)
    document.getElementById("data101x").innerHTML = '<b>pickup location :- </b><p id="p1">'+ originX+'</p><b> drop location :- </b><p id="d1">'+wayapathX1+'</p>';
    document.getElementById("data101y").innerHTML = '<b>drop location 2:- </b><p id="d2">'+ wayapathX2+ " " +'</p><b> drop location 3:- </b><p id="d3">'+destinationX+'</p>';
  }

}

// update the searched location
function UpdateSearchLocation(){
  document.querySelector(".map101").style.display = "none";
  document.querySelector(".map102").style.display = "none";
  document.querySelector(".display101").style.display = "none";
  document.querySelector(".SelectTruck").style.display = "block";
  const MainData = [];
  var wayapoint = sessionStorage.getItem("wxp");
  console.log(document.getElementById("data101y").innerHTML)
  if(wayapoint == "zero"){
    let datax = {"origin":document.getElementById("p1").innerHTML, "destination":document.getElementById("d1").innerHTML, "distance":sessionStorage.getItem('dX'), "RDX":"zero"}
    MainData.push(datax);
  }
  else if(wayapoint == "one"){
    let datax = {"origin":document.getElementById("p1").innerHTML, "wayapath1":document.getElementById("d1").innerHTML ,"destination":document.getElementById("d2").innerHTML, "distance":sessionStorage.getItem('dX'), "RDX":"one"}
    MainData.push(datax);
  }
  else if(wayapoint == "two"){
    let datax = {"origin":document.getElementById("p1").innerHTML, "wayapath1":document.getElementById("d1").innerHTML, "wayapath2":document.getElementById("d2").innerHTML ,"destination":document.getElementById("d3").innerHTML, "distance":sessionStorage.getItem('dX'), "RDX":"two"}
    MainData.push(datax);
  }
  const data = MainData[0];
  fetch("http://127.0.0.1:8000/updateLocationRequest/", {
	
    // Adding method type
    method: "POST",
    
    // Adding body or contents to send
    body: JSON.stringify(data),
    
    // Adding headers to the request
    headers: {
      "Content-type": "application/json",
      'Accept': 'application/json',
      "X-CSRFToken":csrftoken
    }
  }).then(response => {
    TruckDistanceLocation();
      response.json()
      console.log(response.status)
  })
  
  // Converting to JSON
  
  
  // Displaying results to console
  .then(data => {
  
  });
}

function TruckDistanceLocation(){
  fetch("http://127.0.0.1:8000/export/", {
	
  // Adding method type
  method: "GET",
  }).then(response => {
    console.log(response.status)
    return response.json()
  })
  // Converting to JSON
  // Displaying results to console
  .then(data => {
    console.log(data)
    if(data['list_micro'] !== 'undefined' && data['list_micro'].length > 0){
      document.getElementById('micro_t').innerHTML = data['list_micro'][0]['Time'];
      document.getElementById('micro_t_tp').innerHTML = data['list_micro'][0]['TruckType'];
      document.getElementById('micro_d').innerHTML = data['list_micro'][0]['Truck_Desc'];
      document.getElementById('micro_truck').value = data['list_micro'][0]['RegistrationNo'];
      document.getElementById('TruckData3x').innerHTML = '<a href="/RedirectTo"><button class="B_continue" id="MicroTUDT" onclick="AddTruckWithUser(this.id)">continue</button></a>';
    }
    if(data['list_mini'] !== 'undefined' && data['list_mini'].length > 0){
      document.getElementById('mini_t').innerHTML = data['list_mini'][0]['Time'];
      document.getElementById('mini_t_tp').innerHTML = data['list_mini'][0]['TruckType'];
      document.getElementById('mini_d').innerHTML = data['list_mini'][0]['Truck_Desc'];
      document.getElementById('mini_truck').value = data['list_mini'][0]['RegistrationNo'];
      document.getElementById('TruckData3mi').innerHTML = '<a href="/RedirectTo"><button class="B_continue" id="MiniTUDT" onclick="AddTruckWithUser(this.id)">continue</button></a>';
    }
    if(data['list_medium'] !== 'undefined' && data['list_medium'].length > 0){
      document.getElementById('medium_t').innerHTML = data['list_medium'][0]['Time'];
      document.getElementById('medium_t_tp').innerHTML = data['list_medium'][0]['TruckType'];
      document.getElementById('medium_d').innerHTML = data['list_medium'][0]['Truck_Desc'];
      document.getElementById('medium_truck').value = data['list_medium'][0]['RegistrationNo'];
      document.getElementById('TruckData3me').innerHTML = '<a href="/RedirectTo"><button class="B_continue" id="MediumTUDT" onclick="AddTruckWithUser(this.id)">continue</button></a>';
    }
    if(data['list_max'] !== 'undefined' && data['list_max'].length > 0){
      document.getElementById('max_t').innerHTML = data['list_max'][0]['Time'];
      document.getElementById('max_t_tp').innerHTML = data['list_max'][0]['TruckType'];
      document.getElementById('max_d').innerHTML = data['list_max'][0]['Truck_Desc'];
      document.getElementById('max_truck').value = data['list_max'][0]['RegistrationNo'];
      document.getElementById('TruckData3max').innerHTML = '<a href="/RedirectTo"><button class="B_continue" id="MaxTUDT" onclick="AddTruckWithUser(this.id)">continue</button></a>';
    }
    if(data['list_ultra_Max'] !== 'undefined' && data['list_ultra_Max'].length > 0){
      document.getElementById('umax_t').innerHTML = data['list_ultra_Max'][0]['Time'];
      document.getElementById('umax_t_tp').innerHTML = data['list_ultra_Max'][0]['TruckType'];
      document.getElementById('umax_d').innerHTML = data['list_ultra_Max'][0]['Truck_Desc'];
      document.getElementById('umax_truck').value = data['list_ultra_Max'][0]['RegistrationNo'];
      document.getElementById('TruckData3umax').innerHTML = '<a href="/RedirectTo"><button class="B_continue" id="UMaxTUDT" onclick="AddTruckWithUser(this.id)">continue</button></a>';
    }
    console.log(data['list_mini'])
    console.log(data['list_medium'])
    console.log(data['list_max'])
    console.log(data['list_ultra_Max'])
});
}

function DisplayPoup(){
  document.querySelector(".display101").style.display = "block";
}
function ClosePoup(){
  document.querySelector(".display101").style.display = "none";
}
function closePopup(){
  document.querySelector(".display101").style.display = "none";
}

function reOprn101(){
  document.querySelector(".map101").style.display = "none";
  document.querySelector(".map102").style.display = "none";
  document.querySelector(".SelectTruck").style.display = "block";
}

function closeSetOTP(){
  document.querySelector(".map101").style.display = "block";
  document.querySelector(".map102").style.display = "block";
  document.querySelector(".getOTP").style.display = "none";
}

function onlyNumberKey(evt) {
          
  // Only ASCII character in that range allowed
  var ASCIICode = (evt.which) ? evt.which : evt.keyCode
  if (ASCIICode > 31 && (ASCIICode < 48 || ASCIICode > 57))
      return false;
  return true;
}

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}

const csrftoken = getCookie('csrftoken');

// POST request using fetch()
function OpenSetOTP(e){
  if(document.getElementById("OTP_phoneNo").value == ''){
    alert("Please Enter Valid Mobile Number");
  }

  else if(document.getElementById("OTP_phoneNo").value.length  < 10){
    alert("Please Enter Valid Mobile Number");
  }
  else{
    document.getElementById("goToVerification").href = "http://127.0.0.1:8000/renderVerification/";
  fetch("http://127.0.0.1:8000/SaveOTPContact/", {
	
	// Adding method type
	method: "POST",
	
	// Adding body or contents to send
	body: JSON.stringify({
		"Contact": document.getElementById("OTP_phoneNo").value
	}),
	
	// Adding headers to the request
	headers: {
		"Content-type": "application/json",
    'Accept': 'application/json',
    "X-CSRFToken":csrftoken
	}
}).then(response => response.json())

// Converting to JSON


// Displaying results to console
.then(data => {

});
}
}

function AddTruckWithUser(t_ID){
  const TRNOData = []
  const TruckType = []
if(t_ID == 'MicroTUDT'){
  const TRNO = document.getElementById("micro_truck").value
  TRNOData.push(TRNO)
  TruckType.push('micro')
}
else if(t_ID == 'MiniTUDT'){
  const TRNO = document.getElementById("mini_truck").value
  TRNOData.push(TRNO)
  TruckType.push('mini')
}
else if(t_ID == 'MediumTUDT'){
  const TRNO = document.getElementById("medium_truck").value
  TRNOData.push(TRNO)
  TruckType.push('medium')
}
else if(t_ID == 'MaxTUDT'){
  const TRNO = document.getElementById("max_truck").value
  TRNOData.push(TRNO)
  TruckType.push('max')
}
else if(t_ID == 'UMaxTUDT'){
  const TRNO = document.getElementById("umax_truck").value
  TRNOData.push(TRNO)
  TruckType.push('ultramax')
}
else{
  const TRNO = document.getElementById("micro_truck").value
  TRNOData.push(TRNO)
  TruckType.push('mini')
}

console.log(TRNOData[0])
let varX = TRNOData[0]
let vary = TruckType[0]
  fetch("http://127.0.0.1:8000/updateTRNO/", {
	// Adding method type
	method: "POST",
	
	// Adding body or contents to send
	body: JSON.stringify({
		"TRNO": varX,
		"Truck_type": vary
	}),
	
	// Adding headers to the request
	headers: {
		"Content-type": "application/json",
    'Accept': 'application/json',
    "X-CSRFToken":csrftoken
	}
}).then(response =>{
  response.json()
  if(response.status == "400"){
    alert('please enter correct otp')
  }
})
// Converting to JSON
// Displaying results to console
.then(data => {

});
}
// function VerifyOTP(){

//   fetch("http://127.0.0.1:8000/VerifyOTP/", {
	
// 	// Adding method type
// 	method: "POST",
	
// 	// Adding body or contents to send
// 	body: JSON.stringify({
// 		"OTP": document.getElementById("OTPVerify").value
// 	}),
	
// 	// Adding headers to the request
// 	headers: {
// 		"Content-type": "application/json",
//     'Accept': 'application/json',
//     "X-CSRFToken":csrftoken
// 	}
// }).then(response =>{
//   response.json()
//   if(response.status == "400"){
//     alert('please enter correct otp')
//   }
//   else{
//     document.querySelector(".setOTP").style.display = "none";
//   }
// })

// // Converting to JSON


// // Displaying results to console
// .then(data => {

// });

// }



// ********************* user hompage.html

function updateUX(){
  console.log(document.getElementById("NameUx").value)
  if(document.getElementById("NameUx").value == ""){
    alert('plese enter your name')
  }
  else{
    fetch("http://127.0.0.1:8000/updateUX/", {
    
    // Adding method type
    method: "POST",
    
    // Adding body or contents to send
    body: JSON.stringify({
      "Name": document.getElementById("NameUx").value,
      "Email": document.getElementById("EmailUx").value
    }),
    
    // Adding headers to the request
    headers: {
      "Content-type": "application/json",
      'Accept': 'application/json',
      "X-CSRFToken":csrftoken
    }
  }).then(response =>{
    response.json()
    if(response.status == "500"){
      document.querySelector(".container_fillName").style.display = "none";
      document.querySelector("#overlay2").style.display = "none";
    }
    else{
      alert('please enter your name')
    }
  })
  // Displaying results to console
  .then(data => {

  });
  }
}

// cancleing booking********************

function CancleBooking(){
  fetch("http://127.0.0.1:8000/updateBStatusCancle/", {
    
    // Adding method type
    method: "POST",
    
    // Adding body or contents to send
    body: JSON.stringify({
      "status": "cancle",
    }),
    
    // Adding headers to the request
    headers: {
      "Content-type": "application/json",
      'Accept': 'application/json',
      "X-CSRFToken":csrftoken
    }
  }).then(response =>{
    response.json()
    if(response.status == "500"){
      document.querySelector(".containerDisplayBookingDetails").style.display = "none";
    }
    // else{
    //   alert('please enter your name')
    // }
  })
  // Displaying results to console
  .then(data => {

  });
}

function picUserImgFFX(){

}