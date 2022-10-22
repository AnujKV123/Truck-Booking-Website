
window.addEventListener('click', (e) => {
  if (document.querySelector("#b_user").contains(e.target)) {
    // Clicked in box
    document.querySelector(".logout_body").style.display = "block";
  } else {
    // Clicked outside the box
    document.querySelector(".logout_body").style.display = "none";
  }
});

  // open popup edit details
  window.addEventListener('click',(e)=>{   
    if (document.querySelector("#driver_link_Edit_Details").contains(e.target)){
      // Clicked in box
      document.querySelector(".container_driver_edit").style.display = "block";
    } else{
      // Clicked outside the box
      document.querySelector(".container_driver_edit").style.display = "none";
    }
    
  });

// PopUp_add_Truck()

function PopUp_add_Truck(){
  document.querySelector(".truck_content_modal").style.display = "block";
  document.querySelector(".truck_content_modalX").style.display = "none";
  document.querySelector(".truck_content_modalY").style.display = "none";
}

const Close_modal = document.getElementById("close_modal");
Close_modal.addEventListener("click", () => {
  document.querySelector(".truck_content_modal").style.display = "none";
})


// PopUp_truck_with_D()

function PopUp_truck_with_Driver(){
  document.querySelector(".truck_content_modalX").style.display = "block";
  document.querySelector(".truck_content_modal").style.display = "none";
  document.querySelector(".truck_content_modalY").style.display = "none";
}

const Close_modalX = document.getElementById("close_modalX");
Close_modalX.addEventListener("click", () => {
  document.querySelector(".truck_content_modalX").style.display = "none";
})


// PopUp_Create_Profile()

function PopUp_Create_Profile(){
  document.querySelector(".truck_content_modalY").style.display = "block";
  document.querySelector(".truck_content_modal").style.display = "none";
  document.querySelector(".truck_content_modalX").style.display = "none";
}

const Close_modalY = document.getElementById("close_modalY");
Close_modalY.addEventListener("click", () => {
  document.querySelector(".truck_content_modalY").style.display = "none";
})

// **************************

function show_aadhar(){
  document.getElementById("overlay1").style.display = "block";
  document.getElementById("container_aadhar_imgXX").style.display = "block";
}
function close_aadhar_imgXX(){
  document.getElementById("overlay1").style.display = "none";
  document.getElementById("container_aadhar_imgXX").style.display = "none";
}


function show_pan(){
  document.getElementById("overlay1").style.display = "block";
  document.getElementById("container_pan_imgXX").style.display = "block";
}
function close_pan_imgXX(){
  document.getElementById("overlay1").style.display = "none";
  document.getElementById("container_pan_imgXX").style.display = "none";
}


function show_lisence(){
  document.getElementById("overlay1").style.display = "block";
  document.getElementById("container_lisence_imgXX").style.display = "block";
}
function close_lisence_imgXX(){
  document.getElementById("overlay1").style.display = "none";
  document.getElementById("container_lisence_imgXX").style.display = "none";
}


// update driver picture
function Edit_Profile_Picture(){
  document.getElementById("container_edit_driver_box1").style.display = "block"
  document.getElementById("overlay2").style.display = "block"
}

function close_update_driver_img(){
  document.getElementById("container_edit_driver_box1").style.display = "none"
  document.getElementById("overlay2").style.display = "none"
}

// update driver aadhar
function Edit_Copy_of_Aadhar(){
  document.getElementById("container_edit_driver_box2").style.display = "block"
  document.getElementById("overlay2").style.display = "block"
}

function close_update_driver_aadhar(){
  document.getElementById("container_edit_driver_box2").style.display = "none"
  document.getElementById("overlay2").style.display = "none"
}

// update driver pan
function Edit_Copy_of_PAN(){
  document.getElementById("container_edit_driver_box3").style.display = "block"
  document.getElementById("overlay2").style.display = "block"
}

function close_update_driver_pan(){
  document.getElementById("container_edit_driver_box3").style.display = "none"
  document.getElementById("overlay2").style.display = "none"
}

// update driver license
function Edit_Copy_of_Driving_Licence(){
  document.getElementById("container_edit_driver_box4").style.display = "block"
  document.getElementById("overlay2").style.display = "block"
}

function close_update_driver_license(){
  document.getElementById("container_edit_driver_box4").style.display = "none"
  document.getElementById("overlay2").style.display = "none"
}

// update driver presionl details
function Edit_presional_Detail(){
  document.getElementById("container_edit_driver_box5").style.display = "block"
  document.getElementById("overlay2").style.display = "block"
}

function close_update_driver_P_details(){
  document.getElementById("container_edit_driver_box5").style.display = "none"
  document.getElementById("overlay2").style.display = "none"
}

// update driver bank detail
function Edit_bank_detail(){
  document.getElementById("container_edit_driver_box6").style.display = "block"
  document.getElementById("overlay2").style.display = "block"
}

function close_update_driver_Bank_detail(){
  document.getElementById("container_edit_driver_box6").style.display = "none"
  document.getElementById("overlay2").style.display = "none"
}
