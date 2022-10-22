
window.addEventListener('click',(e)=>{   
    if (document.querySelector("#b_user").contains(e.target)){
      // Clicked in box
      document.querySelector(".logout_body").style.display = "block";
    } else{
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

  const add_truck = document.getElementById("add_truck");

  add_truck.addEventListener("click", ()=>{
    document.querySelector(".truck_content_modal").style.display="block";
  })
  const Close_modal = document.getElementById("close_modal");
  Close_modal.addEventListener("click", ()=>{
    document.querySelector(".truck_content_modal").style.display="none";
  })

  function term_and_condition_popup(){
    document.querySelector(".driver_Terms_Conditions_modal").style.display = "block";
  }
  

  function Driver_close_agree_modal(){
    document.querySelector(".driver_Terms_Conditions_modal").style.display = "none";
  }

  function Driver_continue_agree_modal(){
    var Agree_checkbox = document.querySelector("#driver_agree_checkbox").checked
    if (Agree_checkbox == true) {
      document.querySelector(".driver_Terms_Conditions_modal").style.display = "none";
      document.querySelector(".Driver_content_modal").style.display = "block";
    }
  }

  function Close_modal_driver(){
    document.querySelector(".Driver_content_modal").style.display = "none";
  }
  
  function close_adding_truck_modal(e) {
    e.preventDefault
    // if()
    // document.querySelector(".truck_content_modal").style.display = "none";
  }

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
