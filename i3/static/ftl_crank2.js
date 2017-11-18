var volumeTickWidth = 0.03;
var maxRotation = 7200;
var minRotation = 0;
var volume = [];
var wheelDrag = {};
$(function() {
  volume = $("#volumeBar");

  $("#volumeBarHolder").width(maxRotation * volumeTickWidth + "px");

  wheelDrag = Draggable.create($("#wheel"), {
    type: "rotation",
    bounds: { minRotation: minRotation, maxRotation: maxRotation }
  })[0];
  wheelDrag.addEventListener("drag", onWheelDrag);
});

function onWheelDrag() {
  setVolumeWidth();
  if(wheelDrag.rotation == maxRotation){
     alert("FTL POWERED UP!!!!");
     }
}

function setVolumeWidth() {
  var width = Math.round(wheelDrag.rotation * volumeTickWidth);
  volume.width(width + "px");
}
