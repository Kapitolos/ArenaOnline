

function backgroundtoggle(enemy) {  
  enemyname = enemy;     
  const pageid = "body" + enemyname;
  document.getElementById('body').setAttribute('id', pageid);
} 

function anitoggle(idname) {
  console.log(idname);
  // const enemyname = idname;
  const animation = idname+"attack";
  console.log(animation);
  // document.getElementById(enemyname).setAttribute('id', animation);

}


 
function test() {
  console.log("Hello World");
}

// window.onload.console.log('working');